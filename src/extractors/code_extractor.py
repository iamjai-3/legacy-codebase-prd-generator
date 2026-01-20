"""
Code Extractor for processing legacy codebase files.
"""

import ast
import re
from dataclasses import dataclass, field
from pathlib import Path

import javalang
import sqlparse
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
    fields: list[str] = field(default_factory=list)
    extends: str | None = None
    implements: list[str] = field(default_factory=list)
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
        extracted_files = self._filter_extracted_files(
            extracted_files, dependency_paths, file_mappings, extract_dir
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
            code_files = self._process_files_by_dependencies(directory, dependency_paths)
        elif file_mappings:
            code_files = self._process_files_by_mappings(directory, file_mappings)
        else:
            code_files = self._process_all_code_files(directory)

        logger.info(
            "Extracted code files from directory",
            directory=str(directory),
            total_files=len(code_files),
            filtered=bool(dependency_paths or file_mappings),
        )

        return code_files

    def _filter_extracted_files(
        self,
        extracted_files: list[Path],
        dependency_paths: list[str] | None,
        file_mappings: list[str] | None,
        extract_dir: Path,
    ) -> list[Path]:
        """Filter extracted files by dependency paths or mappings."""
        if dependency_paths:
            filtered_files = [
                f for f in extracted_files if match_file_path(f, dependency_paths, extract_dir)
            ]
            logger.info(
                "Filtered files by dependency paths",
                total_extracted=len(filtered_files),
                dependency_paths=len(dependency_paths),
            )
            return filtered_files
        if file_mappings:
            mapping_set = {Path(m).name for m in file_mappings}
            filtered_files = [f for f in extracted_files if f.name in mapping_set]
            logger.info(
                "Filtered files by mappings",
                total_extracted=len(filtered_files),
                mappings_count=len(file_mappings),
            )
            return filtered_files
        return extracted_files

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
            classes, methods, imports, fields, extends, implements = (
                self._extract_code_structure_ast(content, language)
            )

            # Extract dependencies (keep existing method for regex fallback/augmentation)
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
                fields=fields,
                extends=extends,
                implements=implements,
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
        if file_path.suffix == ".sql":
            return self._determine_sql_type(content)
        if "adapter" in name:
            return "adapter"
        if "service" in name:
            return "service"
        if "controller" in name or "action" in name:
            return "controller"
        if "model" in name or "entity" in name:
            return "model"
        if "util" in name or "helper" in name:
            return "utility"
        if "test" in name:
            return "test"
        return "source"

    def _determine_sql_type(self, content: str) -> str:
        """Determine SQL file type based on content."""
        content_lower = content.lower()
        if "create table" in content_lower:
            return "ddl"
        if "insert" in content_lower or "update" in content_lower:
            return "dml"
        return "query"

    def _extract_code_structure_ast(
        self, content: str, language: str
    ) -> tuple[list[str], list[str], list[str], list[str], str | None, list[str]]:
        """
        Extract code structure using AST parsing.

        Returns:
            Tuple of (classes, methods, imports, fields, extends, implements)
        """
        try:
            if language == "java":
                return self._parse_java_ast(content)
            elif language == "python":
                return self._parse_python_ast(content)
            elif language == "sql":
                return self._parse_sql_ast(content)
        except Exception as e:
            logger.warning(f"AST parsing failed for {language}, falling back to regex: {e}")

        # Fallback to regex (for other languages or if AST fails)
        # Note: Regex doesn't extract fields, extends, implements reliably yet
        c, m, i = self._extract_code_structure(content, language)
        return c, m, i, [], None, []

    def _parse_java_ast(
        self, content: str
    ) -> tuple[list[str], list[str], list[str], list[str], str | None, list[str]]:
        """Parse Java Content using javalang."""
        classes = []
        methods = []
        imports = []
        fields = []
        extends = None
        implements = []

        try:
            tree = javalang.parse.parse(content)
            self._extract_java_imports(tree, imports)
            extends = self._extract_java_classes(tree, classes, methods, fields, implements)
            self._extract_java_interfaces(tree, classes, implements)
        except Exception as e:
            logger.debug(f"Javalang parse error: {e}")
            raise e

        return classes, methods, imports, fields, extends, implements

    def _extract_java_imports(self, tree, imports: list[str]) -> None:
        """Extract imports from Java AST."""
        for path, node in tree.filter(javalang.tree.Import):
            imports.append(node.path)

    def _extract_java_classes(
        self, tree, classes: list[str], methods: list[str], fields: list[str], implements: list[str]
    ) -> str | None:
        """Extract class declarations from Java AST."""
        extends = None
        for path, node in tree.filter(javalang.tree.ClassDeclaration):
            classes.append(node.name)
            if node.extends and extends is None:
                extends = node.extends.name
            if node.implements:
                implements.extend([i.name for i in node.implements])

            # Extract ALL fields including private ones
            for field in node.fields:
                for declarator in field.declarators:
                    field_name = declarator.name
                    # Include field type information
                    field_type = ""
                    if field.type:
                        if isinstance(field.type, javalang.tree.ReferenceType):
                            if hasattr(field.type.name, '__iter__'):
                                field_type = ".".join(field.type.name)
                            else:
                                field_type = str(field.type.name)
                        elif hasattr(field.type, 'name'):
                            field_type = str(field.type.name)
                        else:
                            field_type = str(field.type)
                    # Store as "name:type" for better context
                    if field_type:
                        fields.append(f"{field_name}:{field_type}")
                    else:
                        fields.append(field_name)

            for method in node.methods:
                methods.append(method.name)
        return extends

    def _extract_java_interfaces(self, tree, classes: list[str], implements: list[str]) -> None:
        """Extract interface declarations from Java AST."""
        for path, node in tree.filter(javalang.tree.InterfaceDeclaration):
            classes.append(node.name)
            if node.extends:
                implements.extend([i.name for i in node.extends])

    def _parse_python_ast(
        self, content: str
    ) -> tuple[list[str], list[str], list[str], list[str], str | None, list[str]]:
        """Parse Python Content using ast."""
        classes = []
        methods = []
        imports = []
        fields = []
        extends = None

        try:
            tree = ast.parse(content)
            extends_ref = [extends]
            self._extract_python_nodes(tree, classes, methods, imports, extends_ref)
            extends = extends_ref[0]

        except Exception as e:
            logger.debug(f"Python AST parse error: {e}")
            raise e

        return classes, methods, imports, fields, extends, []

    def _extract_python_nodes(
        self, tree, classes: list[str], methods: list[str], imports: list[str], extends_ref: list
    ) -> None:
        """Extract nodes from Python AST."""
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                self._extract_python_imports(node, imports)
            elif isinstance(node, ast.ImportFrom):
                self._extract_python_import_from(node, imports)
            elif isinstance(node, ast.ClassDef):
                self._extract_python_class(node, classes, methods, extends_ref)
            elif isinstance(node, ast.FunctionDef) and node.name not in methods:
                methods.append(node.name)

    def _extract_python_imports(self, node: ast.Import, imports: list[str]) -> None:
        """Extract import statements."""
        for alias in node.names:
            imports.append(alias.name)

    def _extract_python_import_from(self, node: ast.ImportFrom, imports: list[str]) -> None:
        """Extract import from statements."""
        module = node.module or ""
        for alias in node.names:
            imports.append(f"{module}.{alias.name}")

    def _extract_python_class(
        self, node: ast.ClassDef, classes: list[str], methods: list[str], extends_ref: list
    ) -> None:
        """Extract class definition."""
        classes.append(node.name)
        for base in node.bases:
            if isinstance(base, ast.Name) and extends_ref[0] is None:
                extends_ref[0] = base.id

        for item in node.body:
            if isinstance(item, ast.FunctionDef):
                methods.append(item.name)

    def _parse_sql_ast(
        self, content: str
    ) -> tuple[list[str], list[str], list[str], list[str], str | None, list[str]]:
        """Parse SQL Content using sqlparse."""
        tables = []
        operations = []
        columns = []

        try:
            parsed = sqlparse.parse(content)
            for statement in parsed:
                type_ = statement.get_type()
                if type_ != "UNKNOWN":
                    operations.append(type_)

                if type_ == "CREATE":
                    self._extract_create_table_info(statement, tables, columns)
                found_tables = self._extract_tables_from_statement(statement)
                tables.extend(list(found_tables))

            # Dedupe
            tables = list(set(tables))
            operations = list(set(operations))
            columns = list(set(columns))

        except Exception as e:
            logger.debug(f"SQL parsing error: {e}")

        return tables, operations, [], columns, None, []

    def _extract_create_table_info(self, statement, tables: list[str], columns: list[str]) -> None:
        """Extract table and column info from CREATE TABLE statement."""
        for token in statement.tokens:
            if isinstance(token, sqlparse.sql.Identifier):
                tables.append(token.get_real_name())
            elif isinstance(token, sqlparse.sql.Parenthesis):
                self._extract_columns_from_parenthesis(token, columns)

    def _extract_columns_from_parenthesis(self, token, columns: list[str]) -> None:
        """Extract columns from parenthesis token."""
        for sub_token in token.tokens:
            if isinstance(sub_token, sqlparse.sql.IdentifierList):
                for identifier in sub_token.get_identifiers():
                    if isinstance(identifier, sqlparse.sql.Identifier):
                        columns.append(identifier.get_real_name())
            elif isinstance(sub_token, sqlparse.sql.Identifier):
                columns.append(sub_token.get_real_name())

    def _extract_tables_from_statement(self, statement) -> set[str]:
        """Extract table names from SQL statement."""

        tables = set()
        idx = 0
        if not hasattr(statement, "tokens"):
            return tables

        while idx < len(statement.tokens):
            token = statement.tokens[idx]
            if token.is_group:
                tables.update(self._extract_tables_from_statement(token))

            if self._is_table_keyword(token):
                idx = self._extract_table_after_keyword(statement, idx, tables)
            idx += 1
        return tables

    def _is_table_keyword(self, token) -> bool:
        """Check if token is a keyword that precedes table names."""
        from sqlparse.tokens import Keyword

        if token.ttype not in (Keyword, Keyword.DML):
            return False
        return token.value.upper() in ["FROM", "JOIN", "UPDATE", "INTO"]

    def _extract_table_after_keyword(self, statement, idx: int, tables: set[str]) -> int:
        """Extract table name after a keyword and return new index."""
        from sqlparse.sql import Function, Identifier, IdentifierList
        from sqlparse.tokens import Comment, Whitespace

        idx += 1
        while idx < len(statement.tokens) and statement.tokens[idx].ttype in (
            Whitespace,
            Comment,
        ):
            idx += 1
        if idx < len(statement.tokens):
            next_token = statement.tokens[idx]
            if isinstance(next_token, Identifier):
                tables.add(next_token.get_real_name())
            elif isinstance(next_token, IdentifierList):
                for id_token in next_token.get_identifiers():
                    if isinstance(id_token, Identifier):
                        tables.add(id_token.get_real_name())
            elif isinstance(next_token, Function):
                tables.add(next_token.get_real_name())
        return idx

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
                if matches:
                    first_match = matches[0]
                    if isinstance(first_match, str):
                        dependencies.extend(matches)

        return list(set(dependencies))

    def to_documents(self, code_files: list[CodeFile], form_name: str) -> list[Document]:
        """
        Convert CodeFile objects to LangChain Documents for vectorization.
        
        Creates separate chunks for:
        - Class definitions (with all fields)
        - Method implementations (business logic)
        - Field mappings (legacy codes → normalized fields)
        - Validation rules (extracted patterns)

        Args:
            code_files: List of parsed code files
            form_name: Name of the form these files belong to

        Returns:
            List of LangChain Documents with enhanced metadata
        """
        documents: list[Document] = []

        for code_file in code_files:
            # Determine document type based on file characteristics
            is_dto = any("DTO" in c or "dto" in c.lower() for c in code_file.classes) or "dto" in code_file.path.lower()
            is_model = code_file.file_type == "model" or "model" in code_file.path.lower()
            is_support = "Support" in code_file.path or "support" in code_file.path.lower()
            
            # Create class definition document (for DTOs/models)
            if is_dto or is_model:
                class_doc = self._create_class_definition_document(code_file, form_name)
                if class_doc:
                    documents.append(class_doc)
            
            # Create method/business logic documents
            if code_file.methods:
                method_docs = self._create_method_documents(code_file, form_name)
                documents.extend(method_docs)
            
            # Create comprehensive code document (fallback for other files)
            if not (is_dto or is_model):
                comprehensive_doc = self._create_comprehensive_document(code_file, form_name)
                documents.append(comprehensive_doc)

        logger.info("Converted code files to documents", count=len(documents), files=len(code_files))

        return documents
    
    def _create_class_definition_document(self, code_file: CodeFile, form_name: str) -> Document | None:
        """Create a document focused on class definition with all fields."""
        if not code_file.classes:
            return None
            
        text_parts = [
            f"File: {code_file.path}",
            f"Class Definition: {', '.join(code_file.classes)}",
            f"Language: {code_file.language}",
            "",
        ]
        
        if code_file.extends:
            text_parts.append(f"Extends: {code_file.extends}")
        if code_file.implements:
            text_parts.append(f"Implements: {', '.join(code_file.implements)}")
        
        text_parts.append("")
        text_parts.append("## All Fields:")
        if code_file.fields:
            for field in code_file.fields:
                text_parts.append(f"- {field}")
        else:
            text_parts.append("- No fields detected")
        
        text_parts.append("")
        text_parts.append("## Full Class Code:")
        # Include up to 8000 chars for better context
        text_parts.append(code_file.content[:8000])
        
        metadata = {
            "form_name": form_name,
            "file_path": code_file.path,
            "language": code_file.language,
            "file_type": code_file.file_type,
            "classes": code_file.classes,
            "fields": code_file.fields,  # Include ALL fields
            "extends": code_file.extends,
            "implements": code_file.implements,
            "line_count": code_file.line_count,
            "doc_type": "class_definition",
            "chunk_type": "class_definition",
        }
        
        return Document(
            page_content="\n".join(text_parts),
            metadata=metadata,
        )
    
    def _create_method_documents(self, code_file: CodeFile, form_name: str) -> list[Document]:
        """Create separate documents for important methods (business logic)."""
        documents = []
        
        # Focus on methods that likely contain business logic
        important_methods = [
            m for m in code_file.methods 
            if any(keyword in m.lower() for keyword in [
                "save", "update", "delete", "create", "validate", "check", 
                "does", "using", "get", "set", "action"
            ])
        ]
        
        # If too many methods, prioritize the important ones
        methods_to_process = important_methods[:10] if len(important_methods) > 10 else code_file.methods[:15]
        
        for method_name in methods_to_process:
            # Extract method content using regex
            method_pattern = rf'(?:public|private|protected)?\s*(?:static\s+)?(?:\w+\s+)?{re.escape(method_name)}\s*\([^)]*\)\s*(?:throws\s+[\w,\s]+)?\s*\{{([^{{}}]*(?:\{{[^{{}}]*\}}[^{{}}]*)*)'
            match = re.search(method_pattern, code_file.content, re.MULTILINE | re.DOTALL)
            
            if match:
                method_body = match.group(0)[:8000]  # Up to 8000 chars
                line_num = code_file.content[:match.start()].count('\n') + 1
                
                text_parts = [
                    f"File: {code_file.path}",
                    f"Method: {method_name}",
                    f"Line: {line_num}",
                    f"Class: {', '.join(code_file.classes) if code_file.classes else 'N/A'}",
                    "",
                    "## Method Implementation:",
                    method_body,
                ]
                
                metadata = {
                    "form_name": form_name,
                    "file_path": code_file.path,
                    "language": code_file.language,
                    "file_type": code_file.file_type,
                    "method_name": method_name,
                    "classes": code_file.classes,
                    "line_number": line_num,
                    "doc_type": "business_logic",
                    "chunk_type": "method_implementation",
                }
                
                documents.append(Document(
                    page_content="\n".join(text_parts),
                    metadata=metadata,
                ))
        
        return documents
    
    def _create_comprehensive_document(self, code_file: CodeFile, form_name: str) -> Document:
        """Create a comprehensive document for files that aren't DTOs/models."""
        text_parts = [
            f"File: {code_file.path}",
            f"Language: {code_file.language}",
            f"Type: {code_file.file_type}",
            "",
        ]

        if code_file.classes:
            text_parts.append(f"Classes: {', '.join(code_file.classes)}")

        if code_file.methods:
            text_parts.append(f"Methods: {', '.join(code_file.methods[:30])}")

        if code_file.fields:
            text_parts.append(f"Fields: {', '.join(code_file.fields)}")

        if code_file.imports:
            text_parts.append(f"Imports: {', '.join(code_file.imports[:15])}")

        text_parts.extend(["", "## Code:", code_file.content[:8000]])  # Increased from 1500 to 8000

        metadata = {
            "form_name": form_name,
            "file_path": code_file.path,
            "language": code_file.language,
            "file_type": code_file.file_type,
            "classes": code_file.classes,
            "methods": code_file.methods[:30],
            "fields": code_file.fields,
            "extends": code_file.extends,
            "implements": code_file.implements,
            "line_count": code_file.line_count,
            "doc_type": "code",
            "chunk_type": "comprehensive",
        }

        return Document(
            page_content="\n".join(text_parts),
            metadata=metadata,
        )

    def get_form_mapping(
        self,
        form_name: str,
        mapping_file: str | Path | None = None,
        file_patterns: list[str] | None = None,  # Reserved for future use
    ) -> FormMapping:
        """
        Get file mapping for a specific form.

        Args:
            form_name: Name of the form (e.g., 'le01')
            mapping_file: Optional JSON file with mappings
            file_patterns: Optional list of file patterns (reserved for future use)

        Returns:
            FormMapping object
        """
        # Suppress unused parameter warning - reserved for future use
        _ = file_patterns
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
