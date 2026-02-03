# PRD Agent 🚀

**AI-powered Product Requirements Document Generation and Code Migration**

PRD Agent is a comprehensive system that generates detailed Product Requirements Documents (PRDs) from legacy codebases and migrates them to modern frameworks using AI agents. It creates a vector knowledge base for semantic search and uses Anthropic Claude or OpenAI for intelligent code generation.

## 🌟 Features

- **Multi-Source Analysis**: Extracts insights from code, UI screenshots, and documentation
- **Agentic Code Migration**: AI agents that reason and generate modern code (like Antigravity IDE)
- **Vector Knowledge Base**: Searchable embeddings using Qdrant + OpenAI
- **PostgreSQL Caching**: Smart caching for LLM responses, vector searches, and tool results
- **Temporal Orchestration**: Enterprise-grade workflow execution with fault tolerance
- **Comprehensive PRD Output**: Detailed migration specifications and documentation

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
- Docker & Docker Compose
- OpenAI API key (for embeddings) + Anthropic or OpenAI API key (for LLM)

### Quick Start

1. **Clone and configure**:

```bash
git clone <repo>
cd PRD_Agent
cp env.example .env
# Edit .env with your API keys:
# - ANTHROPIC_API_KEY or OPENAI_API_KEY
# - LLM_PROVIDER=anthropic or openai
```

2. **Start infrastructure**:

```bash
docker-compose up -d
# Starts: PostgreSQL, Temporal, Qdrant, MinIO, n8n
```

3. **Install dependencies**:

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

4. **Create MinIO folders** (first time only):

```bash
prd-agent create-minio-folders
prd-agent create-form-folders LE11
# Upload files via MinIO UI at http://localhost:9001
```

5. **Start Temporal worker** (in separate terminal):

```bash
python -m src.worker.temporal_worker
```

6. **Generate PRD**:

```bash
prd-agent generate -f le11 -o ./output
```

7. **Migrate code with AI**:

```bash
prd-agent migrate-agentic -f le11 -o ./output/agentic
```

### Available Commands

```bash
prd-agent generate           # Generate PRD from legacy code
prd-agent migrate-agentic    # Migrate code using AI agents
prd-agent list-collections   # List vector collections
prd-agent search             # Search knowledge base
prd-agent stats              # Get collection statistics
prd-agent delete-collection  # Delete collection and form data
prd-agent cache-stats        # View cache statistics
prd-agent cache-clear        # Clear cache entries
prd-agent version            # Show version
```

**See `cmds.md` for detailed command documentation.**

## 🎯 Usage

### PRD Generation

```bash
# Generate PRD (loads code from MinIO)
prd-agent generate -f le11 -o ./output

# Generate PRD with local ZIP
prd-agent generate -f le11 -z ./code.zip -o ./output

# Generate PRD with local code directory
prd-agent generate -f le11 -c ./src/code -o ./output
```

**What it does:**

- Extracts code from legacy codebase
- Analyzes UI screenshots from MinIO
- Analyzes database schemas
- Creates vector knowledge base in Qdrant
- Generates comprehensive PRD document

### Agentic Code Migration

```bash
# Migrate to .NET + React using AI agents
prd-agent migrate-agentic -f le11 -o ./output/agentic

# With verbose output
prd-agent migrate-agentic -f le11 -o ./output/agentic -v

# With custom prompt
prd-agent migrate-agentic -f le11 -o ./output/agentic \
  -p "Focus on database entities and API endpoints"
```

**What it does:**

- Uses Anthropic Claude for reasoning and planning
- Searches vector knowledge base for context
- Generates ASP.NET Core backend with EF Core
- Generates React frontend with TypeScript
- Creates complete project structure

### Knowledge Base Search

```bash
# Search all content
prd-agent search -f le11 -q "validation rules" -l 10

# Search specific types
prd-agent search -f le11 -q "save method" -t code
prd-agent search -f le11 -q "field mapping" -t existing_prd
prd-agent search -f le11 -q "table schema" -t database

# Get statistics
prd-agent stats -f le11

# List all collections
prd-agent list-collections
```

### Cache Management

```bash
# View cache statistics
prd-agent cache-stats

# Clear specific cache type
prd-agent cache-clear -t llm_response --yes
prd-agent cache-clear -t vector_search --yes

# Clear all cache
prd-agent cache-clear --yes
```

### MinIO Management

```bash
# Create folder structure
prd-agent create-minio-folders

# Create form-specific folders
prd-agent create-form-folders LE11

# Delete form data
prd-agent delete-collection -f le11 --yes
```

## 🤖 AI Agent System

### PRD Generation Agents

**1. ScreenshotAnalysisAgent**

- Analyzes UI screenshots using GPT-4 Vision
- Identifies components, layouts, and interactions
- Extracts form fields and validation hints

**2. RequirementsGeneratorAgent**

- Generates functional and non-functional requirements
- Creates data models and entity definitions
- Documents validation rules and business logic

**3. UserFlowAgent**

- Documents user journeys step-by-step
- Creates Mermaid flow diagrams
- Identifies entry/exit points and error paths

**4. DatabaseAnalysisAgent**

- Analyzes database schemas and relationships
- Maps form fields to database tables
- Documents queries and stored procedures

**5. PRDAggregatorAgent**

- Combines all analyses into comprehensive PRD
- Creates executive summary and recommendations
- Structures output with proper formatting

### Agentic Code Migration System

**Migration Orchestrator**

- Coordinates backend and frontend migration
- Uses Anthropic Claude with tool calling
- Searches knowledge base for context
- Generates complete project structures

**Code Generation Agent**

- Generates ASP.NET Core API projects
- Creates Entity Framework entities and repositories
- Implements business logic and validation
- Generates React components and services

**UI Migration Agent**

- Creates React frontend with TypeScript
- Implements forms with validation
- Generates API service layer
- Creates component library structure

**Database Migration Agent**

- Generates EF Core entity models
- Creates database context and configurations
- Implements repository pattern
- Generates migration scripts

### Tool System

Agents have access to tools:

- **File Tools**: Read, write, create directories
- **Code Tools**: Search codebase, analyze structure
- **Database Tools**: Query schemas, analyze relationships
- **MinIO Tools**: Read form docs and templates

## 📁 Project Structure

```
PRD_Agent/
├── src/
│   ├── core/                        # Core functionality
│   │   ├── prd/                     # PRD Generation agents
│   │   │   ├── base_agent.py
│   │   │   ├── screenshot_analysis_agent.py
│   │   │   ├── requirements_generator_agent.py
│   │   │   ├── user_flow_agent.py
│   │   │   ├── database_analysis_agent.py
│   │   │   └── prd_aggregator_agent.py
│   │   ├── migration/               # Code migration agents
│   │   │   ├── migration_orchestrator.py
│   │   │   ├── code_generation_agent.py
│   │   │   ├── ui_migration_agent.py
│   │   │   └── db_migration_agent.py
│   │   └── agentic/                 # Agentic AI framework
│   │       ├── agentic_base.py      # Base agent class
│   │       ├── agent_runner.py      # Orchestration
│   │       ├── message_history.py   # Conversation management
│   │       └── tool_registry.py     # Tool registration
│   ├── tools/                       # Agent tools
│   │   ├── file_tools.py
│   │   ├── code_tools.py
│   │   ├── database_tools.py
│   │   ├── database_knowledge_tool.py
│   │   └── minio_tools.py
│   ├── extractors/                  # Data extraction
│   │   ├── code_extractor.py
│   │   ├── minio_extractor.py
│   │   └── prd_extractor.py
│   ├── workflows/                   # Temporal workflows
│   │   ├── activities/
│   │   └── prd_generation_workflow.py
│   ├── vector_store/                # Qdrant knowledge base
│   │   ├── embeddings.py
│   │   └── qdrant_manager.py
│   ├── cli/                         # CLI commands
│   │   └── commands.py
│   ├── worker/                      # Temporal worker
│   │   └── temporal_worker.py
│   ├── config/                      # Configuration
│   │   └── settings.py
│   ├── prompts/                     # LLM prompts
│   └── utils/                       # Utilities
├── tests/                           # Test suite
├── docker-compose.yml               # Infrastructure
├── requirements.txt                 # Dependencies
└── pyproject.toml                   # Project config
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

## 🧠 Vector Knowledge Base

The system creates a searchable vector knowledge base using Qdrant:

| Source      | Location                       | Content                      | Doc Type                 |
| ----------- | ------------------------------ | ---------------------------- | ------------------------ |
| Legacy Code | `LEGACY_CODEBASE/*.zip`        | Java classes, methods, logic | `code`, `business_logic` |
| Form Docs   | `FORMS/{FORM}/FORM_DOCS/`      | Requirements, specifications | `existing_prd`           |
| DB Schema   | `DB_PRD/`                      | Tables, relationships        | `database`               |
| Screenshots | `FORMS/{FORM}/UI_SCREENSHOTS/` | UI analysis results          | `screenshot_analysis`    |

### Searching the Knowledge Base

```bash
# Search all content
prd-agent search -f le11 -q "validation rules" -l 10

# Search specific doc types
prd-agent search -f le11 -q "save method" -t code
prd-agent search -f le11 -q "field mapping" -t existing_prd
prd-agent search -f le11 -q "table schema" -t database
prd-agent search -f le11 -q "UI components" -t screenshot_analysis

# Get statistics
prd-agent stats -f le11
```

### Performance

With **PostgreSQL caching**:

- LLM responses: 3-5s → ~100ms (cached)
- Vector searches: ~500ms → ~50ms (cached)
- Tool results: 1-2s → ~50ms (cached)

Expected: **30-50% faster PRD generation** for similar forms!

## 🔄 Code Migration

After generating the PRD and knowledge base, migrate to modern frameworks:

```bash
# Step 1: Generate PRD and build knowledge base
prd-agent generate -f le11 -o ./output

# Step 2: Migrate using AI agents (like Antigravity IDE)
prd-agent migrate-agentic -f le11 -o ./output/agentic -v
```

### Migration Output Structure

```
output/agentic/
├── backend/
│   └── Le11Management/
│       ├── Le11Management.API/          # ASP.NET Core Web API
│       │   ├── Controllers/
│       │   ├── Program.cs
│       │   └── appsettings.json
│       ├── Le11Management.Business/     # Business logic layer
│       │   ├── Services/
│       │   └── Interfaces/
│       ├── Le11Management.Data/         # Data access layer
│       │   ├── Entities/
│       │   ├── Repositories/
│       │   └── DbContext/
│       └── Le11Management.Common/       # Shared models
│           ├── DTOs/
│           └── Validators/
└── frontend/
    └── le11-management/
        ├── src/
        │   ├── components/              # React components
        │   ├── pages/                   # Page components
        │   ├── services/                # API service layer
        │   ├── hooks/                   # Custom hooks
        │   ├── types/                   # TypeScript types
        │   └── utils/                   # Utilities
        ├── package.json
        └── tsconfig.json
```

### Tech Stack

**Backend:**

- ASP.NET Core 8.0 Web API
- Entity Framework Core 8.0
- PostgreSQL database
- Repository pattern
- FluentValidation

**Frontend:**

- React 18 with TypeScript
- TanStack Query for data fetching
- shadcn/ui component library
- Tailwind CSS
- React Hook Form + Zod

## ⚙️ Configuration

### Environment Variables

**LLM Configuration:**

| Variable                 | Description        | Default                       |
| ------------------------ | ------------------ | ----------------------------- |
| `LLM_PROVIDER`           | LLM provider       | `openai` or `anthropic`       |
| `ANTHROPIC_API_KEY`      | Anthropic API key  | Required if using Anthropic   |
| `ANTHROPIC_MODEL`        | Claude model       | `claude-sonnet-4-5-20250929`  |
| `OPENAI_API_KEY`         | OpenAI API key     | Required (for embeddings/LLM) |
| `OPENAI_MODEL`           | GPT model          | `gpt-4o`                      |
| `OPENAI_EMBEDDING_MODEL` | Embedding model    | `text-embedding-3-large`      |
| `EMBEDDING_PROVIDER`     | Embedding provider | `openai`                      |

**Infrastructure:**

| Variable           | Description       | Default          |
| ------------------ | ----------------- | ---------------- |
| `QDRANT_HOST`      | Qdrant host       | `localhost`      |
| `QDRANT_PORT`      | Qdrant port       | `6333`           |
| `TEMPORAL_HOST`    | Temporal host     | `localhost`      |
| `TEMPORAL_PORT`    | Temporal port     | `7233`           |
| `MINIO_ENDPOINT`   | MinIO endpoint    | `localhost:9000` |
| `MINIO_BUCKET`     | MinIO bucket name | `metadatas`      |
| `MINIO_ACCESS_KEY` | MinIO access key  | `minioadmin`     |
| `MINIO_SECRET_KEY` | MinIO secret key  | `minioadmin`     |

**Cache Configuration (uses Temporal PostgreSQL):**

| Variable                  | Description             | Default     |
| ------------------------- | ----------------------- | ----------- |
| `CACHE_ENABLED`           | Enable caching          | `true`      |
| `CACHE_HOST`              | PostgreSQL host         | `localhost` |
| `CACHE_PORT`              | PostgreSQL port         | `5432`      |
| `CACHE_DATABASE`          | Database name           | `temporal`  |
| `CACHE_USER`              | Database user           | `temporal`  |
| `CACHE_PASSWORD`          | Database password       | `temporal`  |
| `CACHE_LLM_RESPONSE_TTL`  | LLM cache TTL (seconds) | `86400`     |
| `CACHE_VECTOR_SEARCH_TTL` | Search cache TTL        | `3600`      |
| `CACHE_TOOL_RESULT_TTL`   | Tool cache TTL          | `1800`      |

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

## 🔍 Monitoring

### Temporal UI

Monitor workflow execution:

```bash
open http://localhost:8080
```

View:

- Workflow status and history
- Activity execution details
- Errors and retry attempts
- Event timeline

### MinIO Console

Manage object storage:

```bash
open http://localhost:9001
# Login: minioadmin / minioadmin
```

### Qdrant Dashboard

Explore vector collections:

```bash
open http://localhost:6333/dashboard
```

### Cache Statistics

Monitor cache effectiveness:

```bash
prd-agent cache-stats
```

## 🧪 Testing

```bash
# Run tests
pytest

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Run specific test
pytest tests/test_workflow.py -v

# Test connections
curl http://localhost:6333/health        # Qdrant
curl http://localhost:9000/minio/health/live  # MinIO
```

## 🚀 Production Readiness

### Architecture Benefits

✅ **Enterprise-grade orchestration** with Temporal (fault tolerance, retries, state management)  
✅ **Scalable vector search** with Qdrant (handles large codebases)  
✅ **Smart caching** with PostgreSQL (reduces LLM costs and latency)  
✅ **Agentic AI system** with Anthropic Claude (reasoning and tool use)  
✅ **Clean folder structure** following DRY principles  
✅ **Comprehensive tooling** for file operations, code analysis, and database queries

### Best Practices

- Use `migrate-agentic` for complex migrations requiring reasoning
- Run `generate` first to build knowledge base
- Monitor workflows via Temporal UI
- Check cache statistics regularly
- Use verbose mode (`-v`) for debugging

### Performance Tips

1. **Enable caching** for faster repeated operations
2. **Use vector search** to find relevant code quickly
3. **Monitor Temporal workflows** for bottlenecks
4. **Adjust TTL values** based on cache hit rates

## 📚 Documentation

- `cmds.md` - Complete command reference with examples
- `CACHE_USAGE.txt` - Cache integration guide and usage
- `env.example` - Environment configuration template

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

---

**Built with:** Python, Anthropic Claude, OpenAI, Temporal, Qdrant, PostgreSQL, MinIO
