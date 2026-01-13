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
| `JIRA_URL`               | Jira instance URL | -                        |
| `JIRA_API_TOKEN`         | Jira API token    | -                        |

## 🔄 Workflow Execution

The Temporal workflow orchestrates the entire process:

```
Phase 1: Data Extraction (Parallel)
  ├── Extract code from ZIP/directory
  ├── Fetch screenshots from Minio
  └── Query Jira for documentation

Phase 2: Vector Storage
  └── Create embeddings and store in Qdrant

Phase 3: Initial Analysis (Parallel)
  ├── Screenshot analysis
  └── Jira analysis

Phase 4: Requirements Generation
  └── Generate functional/non-functional requirements

Phase 5: Flow & Risk Analysis (Parallel)
  ├── User flow documentation
  └── Risk assessment

Phase 6: PRD Aggregation
  └── Combine all insights into PRD

Phase 7: Output
  └── Save PRD markdown and metadata
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
