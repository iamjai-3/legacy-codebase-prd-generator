# PRD Agent 🚀

**AI-powered Product Requirements Document Generation for Legacy Code Migration**

PRD Agent is a comprehensive system that generates detailed Product Requirements Documents (PRDs) from legacy codebases, UI screenshots, and Jira documentation. It creates a vector knowledge base for each form/module, enabling intelligent code migration to modern frameworks.

## 🌟 Features

- **Multi-Source Analysis**: Extracts insights from code, screenshots, and Jira
- **Specialized AI Agents**: Purpose-built agents for different analysis tasks
- **Vector Knowledge Base**: Creates searchable embeddings using Qdrant
- **Temporal Orchestration**: Reliable workflow execution with retries
- **Comprehensive PRD Output**: Markdown documents with full migration specs

## 🏗️ Architecture

```
PRD Agent Workflow
┌─────────────────────────────────────────────────────────────────┐
│                                                                 │
│  ┌─────────────┐  ┌─────────────┐  ┌─────────────┐            │
│  │ Code ZIP    │  │ Screenshots │  │ Jira Docs   │            │
│  │ + Mappings  │  │ (Minio)     │  │             │            │
│  └──────┬──────┘  └──────┬──────┘  └──────┬──────┘            │
│         │                │                │                    │
│         ▼                ▼                ▼                    │
│  ┌──────────────────────────────────────────────────┐         │
│  │            Data Extraction Layer                 │         │
│  │  CodeExtractor │ MinioExtractor │ JiraExtractor  │         │
│  └──────────────────────────┬───────────────────────┘         │
│                             │                                  │
│                             ▼                                  │
│  ┌──────────────────────────────────────────────────┐         │
│  │         Vector Store (Qdrant Collection)         │         │
│  │              OpenAI Embeddings                   │         │
│  └──────────────────────────┬───────────────────────┘         │
│                             │                                  │
│         ┌───────────────────┼───────────────────┐             │
│         ▼                   ▼                   ▼              │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐      │
│  │ Screenshot  │     │ Atlassian   │     │Requirements │      │
│  │ Analysis    │     │ Integration │     │ Generator   │      │
│  │ Agent       │     │ Agent       │     │ Agent       │      │
│  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘      │
│         │                   │                   │              │
│         └───────────────────┼───────────────────┘              │
│                             │                                  │
│         ┌───────────────────┼───────────────────┐             │
│         ▼                   ▼                   ▼              │
│  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐      │
│  │ User Flow   │     │    Risk     │     │    PRD      │      │
│  │ Agent       │     │  Analysis   │     │ Aggregator  │      │
│  │             │     │   Agent     │     │   Agent     │      │
│  └─────────────┘     └─────────────┘     └──────┬──────┘      │
│                                                 │              │
│                                                 ▼              │
│                                          ┌─────────────┐      │
│                                          │  PRD.md     │      │
│                                          │  Document   │      │
│                                          └─────────────┘      │
│                                                                │
│                    Temporal Workflow Orchestration             │
└─────────────────────────────────────────────────────────────────┘
```

## 📦 Installation

### Prerequisites

- Python 3.11+
- Docker & Docker Compose (for Qdrant, Temporal, Minio)
- OpenAI API key

### Quick Start

1. **Clone and setup**:

```bash
cd PRD_Agent
cp env.example .env
# Edit .env with your OpenAI API key
```

2. **Start infrastructure**:

```bash
docker-compose up -d
```

3. **Install dependencies**:

```bash
pip install -e .
# or
pip install -r requirements.txt
```

4. **Run the worker**:

```bash
python -m src.worker.temporal_worker
```

5. **Generate a PRD**:

```bash
prd-agent generate -f le01 -z ./code.zip -o ./output
```

# Available commands:

```bash
prd-agent generate          # Generate a PRD
prd-agent list-collections  # List vector collections
prd-agent search            # Search knowledge base
prd-agent stats             # Get collection stats
prd-agent delete-collection # Delete a collection
prd-agent version
```

## 🎯 Usage

### CLI Commands

```bash
# Generate PRD for a form
prd-agent generate \
  --form-name le01 \
  --zip-path ./oases-master.zip \
  --bucket screenshots \
  --jira-project OASES \
  --output ./output


prd-agent generate \
  -f le07 \
  -z src/templates_code_zip/oases-master.zip \
  -d src/form_dependencies/le07_dependencies.txt \
  -b <minio-bucket> \
  -o ./output

# Direct execution (without Temporal)
prd-agent generate -f le01 -z ./code.zip --direct

# List vector collections
prd-agent list-collections

# Search knowledge base
prd-agent search -f le01 -q "validation rules" -l 10

# Get collection stats
prd-agent stats -f le01

# Delete a collection
prd-agent delete-collection -f le01 --yes
```

### Programmatic Usage

```python
import asyncio
from src.main import generate_prd

async def main():
    result = await generate_prd(
        form_name="le01",
        zip_path="./oases-master.zip",
        minio_bucket="screenshots",
        jira_project="OASES",
        output_dir="./output",
    )

    if result["success"]:
        print(f"PRD generated: {result['prd_file']}")
    else:
        print(f"Error: {result['error']}")

asyncio.run(main())
```

### Using the PRDGenerator Class

```python
from src.generators.prd_generator import PRDGenerator, PRDGenerationConfig

config = PRDGenerationConfig(
    form_name="le01",
    zip_path="./code.zip",
    file_mappings=["LE01Adapter.java", "LE01Service.java"],
    minio_bucket="screenshots",
    jira_project_key="OASES",
    output_dir="./output",
)

generator = PRDGenerator()
result = await generator.generate(config)
```

## 🤖 Specialized Agents

### 1. ScreenshotAnalysisAgent

Analyzes UI screenshots using GPT-4 Vision to:

- Identify UI components and their types
- Understand screen layouts and hierarchy
- Extract user interaction patterns
- Document form fields and validation hints

### 2. AtlassianIntegrationAgent

Connects to Jira to extract:

- User stories and requirements
- Acceptance criteria
- Business rules from descriptions
- Stakeholder comments and feedback

### 3. RequirementsGeneratorAgent

Generates comprehensive requirements:

- Functional requirements (FR-XXX)
- Non-functional requirements (NFR-XXX)
- Data requirements and entity models
- Validation rules and business logic

### 4. UserFlowAgent

Documents user journeys:

- Step-by-step user flows
- Entry and exit points
- Alternative paths and error scenarios
- Mermaid flow diagrams

### 5. RiskAnalysisAgent

Identifies migration risks:

- Technical complexity assessment
- Dependency analysis
- Resource and timeline risks
- Mitigation strategies

### 6. PRDAggregatorAgent

Combines all analyses into:

- Executive summary
- Structured PRD document
- Migration recommendations
- Appendices and references

## 📁 Project Structure

```
PRD_Agent/
├── src/
│   ├── agents/                 # Specialized AI agents
│   │   ├── base_agent.py
│   │   ├── screenshot_analysis_agent.py
│   │   ├── atlassian_integration_agent.py
│   │   ├── requirements_generator_agent.py
│   │   ├── user_flow_agent.py
│   │   ├── risk_analysis_agent.py
│   │   └── prd_aggregator_agent.py
│   ├── extractors/             # Data extraction modules
│   │   ├── code_extractor.py
│   │   ├── minio_extractor.py
│   │   └── jira_extractor.py
│   ├── workflows/              # Temporal workflows
│   │   ├── activities.py
│   │   └── prd_generation_workflow.py
│   ├── vector_store/           # Qdrant integration
│   │   ├── embeddings.py
│   │   └── qdrant_manager.py
│   ├── generators/             # PRD generation
│   │   └── prd_generator.py
│   ├── cli/                    # CLI commands
│   │   └── commands.py
│   ├── worker/                 # Temporal worker
│   │   └── temporal_worker.py
│   ├── config/                 # Configuration
│   │   └── settings.py
│   └── utils/                  # Utilities
│       ├── file_utils.py
│       └── logging_config.py
├── tests/                      # Test suite
├── docker-compose.yml          # Infrastructure
├── requirements.txt            # Dependencies
└── pyproject.toml             # Project config
```

## 📂 MinIO Folder Structure

The system uses MinIO for storing all input data. Default bucket: `metadata`

```
metadata/
├── DB_PRD/                              # Database documentation
│   ├── schema.md
│   └── table_mappings.md
│
├── EXPORT_CODEBASE_PRD/                 # Migration prompt templates
│   ├── BE/dotnet_backend_conversion_prompt.txt
│   └── FE/react_frontend_conversion_prompt.txt
│
├── FORMS/{FORM_NAME}/                   # Form-specific data (e.g., LE11)
│   ├── FORM_DOCS/                       # Markdown documentation
│   ├── FORM_FILE_DEPENDENCIES/          # Code file dependencies
│   └── UI_SCREENSHOTS/                  # UI screenshots
│
└── LEGACY_CODEBASE/                     # Legacy source code ZIP
    └── oases-master.zip
```

## 🧠 Knowledge Base

The system creates a unified vector knowledge base from multiple sources:

| Source      | Content                               | Doc Type                 |
| ----------- | ------------------------------------- | ------------------------ |
| Legacy Code | Java classes, methods, business logic | `code`, `business_logic` |
| Form Docs   | Requirements, specifications          | `existing_prd`           |
| DB Schema   | Tables, relationships, mappings       | `database`               |
| Screenshots | UI analysis results                   | `screenshot_analysis`    |

### Searching the Knowledge Base

```bash
# Search all content
prd-agent search -f le11 -q "validation rules"

# Search specific doc types
prd-agent search -f le11 -q "save method" --type code
prd-agent search -f le11 -q "field mapping" --type existing_prd
prd-agent search -f le11 -q "table schema" --type database
```

## 🔄 Code Migration

After generating the PRD and knowledge base, migrate to modern frameworks:

```bash
# Generate PRD and build knowledge base
prd-agent generate -f le11 -o ./output

# Migrate to .NET + React
prd-agent migrate-code -f le11 -o ./output/migratedCode
```

### Migration Output

- **Backend**: ASP.NET Core with Entity Framework, PostgreSQL
- **Frontend**: React with TypeScript, TanStack Query, shadcn/ui

## ⚙️ Configuration

### Environment Variables

| Variable                 | Description       | Default                  |
| ------------------------ | ----------------- | ------------------------ |
| `OPENAI_API_KEY`         | OpenAI API key    | Required                 |
| `OPENAI_MODEL`           | Chat model        | `gpt-4o`                 |
| `OPENAI_EMBEDDING_MODEL` | Embedding model   | `text-embedding-3-large` |
| `QDRANT_HOST`            | Qdrant host       | `localhost`              |
| `QDRANT_PORT`            | Qdrant port       | `6333`                   |
| `TEMPORAL_HOST`          | Temporal host     | `localhost`              |
| `TEMPORAL_PORT`          | Temporal port     | `7233`                   |
| `MINIO_ENDPOINT`         | Minio endpoint    | `localhost:9000`         |
| `MINIO_BUCKET`           | MinIO bucket name | `metadata`               |
| `JIRA_URL`               | Jira instance URL | -                        |
| `JIRA_API_TOKEN`         | Jira API token    | -                        |

## 🔄 Workflow Execution

The Temporal workflow orchestrates the entire process:

```
Phase 1: Data Extraction (from MinIO)
  ├── Extract legacy code from LEGACY_CODEBASE/*.zip
  ├── Fetch screenshots from FORMS/{FORM}/UI_SCREENSHOTS/
  ├── Load form docs from FORMS/{FORM}/FORM_DOCS/
  └── Load DB docs from DB_PRD/

Phase 2: Vector Storage (Knowledge Base Creation)
  ├── Store code with FULL business logic (methods, classes)
  ├── Store form documentation (requirements, specs)
  ├── Store database schemas and mappings
  └── Store screenshot analysis results

Phase 3: Initial Analysis
  └── Screenshot analysis with GPT-4 Vision

Phase 4: Requirements Generation
  └── Generate requirements from knowledge base

Phase 5: User Flow Analysis
  └── Document user journeys and flows

Phase 6: Database Analysis
  └── Analyze form-specific table mappings

Phase 7: PRD Aggregation
  └── Combine all insights into comprehensive PRD

Phase 8: Output
  └── Save PRD markdown to output directory
```

### Code Migration Workflow

After PRD generation, the migration workflow:

```
1. Retrieve Knowledge Base Context
   ├── Business logic & methods (doc_type: business_logic)
   ├── Data models & entities (doc_type: code)
   ├── Form documentation (doc_type: existing_prd)
   ├── Database schemas (doc_type: database)
   └── UI context (doc_type: screenshot_analysis)

2. Generate Backend Specification
   └── JSON spec with entities, APIs, validations

3. Generate .NET Backend Code
   └── Using EXPORT_CODEBASE_PRD/BE/ template

4. Generate Frontend Specification
   └── JSON spec with forms, components, navigation

5. Generate React Frontend Code
   └── Using EXPORT_CODEBASE_PRD/FE/ template

6. Package Output
   └── Create ZIP archives for backend and frontend
```

## 📊 Output

### PRD Document Structure

1. **Executive Summary**
2. **User Interface** - Screen analysis and UI patterns
3. **Functional Requirements** - Detailed FR specifications
4. **Non-Functional Requirements** - Performance, security, etc.
5. **Data Model** - Entities, fields, relationships
6. **User Flows** - Step-by-step journeys with diagrams
7. **Business Rules** - Validation and logic rules
8. **Risk Assessment** - Risks and mitigation strategies
9. **Migration Strategy** - Recommended approach

### Vector Knowledge Base

Each form creates a Qdrant collection with:

- Code chunks with metadata (file, class, methods)
- Screenshot descriptions
- Jira issue content
- All queryable via semantic search

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Run specific test
pytest tests/test_workflow.py -v
```

## 🛠️ Development

```bash
# Install dev dependencies
pip install -e ".[dev]"

# Format code
black src tests

# Lint
ruff check src

# Type check
mypy src
```

## 📝 License

MIT License - See LICENSE file for details.

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Run tests
5. Submit a pull request

## 📞 Support

For issues or questions, please open a GitHub issue.
