"""
Code Extractor for processing legacy codebase files.
"""

import re
from dataclasses import dataclass, field
from pathlib import Path

from langchain_core.documents import Document

from src.config.settings import get_settings
from src.utils.dependency_parser import (
    match_file_path,
    parse_dependency_file,
)
from src.utils.file_utils import (
    extract_zip,
    get_file_extension,
    is_code_file,
    read_file_content,
)
from src.utils.logging_config import get_logger

logger = get_logger(__name__)


@dataclass
class CodeFile:
    """Represents a parsed code file."""

    path: str
    content: str
    language: str
    file_type: str
    classes: list[str] = field(default_factory=list)
    methods: list[str] = field(default_factory=list)
    imports: list[str] = field(default_factory=list)
    dependencies: list[str] = field(default_factory=list)
    line_count: int = 0


@dataclass
class FormMapping:
    """Mapping of form to its related code files."""

    form_name: str
    main_files: list[str]
    related_files: list[str]
    sql_files: list[str]
    form_files: list[str]


class CodeExtractor:
    """
    Extracts and analyzes code from legacy codebase archives.
    Supports Java, SQL, and form files commonly found in legacy systems.
    """

    LANGUAGE_MAP = {
        ".java": "java",
        ".py": "python",
        ".js": "javascript",
        ".ts": "typescript",
        ".tsx": "typescript",
        ".cs": "csharp",
        ".sql": "sql",
        ".xml": "xml",
        ".form": "java_form",
        ".properties": "properties",
    }

    def __init__(self) -> None:
        """Initialize the code extractor."""
        self.settings = get_settings()

    def extract_from_zip(
        self,
        zip_path: str | Path,
        extract_dir: str | Path | None = None,
        file_mappings: list[str] | None = None,
        dependency_file: str | Path | None = None,
    ) -> list[CodeFile]:
        """
        Extract and parse code files from a ZIP archive.

        Args:
            zip_path: Path to the ZIP file
            extract_dir: Optional extraction directory
            file_mappings: Optional list of specific file paths to extract
            dependency_file: Optional path to dependency file with file paths

        Returns:
            List of parsed CodeFile objects
        """
        zip_path = Path(zip_path)
        extract_dir = (
            Path(extract_dir) if extract_dir else Path(self.settings.uploads_dir) / zip_path.stem
        )

        # Parse dependency file if provided
        dependency_paths: list[str] | None = None
        if dependency_file:
            dependency_paths = parse_dependency_file(dependency_file)
            logger.info(
                "Loaded dependency file",
                file=str(dependency_file),
                paths_count=len(dependency_paths),
        )

        # Extract ZIP
        extracted_files = extract_zip(zip_path, extract_dir)

        # Filter by dependency paths or mappings if provided
        if dependency_paths:
            # Use dependency paths for filtering (full path matching)
            filtered_files = []
            for file_path in extracted_files:
                if match_file_path(file_path, dependency_paths, extract_dir):
                    filtered_files.append(file_path)
            extracted_files = filtered_files
            logger.info(
                "Filtered files by dependency paths",
                total_extracted=len(extracted_files),
                dependency_paths=len(dependency_paths),
            )
        elif file_mappings:
            # Fallback to simple filename matching for backward compatibility
            mapping_set = {Path(m).name for m in file_mappings}
            extracted_files = [f for f in extracted_files if f.name in mapping_set]
            logger.info(
                "Filtered files by mappings",
                total_extracted=len(extracted_files),
                mappings_count=len(file_mappings),
            )

        # Parse code files
        code_files: list[CodeFile] = []
        for file_path in extracted_files:
            if is_code_file(file_path):
                code_file = self._parse_code_file(file_path, extract_dir)
                if code_file:
                    code_files.append(code_file)

        logger.info(
            "Extracted code files from ZIP",
            zip=str(zip_path),
            total_files=len(code_files),
            filtered=bool(dependency_paths or file_mappings),
        )

        return code_files

    def extract_from_directory(
        self,
        directory: str | Path,
        file_mappings: list[str] | None = None,
        dependency_file: str | Path | None = None,
    ) -> list[CodeFile]:
        """
        Extract and parse code files from a directory.

        Args:
            directory: Path to the directory
            file_mappings: Optional list of specific file paths
            dependency_file: Optional path to dependency file with file paths

        Returns:
            List of parsed CodeFile objects
        """
        directory = Path(directory)
        code_files: list[CodeFile] = []

        # Parse dependency file if provided
        dependency_paths: list[str] | None = None
        if dependency_file:
            dependency_paths = parse_dependency_file(dependency_file)
            logger.info(
                "Loaded dependency file",
                file=str(dependency_file),
                paths_count=len(dependency_paths),
            )

        if dependency_paths:
            # Process files matching dependency paths
            for file_path in directory.rglob("*"):
                if file_path.is_file() and is_code_file(file_path):
                    if match_file_path(file_path, dependency_paths, directory):
                        code_file = self._parse_code_file(file_path, directory)
                        if code_file:
                            code_files.append(code_file)
        elif file_mappings:
            # Process specific files
            for mapping in file_mappings:
                file_path = directory / mapping
                if file_path.exists() and is_code_file(file_path):
                    code_file = self._parse_code_file(file_path, directory)
                    if code_file:
                        code_files.append(code_file)
        else:
            # Process all code files recursively
            for file_path in directory.rglob("*"):
                if file_path.is_file() and is_code_file(file_path):
                    code_file = self._parse_code_file(file_path, directory)
                    if code_file:
                        code_files.append(code_file)

        logger.info(
            "Extracted code files from directory",
            directory=str(directory),
            total_files=len(code_files),
            filtered=bool(dependency_paths or file_mappings),
        )

        return code_files

    def _parse_code_file(self, file_path: Path, base_path: Path) -> CodeFile | None:
        """
        Parse a single code file.

        Args:
            file_path: Path to the code file
            base_path: Base path for relative path calculation

        Returns:
            Parsed CodeFile or None if parsing fails
        """
        try:
            content = read_file_content(file_path)
            extension = get_file_extension(file_path)
            language = self.LANGUAGE_MAP.get(extension, "unknown")

            relative_path = str(file_path.relative_to(base_path))

            # Determine file type
            file_type = self._determine_file_type(file_path, content)

            # Extract code structure based on language
            classes, methods, imports = self._extract_code_structure(content, language)

            # Extract dependencies
            dependencies = self._extract_dependencies(content, language)

            return CodeFile(
                path=relative_path,
                content=content,
                language=language,
                file_type=file_type,
                classes=classes,
                methods=methods,
                imports=imports,
                dependencies=dependencies,
                line_count=content.count("\n") + 1,
            )

        except Exception as e:
            logger.warning("Failed to parse code file", file_path=str(file_path), error=str(e))
            return None

    def _determine_file_type(self, file_path: Path, content: str) -> str:
        """Determine the type of code file based on content and path."""
        name = file_path.name.lower()

        if file_path.suffix == ".form":
            return "form_definition"
        elif file_path.suffix == ".sql":
            if "create table" in content.lower():
                return "ddl"
            elif "insert" in content.lower() or "update" in content.lower():
                return "dml"
            else:
                return "query"
        elif "adapter" in name:
            return "adapter"
        elif "service" in name:
            return "service"
        elif "controller" in name or "action" in name:
            return "controller"
        elif "model" in name or "entity" in name:
            return "model"
        elif "util" in name or "helper" in name:
            return "utility"
        elif "test" in name:
            return "test"
        else:
            return "source"

    def _extract_code_structure(
        self, content: str, language: str
    ) -> tuple[list[str], list[str], list[str]]:
        """
        Extract classes, methods, and imports from code.

        Returns:
            Tuple of (classes, methods, imports)
        """
        classes: list[str] = []
        methods: list[str] = []
        imports: list[str] = []

        if language == "java":
            # Extract Java classes
            class_pattern = r"(?:public|private|protected)?\s*(?:abstract|final)?\s*class\s+(\w+)"
            classes = re.findall(class_pattern, content)

            # Extract Java methods
            method_pattern = r"(?:public|private|protected)\s+(?:static\s+)?(?:\w+\s+)?(\w+)\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{"
            methods = re.findall(method_pattern, content)

            # Extract Java imports
            import_pattern = r"import\s+([\w.]+);"
            imports = re.findall(import_pattern, content)

        elif language == "python":
            # Extract Python classes
            class_pattern = r"class\s+(\w+)"
            classes = re.findall(class_pattern, content)

            # Extract Python functions/methods
            method_pattern = r"def\s+(\w+)\s*\("
            methods = re.findall(method_pattern, content)

            # Extract Python imports
            import_pattern = r"(?:from\s+([\w.]+)\s+import|import\s+([\w.]+))"
            import_matches = re.findall(import_pattern, content)
            imports = [m[0] or m[1] for m in import_matches]

        return classes, methods, imports

    def _extract_dependencies(self, content: str, language: str) -> list[str]:
        """Extract external dependencies from code."""
        dependencies: list[str] = []

        if language == "java":
            # Common Java framework patterns
            patterns = [
                r"@Autowired",
                r"@Inject",
                r"extends\s+(\w+)",
                r"implements\s+([\w,\s]+)",
            ]
            for pattern in patterns:
                matches = re.findall(pattern, content)
                dependencies.extend(
                    matches if isinstance(matches[0] if matches else "", str) else []
                )

        return list(set(dependencies))

    def to_documents(self, code_files: list[CodeFile], form_name: str) -> list[Document]:
        """
        Convert CodeFile objects to LangChain Documents for vectorization.

        Args:
            code_files: List of parsed code files
            form_name: Name of the form these files belong to

        Returns:
            List of LangChain Documents
        """
        documents: list[Document] = []

        for code_file in code_files:
            # Create a comprehensive text representation
            text_parts = [
                f"File: {code_file.path}",
                f"Language: {code_file.language}",
                f"Type: {code_file.file_type}",
                "",
            ]

            if code_file.classes:
                text_parts.append(f"Classes: {', '.join(code_file.classes)}")

            if code_file.methods:
                text_parts.append(f"Methods: {', '.join(code_file.methods[:20])}...")  # Limit

            if code_file.imports:
                text_parts.append(f"Imports: {', '.join(code_file.imports[:10])}...")

            text_parts.extend(["", "Code:", code_file.content])

            metadata = {
                "form_name": form_name,
                "file_path": code_file.path,
                "language": code_file.language,
                "file_type": code_file.file_type,
                "classes": code_file.classes,
                "methods": code_file.methods[:20],  # Limit for metadata
                "line_count": code_file.line_count,
                "doc_type": "code",
            }

            document = Document(
                page_content="\n".join(text_parts),
                metadata=metadata,
            )
            documents.append(document)

        logger.info("Converted code files to documents", count=len(documents))

        return documents

    def get_form_mapping(
        self,
        form_name: str,
        mapping_file: str | Path | None = None,
        file_patterns: list[str] | None = None,
    ) -> FormMapping:
        """
        Get file mapping for a specific form.

        Args:
            form_name: Name of the form (e.g., 'le01')
            mapping_file: Optional JSON file with mappings
            file_patterns: Optional list of file patterns

        Returns:
            FormMapping object
        """
        if mapping_file:
            from src.utils.file_utils import read_json

            mappings = read_json(mapping_file)
            form_data = mappings.get(form_name, {})
            return FormMapping(
                form_name=form_name,
                main_files=form_data.get("main_files", []),
                related_files=form_data.get("related_files", []),
                sql_files=form_data.get("sql_files", []),
                form_files=form_data.get("form_files", []),
            )

        # Default patterns based on form name
        return FormMapping(
            form_name=form_name,
            main_files=[f"*{form_name}*.java"],
            related_files=["*Adapter*.java", "*Service*.java"],
            sql_files=[f"*{form_name}*.sql"],
            form_files=[f"*{form_name}*.form"],
        )
