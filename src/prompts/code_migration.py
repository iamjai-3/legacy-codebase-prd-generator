"""Prompts for Code Migration Agent."""

from pathlib import Path

from src.utils.logging_config import get_logger

logger = get_logger(__name__)


class CodeMigrationPrompts:
    """Prompts used by the CodeMigrationAgent for generating .NET and React code."""

    _backend_prompt_template: str | None = None
    _frontend_prompt_template: str | None = None

    @classmethod
    def _load_from_minio(cls, object_name: str) -> str | None:
        """
        Load a prompt template from MinIO.

        Args:
            object_name: Object name in MinIO (e.g., 'EXPORT_CODEBASE_PRD/dotnet_backend_conversion_prompt.txt')

        Returns:
            Template content as string, or None if not found
        """
        try:
            from src.utils.minio_sync import MinioSync

            minio_sync = MinioSync()
            if minio_sync.file_exists(object_name):
                content = minio_sync.get_file_text(object_name)
                logger.info(f"Loaded prompt template from MinIO: {object_name}")
                return content
            else:
                logger.debug(f"Prompt template not found in MinIO: {object_name}")
                return None
        except Exception as e:
            logger.warning(f"Failed to load prompt template from MinIO: {object_name}, error: {e}")
            return None

    @classmethod
    def _load_from_local(cls, filename: str) -> str | None:
        """
        Load a prompt template from local filesystem.

        Args:
            filename: Filename of the template (e.g., 'dotnet_backend_conversion_prompt.txt')

        Returns:
            Template content as string, or None if not found
        """
        try:
            template_path = Path(__file__).parent.parent / "export_codebase" / filename
            if template_path.exists():
                with open(template_path, encoding="utf-8") as f:
                    content = f.read()
                logger.info(f"Loaded prompt template from local: {template_path}")
                return content
            else:
                logger.debug(f"Prompt template not found locally: {template_path}")
                return None
        except Exception as e:
            logger.warning(f"Failed to load prompt template from local: {filename}, error: {e}")
            return None

    @classmethod
    def _load_backend_template(cls) -> str:
        """Load the .NET backend conversion prompt template from MinIO or local fallback."""
        if cls._backend_prompt_template is None:
            filename = "dotnet_backend_conversion_prompt.txt"
            minio_object = f"EXPORT_CODEBASE_PRD/BE/{filename}"

            # Try MinIO first
            template = cls._load_from_minio(minio_object)

            # Fallback to local file
            if template is None:
                template = cls._load_from_local(filename)

            if template is None:
                raise FileNotFoundError(
                    f"Backend conversion prompt template not found. "
                    f"Please upload '{filename}' to MinIO at '{minio_object}' "
                    f"or place it in 'src/export_codebase/' directory."
                )

            cls._backend_prompt_template = template
        return cls._backend_prompt_template

    @classmethod
    def _load_frontend_template(cls) -> str:
        """Load the React frontend conversion prompt template from MinIO or local fallback."""
        if cls._frontend_prompt_template is None:
            filename = "react_frontend_conversion_prompt.txt"
            minio_object = f"EXPORT_CODEBASE_PRD/FE/{filename}"

            # Try MinIO first
            template = cls._load_from_minio(minio_object)

            # Fallback to local file
            if template is None:
                template = cls._load_from_local(filename)

            if template is None:
                raise FileNotFoundError(
                    f"Frontend conversion prompt template not found. "
                    f"Please upload '{filename}' to MinIO at '{minio_object}' "
                    f"or place it in 'src/export_codebase/' directory."
                )

            cls._frontend_prompt_template = template
        return cls._frontend_prompt_template

    @staticmethod
    def backend_conversion_prompt(json_str: str, dependencies: str = "") -> str:
        """
        Format the .NET backend conversion prompt.

        Args:
            json_str: JSON specification of the Java Swing form backend
            dependencies: Dependencies information (optional)

        Returns:
            Formatted prompt string
        """
        template = CodeMigrationPrompts._load_backend_template()
        prompt = template.replace("{json_str}", json_str)
        prompt = prompt.replace(
            "{dependencies}", dependencies if dependencies else "No specific dependencies."
        )
        return prompt

    @staticmethod
    def frontend_conversion_prompt(json_str: str, swagger_json: str, dependencies: str = "") -> str:
        """
        Format the React frontend conversion prompt.

        Args:
            json_str: JSON specification of the Java Swing form frontend
            swagger_json: Swagger/OpenAPI JSON specification from backend
            dependencies: Dependencies information (optional)

        Returns:
            Formatted prompt string
        """
        template = CodeMigrationPrompts._load_frontend_template()
        prompt = template.replace("{json_str}", json_str)
        prompt = prompt.replace("{swagger_json}", swagger_json)
        prompt = prompt.replace(
            "{dependencies}", dependencies if dependencies else "No specific dependencies."
        )
        return prompt

    @staticmethod
    def system_prompt(form_name: str) -> str:
        """Get the system prompt for code migration."""
        return f"""You are a code migration specialist converting legacy Java Swing applications to modern .NET backend and React frontend.

Your task is to analyze the knowledge base for "{form_name}" and generate:
1. Complete .NET backend solution with ASP.NET Core, Entity Framework, and PostgreSQL
2. Complete React frontend application with TypeScript, TanStack Query, and shadcn/ui

CRITICAL REQUIREMENTS:
- Extract ALL business logic, data models, and API specifications from the knowledge base
- The generated code must match 100% with the legacy codebase functionality
- Generate production-ready code following best practices
- Ensure proper error handling and validation
- Create complete, runnable applications

REQUIRED .NET BACKEND STRUCTURE:
```
[FormName].API/
├── Controllers/           <- REQUIRED: One controller per entity
├── Program.cs            <- REQUIRED: Full DI configuration
└── appsettings.json

[FormName].Business/
├── DTOs/                 <- REQUIRED: Read, Create, Update DTOs per entity
├── Services/
│   ├── Interfaces/       <- REQUIRED: I[Entity]Service interfaces
│   └── Implementations/  <- REQUIRED: [Entity]Service with ALL business logic
├── Validators/           <- REQUIRED: Validation logic
└── Mappings/             <- AutoMapper profile

[FormName].Data/
├── Entities/             <- REQUIRED: ALL entities with ALL fields
├── Configurations/       <- REQUIRED: EF Core configurations
├── Context/              <- REQUIRED: DbContext
└── Repositories/         <- REQUIRED: Repository pattern

[FormName].Common/
├── Exceptions/           <- Custom exceptions
└── Models/               <- ApiResponse, PagedResult
```

REQUIRED REACT FRONTEND STRUCTURE:
```
src/
├── types/                <- REQUIRED: TypeScript interfaces for ALL entities
├── schemas/              <- REQUIRED: Zod schemas for validation
├── hooks/api/            <- REQUIRED: TanStack Query hooks for ALL endpoints
├── services/api/         <- REQUIRED: API service functions
├── components/
│   ├── [feature]/        <- REQUIRED: Components for EACH screen from PRD
│   │   ├── [Screen]Form.tsx
│   │   ├── [Screen]Table.tsx
│   │   └── index.tsx
│   └── common/           <- Shared components (dialogs, etc.)
├── pages/                <- Route pages
└── App.tsx               <- Main app with routing
```

The generated code MUST include ALL:
- Entities (with ALL fields from legacy code)
- Services (with ALL business logic methods)
- Controllers (with ALL endpoints from requirements)
- Frontend screens (ALL screens from PRD)
- Validation rules (ALL validations from legacy code)"""

    @staticmethod
    def get_backend_folder_structure(project_name: str = "Management") -> dict[str, list[str]]:
        """Get the required backend folder structure for validation."""
        return {
            f"{project_name}.API": [
                "Controllers/",
                "Program.cs",
                "appsettings.json",
            ],
            f"{project_name}.Business": [
                "DTOs/",
                "Services/Interfaces/",
                "Services/Implementations/",
                "Validators/",
                "Mappings/",
            ],
            f"{project_name}.Data": [
                "Entities/",
                "Configurations/",
                "Context/",
                "Repositories/Interfaces/",
                "Repositories/Implementations/",
            ],
            f"{project_name}.Common": [
                "Exceptions/",
                "Models/",
            ],
        }

    @staticmethod
    def get_frontend_folder_structure() -> dict[str, list[str]]:
        """Get the required frontend folder structure for validation."""
        return {
            "src": [
                "types/",
                "schemas/",
                "hooks/api/",
                "services/api/",
                "components/",
                "pages/",
                "App.tsx",
            ],
        }

    @staticmethod
    def get_required_backend_files(
        entities: list[str], project_name: str = "Management"
    ) -> list[str]:
        """Get list of required backend files based on entities."""
        required_files = [
            f"{project_name}.API/Program.cs",
            f"{project_name}.API/appsettings.json",
            f"{project_name}.Data/Context/{project_name}DbContext.cs",
            f"{project_name}.Business/Mappings/MappingProfile.cs",
            f"{project_name}.Common/Exceptions/NotFoundException.cs",
            f"{project_name}.Common/Models/ApiResponse.cs",
            f"{project_name}.Common/Models/PagedResult.cs",
        ]

        for entity in entities:
            required_files.extend(
                [
                    f"{project_name}.Data/Entities/{entity}.cs",
                    f"{project_name}.Data/Configurations/{entity}Configuration.cs",
                    f"{project_name}.Data/Repositories/Interfaces/I{entity}Repository.cs",
                    f"{project_name}.Data/Repositories/Implementations/{entity}Repository.cs",
                    f"{project_name}.Business/DTOs/{entity}/{entity}ReadDto.cs",
                    f"{project_name}.Business/DTOs/{entity}/{entity}CreateDto.cs",
                    f"{project_name}.Business/DTOs/{entity}/{entity}UpdateDto.cs",
                    f"{project_name}.Business/Services/Interfaces/I{entity}Service.cs",
                    f"{project_name}.Business/Services/Implementations/{entity}Service.cs",
                    f"{project_name}.Business/Validators/{entity}Validator.cs",
                    f"{project_name}.API/Controllers/{entity}Controller.cs",
                ]
            )

        return required_files

    @staticmethod
    def get_required_frontend_files(screens: list[str]) -> list[str]:
        """Get list of required frontend files based on screens."""
        required_files = [
            "src/types/index.ts",
            "src/schemas/index.ts",
            "src/hooks/api/index.ts",
            "src/lib/api.ts",
            "src/App.tsx",
        ]

        for screen in screens:
            screen_folder = screen.replace(" ", "")
            required_files.extend(
                [
                    f"src/components/{screen_folder}/index.tsx",
                    f"src/components/{screen_folder}/{screen_folder}Form.tsx",
                ]
            )

        return required_files
