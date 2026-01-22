# PRD Agent - Complete Project Documentation

**Version:** 1.0.0  
**Last Updated:** 2026-01-20  
**Purpose:** Comprehensive documentation for the AI-powered PRD Generation Agent for Legacy Code Migration

---

## Table of Contents

1. [Project Overview](#project-overview)
2. [System Architecture](#system-architecture)
3. [Complete Workflow](#complete-workflow)
4. [Core Components](#core-components)
5. [Installation & Setup](#installation--setup)
6. [Usage Guide](#usage-guide)
7. [Configuration](#configuration)
8. [Development Guide](#development-guide)
9. [Troubleshooting](#troubleshooting)
10. [API Reference](#api-reference)
11. [Best Practices](#best-practices)

---

## Project Overview

### What is PRD Agent?

PRD Agent is an AI-powered system that automatically generates comprehensive Product Requirements Documents (PRDs) from legacy codebases. It analyzes code, UI screenshots, and Jira documentation to create detailed migration specifications for modernizing legacy applications.

### Key Features

- **Multi-Source Analysis**: Extracts insights from code, screenshots, Jira issues, and existing PRD documents
- **Specialized AI Agents**: Purpose-built agents for different analysis tasks (screenshot analysis, requirements generation, user flow documentation, risk assessment)
- **Vector Knowledge Base**: Creates searchable embeddings using Qdrant for semantic code search
- **Temporal Orchestration**: Reliable workflow execution with automatic retries and fault tolerance
- **Comprehensive PRD Output**: Markdown documents with complete migration specs, field mappings, and business logic
- **Code Migration Support**: Generates .NET backend and React frontend code from knowledge base

### Use Cases

1. **Legacy Code Migration**: Generate PRDs for migrating Java/legacy applications to modern frameworks
2. **Documentation Generation**: Create comprehensive documentation for existing codebases
3. **Requirements Extraction**: Extract functional and non-functional requirements from code
4. **Business Logic Analysis**: Understand complex business rules and validation logic
5. **Data Model Extraction**: Extract complete data models with field mappings

### Technology Stack

- **Language**: Python 3.11+
- **Orchestration**: Temporal (workflow engine)
- **Vector Database**: Qdrant
- **AI/LLM**: OpenAI GPT-4, GPT-4 Vision, text-embedding-3-large
- **Storage**: MinIO (object storage for screenshots)
- **Integration**: Jira/Atlassian API
- **CLI**: Typer with Rich formatting

---

## System Architecture

### High-Level Architecture

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                           PRD Agent System                                   │
└─────────────────────────────────────────────────────────────────────────────┘
                                    │
                    ┌───────────────┼───────────────┐
                    │               │               │
                    ▼               ▼               ▼
        ┌──────────────┐  ┌──────────────┐  ┌──────────────┐
        │   CLI Layer  │  │  Temporal    │  │  Direct      │
        │  (Typer)     │  │  Workflow    │  │  Execution   │
        └──────┬───────┘  └──────┬───────┘  └──────┬───────┘
               │                 │                 │
               └─────────────────┼─────────────────┘
                                 │
                    ┌────────────▼────────────┐
                    │  PRD Generation Workflow │
                    │   (Temporal Orchestrator)│
                    └────────────┬────────────┘
                                 │
        ┌────────────────────────┼────────────────────────┐
        │                        │                        │
        ▼                        ▼                        ▼
┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│  Extraction   │      │   Analysis    │      │  Aggregation  │
│   Activities  │      │   Activities  │      │   Activities  │
└───────┬───────┘      └───────┬───────┘      └───────┬───────┘
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐      ┌───────────────┐      ┌───────────────┐
│   Extractors  │      │  AI Agents     │      │  PRD Writer   │
│               │      │                │      │               │
│ - Code        │      │ - Screenshot   │      │ - Aggregator  │
│ - Screenshots │      │ - Jira         │      │ - Formatter  │
│ - Jira        │      │ - Requirements │      │               │
│ - Existing PRD│      │ - User Flow    │      └───────┬───────┘
└───────┬───────┘      │ - Risk         │              │
        │              └────────────────┘              │
        └───────────────┼──────────────────────────────┘
                       │                               │
                       ▼                               ▼
              ┌─────────────────┐            ┌─────────────────┐
              │  Vector Store   │            │  Output Files   │
              │  (Qdrant)       │            │  (Markdown)     │
              └─────────────────┘            └─────────────────┘
```

### Component Layers

1. **CLI Layer**: User interface for triggering PRD generation
2. **Workflow Layer**: Temporal orchestration for reliable execution
3. **Extraction Layer**: Data extraction from various sources
4. **Analysis Layer**: AI-powered analysis using specialized agents
5. **Storage Layer**: Vector database for knowledge base
6. **Output Layer**: PRD document generation and formatting

---

## Complete Workflow

### Workflow Phases

The PRD generation process is divided into 8 distinct phases:

#### Phase 1: Data Extraction (Parallel)

Extracts data from all available sources:

- **Code Extraction**: Parses ZIP files or directories, extracts Java/SQL files, filters by dependencies
- **Screenshot Extraction**: Fetches UI screenshots from MinIO bucket
- **Jira Extraction**: Queries Jira API for issues and documentation
- **Existing PRD Extraction**: Reads existing PRD documents from `src/PRDs/` directory

**Activities:**
- `extract_code_activity`
- `extract_screenshots_activity`
- `extract_jira_activity`
- `extract_existing_prd_activity`

#### Phase 2: Vector Storage

Creates a unified knowledge base by storing all extracted data as vectors:

- Creates/recreates Qdrant collection for the form
- Generates embeddings using OpenAI text-embedding-3-large
- Stores code chunks, screenshot descriptions, Jira content, and PRD content
- Adds metadata tags (doc_type, chunk_type) for filtering

**Activity:**
- `store_vectors_activity`

**Vector Store Structure:**
- **Code Documents**: Class definitions, method implementations, comprehensive code
- **Screenshot Documents**: UI element descriptions, screen layouts
- **Jira Documents**: Issue descriptions, requirements, comments
- **PRD Documents**: Business logic, app flows, requirements from existing PRDs

#### Phase 3: Initial Analysis (Parallel)

Runs initial analysis agents in parallel:

- **Screenshot Analysis**: GPT-4 Vision analyzes UI screenshots
- **Jira Analysis**: GPT-4 extracts requirements and business context

**Activities:**
- `analyze_screenshots_activity`
- `analyze_jira_activity`

**Output:**
- UI element analysis, screen type classification, layout descriptions
- Requirements summary, issue categorization, business context

#### Phase 4: Requirements Generation

Generates comprehensive functional and non-functional requirements:

- Queries vector store for code context
- Incorporates Jira and screenshot context
- Generates functional requirements (FR-XXX) with acceptance criteria
- Generates non-functional requirements (NFR-XXX)
- Extracts data model requirements
- Extracts validation rules and business logic

**Activity:**
- `generate_requirements_activity`

**Output:**
- Functional requirements with source references
- Non-functional requirements (performance, security, etc.)
- Complete data model with all fields
- Validation rules and business rules
- Integration requirements

#### Phase 5: User Flow Analysis

Documents user journeys and workflows:

- Analyzes screenshot analysis results
- Queries vector store for code context
- Generates user flow diagrams (Mermaid format)
- Creates step-by-step user flows
- Documents alternative paths and error scenarios

**Activity:**
- `analyze_user_flows_activity`

**Output:**
- User flow diagrams (Mermaid)
- Step-by-step flows with actors
- Entry and exit points
- Success criteria

#### Phase 5.5: Store Analysis Results

Stores all analysis results back into the knowledge base:

- Adds screenshot analysis as vectors
- Adds requirements as vectors
- Adds user flows as vectors
- Enables future queries on analysis results

**Activity:**
- `store_analysis_results_activity`

#### Phase 6: PRD Aggregation

Combines all analysis results into a comprehensive PRD:

- Receives all previous agent results
- Generates structured PRD document
- Creates executive summary
- Formats all sections
- Calculates metrics

**Activity:**
- `aggregate_prd_activity`

**PRD Structure:**
1. Executive Summary
2. User Interface (screen analysis, UI patterns)
3. Functional Requirements (detailed FR specifications)
4. Non-Functional Requirements (performance, security, etc.)
5. Data Model (entities, fields, relationships, field mappings)
6. User Flows (step-by-step journeys with diagrams)
7. Business Rules (validation and logic rules)
8. Risk Assessment (risks and mitigation strategies)
9. Migration Strategy (field mapping, key transformation, migration guide)

#### Phase 7: Save PRD

Persists the final PRD document:

- Writes Markdown file
- Writes metadata JSON file

**Activity:**
- `save_prd_activity`

**Output Files:**
- `{form_name}_PRD.md`: Complete PRD document
- `{form_name}_PRD_metadata.json`: Metadata and metrics

### Workflow Execution Flow

```
START: User runs CLI command
│
├─► [CLI] Parse arguments
│
├─► [Workflow] Initialize PRDGenerationWorkflow
│
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 1: EXTRACTION (Parallel Activities)                          │
└─────────────────────────────────────────────────────────────────────┘
│
├─► [Activity] extract_code_activity
│   └─► CodeExtractor.extract_from_zip()
│       ├─► Parse ZIP file
│       ├─► Filter by dependency file
│       └─► Return: CodeFile[] objects
│
├─► [Activity] extract_screenshots_activity (if not skipped)
│   └─► MinioExtractor.get_form_screenshots()
│       └─► Return: Screenshot[] objects
│
├─► [Activity] extract_jira_activity (if not skipped)
│   └─► JiraExtractor.get_form_issues()
│       └─► Return: JiraIssue[] objects
│
└─► [Activity] extract_existing_prd_activity
    └─► PRDExtractor.extract_from_directory()
        └─► Return: PRDDocument[] objects
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 2: VECTOR STORAGE                                             │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] store_vectors_activity
    └─► QdrantManager
        ├─► Create collection (form_name)
        ├─► Generate embeddings (OpenAI)
        ├─► Store code as vectors
        ├─► Store screenshots as vectors
        ├─► Store Jira as vectors
        └─► Store existing PRD as vectors
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 3: INITIAL ANALYSIS (Parallel Agents)                        │
└─────────────────────────────────────────────────────────────────────┘
│
├─► [Activity] analyze_screenshots_activity (if not skipped)
│   └─► ScreenshotAnalysisAgent.analyze()
│       ├─► For each screenshot:
│       │   ├─► Send to GPT-4 Vision
│       │   ├─► Extract UI elements
│       │   └─► Classify screen type
│       ├─► Generate UI flow summary
│       └─► Return: ScreenshotAnalysisResult
│
└─► [Activity] analyze_jira_activity (if not skipped)
    └─► AtlassianIntegrationAgent.analyze()
        ├─► Query vector store for code context
        ├─► Analyze Jira issues with GPT-4
        └─► Return: AtlassianAnalysisResult
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 4: REQUIREMENTS GENERATION                                    │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] generate_requirements_activity
    └─► RequirementsGeneratorAgent.analyze()
        ├─► Query vector store for code context
        ├─► Receive: Jira context, Screenshot context
        ├─► Generate functional requirements (GPT-4)
        ├─► Generate non-functional requirements
        ├─► Generate data requirements
        ├─► Extract validation rules
        └─► Return: RequirementsResult
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 5: USER FLOW ANALYSIS                                         │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] analyze_user_flows_activity
    └─► UserFlowAgent.analyze()
        ├─► Query vector store for code context
        ├─► Receive: ScreenshotAnalysisResult
        ├─► Generate user flow diagrams (Mermaid)
        └─► Return: UserFlowResult
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 5.5: STORE ANALYSIS RESULTS                                   │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] store_analysis_results_activity
    └─► QdrantManager
        ├─► Store screenshot analysis as vectors
        ├─► Store requirements as vectors
        └─► Store user flows as vectors
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 6: PRD AGGREGATION                                            │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] aggregate_prd_activity
    └─► PRDAggregatorAgent.analyze()
        ├─► Receive: All previous agent results
        ├─► Generate PRD structure (GPT-4)
        ├─► Format all sections
        ├─► Create executive summary
        └─► Return: PRDContent (Markdown)
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 7: SAVE PRD                                                   │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] save_prd_activity
    ├─► Write PRD markdown file
    └─► Write metadata JSON file
│
END: Return PRDGenerationOutput
```

### Parallel Execution Strategy

The workflow maximizes efficiency by running independent activities in parallel:

**Parallel Group 1 (Phase 1):**
- Code extraction, Screenshot extraction, Jira extraction, PRD extraction

**Parallel Group 2 (Phase 3):**
- Screenshot analysis, Jira analysis

This reduces total workflow time by ~40% compared to sequential execution.

---

## Core Components

### 1. Agents

All agents inherit from `BaseAgent` which provides:
- LLM integration (OpenAI ChatOpenAI)
- Vector store access (QdrantManager)
- Context retrieval (semantic search)
- JSON response parsing
- Retry logic with exponential backoff
- Execution timing
- Structured logging

#### ScreenshotAnalysisAgent

**Purpose**: Analyze UI screenshots to understand user interface patterns

**Input**: Screenshot images from MinIO

**LLM**: GPT-4 Vision (gpt-4o)

**Output**:
- UI element analysis
- Screen type classification
- Layout descriptions
- User action identification
- Validation rules extraction
- UI flow summary

**Key Methods**:
- `analyze(context, screenshots)`: Main analysis method

#### AtlassianIntegrationAgent

**Purpose**: Extract and analyze requirements from Jira

**Input**: Jira issues and documentation

**LLM**: GPT-4

**Output**:
- Requirements summary
- Issue categorization
- Business context extraction

**Key Methods**:
- `analyze(context, issues)`: Main analysis method

#### RequirementsGeneratorAgent

**Purpose**: Generate comprehensive functional and non-functional requirements

**Input**: Code files, Jira context, Screenshot context

**LLM**: GPT-4

**Vector Store**: Queries code context

**Output**:
- Functional requirements with acceptance criteria
- Non-functional requirements
- Data model requirements
- Integration requirements
- Validation rules
- Business rules

**Key Methods**:
- `analyze(context, code_files, jira_context, screenshot_context)`: Main analysis method
- `_generate_functional_requirements()`: Generate FRs
- `_generate_data_requirements()`: Generate data model
- `_extract_validation_rules()`: Extract validation logic

#### UserFlowAgent

**Purpose**: Generate user flow diagrams and step-by-step flows

**Input**: Screenshot analysis, Code context

**LLM**: GPT-4

**Vector Store**: Queries code context

**Output**:
- User flow diagrams (Mermaid format)
- Step-by-step user flows
- Actor definitions
- Success criteria

**Key Methods**:
- `analyze(context, screenshot_analysis)`: Main analysis method

#### PRDAggregatorAgent

**Purpose**: Combine all analysis results into a comprehensive PRD

**Input**: All previous agent results

**LLM**: GPT-4

**Output**:
- Structured PRD document
- Executive summary
- All sections formatted
- Metrics and statistics

**Key Methods**:
- `analyze(context, screenshot_analysis, atlassian_analysis, requirements_analysis, user_flow_analysis)`: Main aggregation method
- `_generate_migration_mapping_section()`: Generate field mapping and migration guide

#### CodeMigrationAgent

**Purpose**: Generate .NET backend and React frontend code from knowledge base

**Input**: Form name, output directory

**LLM**: GPT-4

**Output**:
- .NET backend code (ZIP file)
- React frontend code (ZIP file)
- Migration documentation

**Key Methods**:
- `analyze(context, output_dir)`: Main migration method

### 2. Extractors

#### CodeExtractor

**Purpose**: Extract and parse code files from ZIP or directory

**Features**:
- Java AST parsing
- SQL file parsing
- Field extraction from DTO classes
- Method extraction
- Dependency filtering

**Key Methods**:
- `extract_from_zip(zip_path, file_mappings, dependency_file)`: Extract from ZIP
- `extract_from_directory(directory, file_mappings, dependency_file)`: Extract from directory
- `to_documents(code_files, form_name)`: Convert to vector store documents

**Document Types Created**:
- `class_definition`: DTO/model class with all fields
- `method_implementation`: Individual method implementations
- `comprehensive`: Complete file content

#### MinioExtractor

**Purpose**: Retrieve screenshots from MinIO object storage

**Key Methods**:
- `get_form_screenshots(form_name, bucket, prefix)`: Get screenshots for a form

#### JiraExtractor

**Purpose**: Fetch Jira issues and documentation

**Key Methods**:
- `get_form_issues(form_name, project_key, jql)`: Get Jira issues

#### PRDExtractor

**Purpose**: Extract content from existing PRD documents

**Key Methods**:
- `extract_from_directory(form_name, directory)`: Extract PRD documents

### 3. Vector Store (QdrantManager)

**Purpose**: Manage vector database operations

**Features**:
- Collection creation and management
- Embedding generation (OpenAI)
- Document storage with metadata
- Semantic search
- Metadata filtering

**Key Methods**:
- `create_collection(form_name, recreate)`: Create or recreate collection
- `add_documents(form_name, documents)`: Add documents to collection
- `search(form_name, query, limit, filter_metadata)`: Semantic search
- `get_collection_stats(form_name)`: Get collection statistics

**Metadata Tags**:
- `doc_type`: code, screenshot, jira, prd, analysis
- `chunk_type`: class_definition, method_implementation, comprehensive

### 4. Workflows

#### PRDGenerationWorkflow

**Purpose**: Temporal workflow orchestrating PRD generation

**Phases**: 8 phases with 12 activities

**Retry Policy**:
- Initial interval: 1 second
- Maximum interval: 5 minutes
- Maximum attempts: 3
- Backoff coefficient: 2.0

**Activity Timeouts**:
- Standard activities: 30 minutes
- LLM-heavy activities: 60 minutes

### 5. Utilities

#### BusinessLogicExtractor

**Purpose**: Extract business logic patterns from code

**Extraction Methods**:
- `extract_configuration_checks()`: Configuration flags
- `extract_validation_functions()`: Validation existence checks
- `extract_fleet_specific_logic()`: Fleet parameter usage
- `extract_alert_rate_management()`: Alert limit calculations
- `extract_field_dependencies()`: Field change dependencies
- `extract_state_transitions()`: Enabled/disabled, visible/invisible logic

#### FieldMappingExtractor

**Purpose**: Extract field mappings between legacy DTOs and normalized schema

**Key Methods**:
- `extract_dto_fields()`: Extract all fields from DTO class
- `map_to_normalized_schema()`: Map DTO fields to normalized columns
- `create_mapping_table()`: Generate markdown mapping table

#### MigrationGuideGenerator

**Purpose**: Generate step-by-step migration guides

**Key Methods**:
- `generate_migration_guide()`: Generate complete guide
- `format_migration_guide()`: Format as markdown

---

## Installation & Setup

### Prerequisites

- Python 3.11 or higher
- Docker & Docker Compose (for Qdrant, Temporal, MinIO)
- OpenAI API key
- (Optional) Jira API credentials
- (Optional) MinIO credentials

### Step 1: Clone Repository

```bash
git clone <repository-url>
cd PRD_Agent
```

### Step 2: Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Step 3: Install Dependencies

```bash
pip install -e .
# or
pip install -r requirements.txt
```

### Step 4: Configure Environment

```bash
cp env.example .env
```

Edit `.env` with your configuration:

```env
# OpenAI Configuration
OPENAI_API_KEY=your_openai_api_key_here
OPENAI_MODEL=gpt-4o
OPENAI_EMBEDDING_MODEL=text-embedding-3-large

# Qdrant Configuration
QDRANT_HOST=localhost
QDRANT_PORT=6333

# Temporal Configuration
TEMPORAL_HOST=localhost
TEMPORAL_PORT=7233
TEMPORAL_TASK_QUEUE=prd-agent-queue

# MinIO Configuration (Optional)
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin

# Jira Configuration (Optional)
JIRA_URL=https://your-jira-instance.atlassian.net
JIRA_USERNAME=your_email@example.com
JIRA_API_TOKEN=your_jira_api_token
```

### Step 5: Start Infrastructure Services

```bash
docker-compose up -d
```

This starts:
- **Qdrant**: Vector database (port 6333)
- **Temporal Server**: Workflow orchestration (port 7233)
- **Temporal UI**: Web interface (port 8080)
- **Temporal DB**: PostgreSQL for Temporal (port 5432)
- **MinIO**: Object storage (ports 9000, 9001)
- **n8n**: Workflow automation (port 5678)

Verify services are running:

```bash
docker-compose ps
```

### Step 6: Start Temporal Worker

In a separate terminal:

```bash
source venv/bin/activate
prd-worker
# or
python -m src.worker.temporal_worker
```

The worker must be running before triggering workflows.

### Step 7: Verify Installation

```bash
prd-agent version
```

---

## Usage Guide

### CLI Commands

#### Generate PRD

```bash
prd-agent generate \
  --form-name le07 \
  --zip-path src/templates_code_zip/oases-master.zip \
  --dependency-file src/form_dependencies/le07_dependencies.txt \
  --bucket screenshots \
  --jira-project OASES \
  --output ./output
```

**Options:**
- `--form-name, -f`: Name of the form to analyze (required)
- `--zip-path, -z`: Path to code ZIP file
- `--code-dir, -c`: Path to code directory (alternative to zip-path)
- `--mappings, -m`: Comma-separated file paths to include
- `--dependency-file, -d`: Path to dependency file with file paths
- `--bucket, -b`: MinIO bucket for screenshots
- `--jira-project, -j`: Jira project key
- `--output, -o`: Output directory (default: ./output)
- `--skip-screenshots`: Skip screenshot analysis
- `--skip-jira`: Skip Jira integration
- `--recreate-vectors`: Recreate vector collection
- `--use-workflow/--direct`: Use Temporal workflow or direct execution

#### List Collections

```bash
prd-agent list-collections
```

Lists all vector collections in Qdrant.

#### Search Knowledge Base

```bash
prd-agent search \
  --form-name le07 \
  --query "validation rules" \
  --limit 10 \
  --type code
```

**Options:**
- `--form-name, -f`: Form name to search in (required)
- `--query, -q`: Search query (required)
- `--limit, -l`: Maximum results (default: 5)
- `--type, -t`: Filter by doc type (code, screenshot, jira)

#### Get Collection Stats

```bash
prd-agent stats --form-name le07
```

#### Delete Collection

```bash
prd-agent delete-collection --form-name le07 --yes
```

#### Migrate Code

```bash
prd-agent migrate-code \
  --form-name le07 \
  --output ./output/migratedCode
```

Generates .NET backend and React frontend code from knowledge base.

### Programmatic Usage

```python
import asyncio
from src.main import generate_prd

async def main():
    result = await generate_prd(
        form_name="le07",
        zip_path="./oases-master.zip",
        dependency_file="./le07_dependencies.txt",
        minio_bucket="screenshots",
        jira_project="OASES",
        output_dir="./output",
    )

    if result["success"]:
        print(f"PRD generated: {result['prd_file']}")
        print(f"Word count: {result['word_count']}")
        print(f"Sections: {result['section_count']}")
    else:
        print(f"Error: {result['error']}")

asyncio.run(main())
```

### Using PRDGenerator Class

```python
from src.generators.prd_generator import PRDGenerator, PRDGenerationConfig

config = PRDGenerationConfig(
    form_name="le07",
    zip_path="./code.zip",
    dependency_file="./le07_dependencies.txt",
    minio_bucket="screenshots",
    jira_project_key="OASES",
    output_dir="./output",
)

generator = PRDGenerator()
result = await generator.generate(config)
```

### Direct Execution (Without Temporal)

For development and testing, you can run without Temporal:

```bash
prd-agent generate \
  --form-name le07 \
  --zip-path ./code.zip \
  --direct
```

---

## Configuration

### Environment Variables

| Variable                 | Description                    | Default                  | Required |
| ------------------------ | ------------------------------ | ------------------------ | -------- |
| `OPENAI_API_KEY`         | OpenAI API key                 | -                        | Yes      |
| `OPENAI_MODEL`           | Chat model                     | `gpt-4o`                 | No       |
| `OPENAI_EMBEDDING_MODEL` | Embedding model                 | `text-embedding-3-large` | No       |
| `OPENAI_MAX_TOKENS`      | Max tokens for completions     | `4096`                   | No       |
| `OPENAI_TEMPERATURE`     | Temperature for completions    | `0.1`                    | No       |
| `QDRANT_HOST`            | Qdrant host                     | `localhost`              | No       |
| `QDRANT_PORT`            | Qdrant port                     | `6333`                   | No       |
| `QDRANT_API_KEY`         | Qdrant API key                  | -                        | No       |
| `TEMPORAL_HOST`          | Temporal host                   | `localhost`              | No       |
| `TEMPORAL_PORT`          | Temporal port                   | `7233`                   | No       |
| `TEMPORAL_TASK_QUEUE`    | Task queue name                 | `prd-agent-queue`        | No       |
| `MINIO_ENDPOINT`         | MinIO endpoint                  | `localhost:9000`         | No       |
| `MINIO_ACCESS_KEY`       | MinIO access key                | `minioadmin`             | No       |
| `MINIO_SECRET_KEY`       | MinIO secret key                | `minioadmin`             | No       |
| `JIRA_URL`               | Jira instance URL               | -                        | No       |
| `JIRA_USERNAME`          | Jira username/email             | -                        | No       |
| `JIRA_API_TOKEN`         | Jira API token                  | -                        | No       |
| `LOG_LEVEL`               | Logging level                   | `INFO`                   | No       |
| `DEBUG`                   | Debug mode                      | `False`                  | No       |

### Settings File

Settings are managed through Pydantic Settings in `src/config/settings.py`. Configuration is loaded from:
1. Environment variables
2. `.env` file
3. Default values

### Dependency Files

Dependency files specify which code files to include in analysis. Format:

```
src/main/java/com/example/LE07Adapter.java
src/main/java/com/example/LE07Service.java
src/main/java/com/example/LE07DTO.java
```

One file path per line.

---

## Development Guide

### Project Structure

```
PRD_Agent/
├── src/
│   ├── agents/                 # Specialized AI agents
│   │   ├── base_agent.py
│   │   ├── screenshot_analysis_agent.py
│   │   ├── atlassian_integration_agent.py
│   │   ├── requirements_generator_agent.py
│   │   ├── user_flow_agent.py
│   │   ├── prd_aggregator_agent.py
│   │   └── code_migration_agent.py
│   ├── extractors/             # Data extraction modules
│   │   ├── code_extractor.py
│   │   ├── minio_extractor.py
│   │   ├── jira_extractor.py
│   │   └── prd_extractor.py
│   ├── workflows/              # Temporal workflows
│   │   ├── activities/
│   │   │   ├── extraction.py
│   │   │   ├── analysis.py
│   │   │   ├── aggregation.py
│   │   │   └── storage.py
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
│   ├── prompts/                # LLM prompts
│   │   ├── base.py
│   │   ├── screenshot_analysis.py
│   │   ├── atlassian.py
│   │   ├── requirements.py
│   │   ├── user_flow.py
│   │   ├── prd_aggregator.py
│   │   └── code_migration.py
│   └── utils/                  # Utilities
│       ├── file_utils.py
│       ├── logging_config.py
│       ├── business_logic_extractor.py
│       ├── field_mapping_extractor.py
│       ├── migration_guide_generator.py
│       └── code_migration_utils.py
├── tests/                      # Test suite
├── docker-compose.yml          # Infrastructure
├── requirements.txt            # Dependencies
├── pyproject.toml             # Project config
└── README.md                  # Quick start guide
```

### Adding a New Agent

1. Create agent class inheriting from `BaseAgent`:

```python
from src.agents.base_agent import BaseAgent, AgentContext, AgentResult

class MyNewAgent(BaseAgent):
    async def analyze(self, context: AgentContext, **kwargs) -> AgentResult:
        # Your analysis logic
        pass
```

2. Add prompt file in `src/prompts/`

3. Register activity in `src/workflows/activities/analysis.py`

4. Add to workflow in `src/workflows/prd_generation_workflow.py`

### Running Tests

```bash
# Run all tests
pytest

# Run with coverage
pytest --cov=src --cov-report=term-missing

# Run specific test
pytest tests/test_workflow.py -v
```

### Code Formatting

```bash
# Format code
black src tests

# Lint
ruff check src

# Type check
mypy src
```

### Development Dependencies

```bash
pip install -e ".[dev]"
```

---

## Troubleshooting

### Common Issues

#### Worker Not Picking Up Tasks

**Symptoms**: Workflow shows "Running" but no progress

**Solution**:
- Check task queue name matches between CLI and worker
- Verify worker is running: `ps aux | grep temporal_worker`
- Check Temporal server is running: `docker-compose ps`

#### Activity Timeout

**Symptoms**: Workflow fails with timeout error

**Solution**:
- Increase timeout in workflow (for long-running activities)
- Optimize the slow activity
- Check OpenAI API response times

#### Connection Refused

**Symptoms**: Worker fails to start

**Solution**:
- Ensure Temporal server is running: `docker-compose up -d temporal`
- Check Temporal address in `.env`: `TEMPORAL_HOST=localhost`
- Verify port 7233 is accessible

#### OpenAI Rate Limit

**Symptoms**: Activity retries repeatedly

**Solution**:
- Wait for rate limit to reset
- Upgrade OpenAI API tier
- Add delays between API calls

#### Missing Dependencies

**Symptoms**: Worker crashes on import

**Solution**:
- Run `pip install -e .` to install all dependencies
- Check Python version: `python --version` (must be 3.11+)
- Verify virtual environment is activated

#### Vector Collection Not Found

**Symptoms**: Search returns no results

**Solution**:
- Verify collection exists: `prd-agent list-collections`
- Check form name matches collection name
- Recreate collection: `--recreate-vectors` flag

### Debugging Workflow Failures

1. **Open Temporal UI** at `http://localhost:8080`
2. **Find your workflow** by ID or filter by status
3. **Click on the workflow** to see Event History
4. **Look for failed activities** (marked in red)
5. **Click on the activity** to see error message and stack trace

### Useful Commands

```bash
# Check Temporal server status
docker-compose ps

# View Temporal UI
open http://localhost:8080

# Check worker logs
python -m src.worker.temporal_worker 2>&1 | tee worker.log

# Check Qdrant status
curl http://localhost:6333/health

# Check MinIO status
curl http://localhost:9000/minio/health/live
```

### Logging

Logs are configured in `src/utils/logging_config.py`. Set log level:

```env
LOG_LEVEL=DEBUG
```

Logs include:
- Workflow execution progress
- Agent analysis steps
- Vector store operations
- API call details (in DEBUG mode)

---

## API Reference

### PRDGenerationInput

```python
@dataclass
class PRDGenerationInput:
    form_name: str                          # Required: e.g., "le07"
    zip_path: str | None                    # Path to code ZIP
    code_directory: str | None              # Or path to code directory
    file_mappings: list[str] | None         # Specific files to include
    dependency_file: str | None             # Filter file for dependencies
    minio_bucket: str | None                # Screenshot bucket
    minio_prefix: str | None                # Screenshot prefix
    jira_project_key: str | None             # Jira project
    jira_jql: str | None                   # Custom JQL query
    output_dir: str = "./output"            # Output directory
    recreate_vector_collection: bool = False # Force recreate collection
    skip_screenshots: bool = False           # Skip screenshot analysis
    skip_jira: bool = False                 # Skip Jira analysis
```

### PRDGenerationOutput

```python
@dataclass
class PRDGenerationOutput:
    form_name: str                          # Form that was processed
    success: bool                           # Overall success status
    prd_file_path: str | None               # Path to generated PRD
    vector_collection: str | None           # Qdrant collection name
    word_count: int                         # Words in PRD
    section_count: int                      # PRD sections
    execution_time_seconds: float           # Total execution time
    error: str | None                       # Error message if failed
    agent_results: dict[str, Any] | None    # Per-agent success status
```

### AgentContext

```python
@dataclass
class AgentContext:
    form_name: str                          # Form being analyzed
    vector_store: QdrantManager | None      # Vector store instance
    settings: Settings                      # Application settings
```

### AgentResult

```python
@dataclass
class AgentResult[T]:
    success: bool                           # Success status
    data: T | None                          # Result data
    error: str | None                       # Error message
    execution_time_ms: float                # Execution time
    metadata: dict[str, Any]                 # Additional metadata
```

---

## Best Practices

### 1. Dependency Files

Create dependency files to filter relevant code:

```
# le07_dependencies.txt
src/main/java/com/example/LE07Adapter.java
src/main/java/com/example/LE07Service.java
src/main/java/com/example/LE07DTO.java
```

This reduces noise and improves analysis accuracy.

### 2. Screenshot Organization

Organize screenshots in MinIO by form name:

```
screenshots/
  le07/
    main-panel.png
    chapter-dropdown.png
    ...
```

Use consistent naming for better analysis.

### 3. Jira Project Setup

Ensure Jira issues are properly tagged:
- Use consistent labels
- Include form name in issue title or description
- Add acceptance criteria

### 4. Vector Collection Management

- Use `--recreate-vectors` only when needed (recreates entire collection)
- Regularly check collection stats: `prd-agent stats -f <form_name>`
- Delete unused collections to save space

### 5. Workflow Execution

- Always start worker before triggering workflows
- Use Temporal UI to monitor progress
- Check logs for detailed error messages

### 6. Code Migration

- Generate PRD first before code migration
- Review PRD for completeness
- Use migration guide section for step-by-step approach

### 7. Testing

- Test with small codebases first
- Verify output quality before processing large projects
- Use `--direct` mode for faster iteration during development

### 8. Performance Optimization

- Use dependency files to reduce code volume
- Skip optional sources if not needed (`--skip-screenshots`, `--skip-jira`)
- Process multiple forms in parallel using multiple workers

---

## Additional Resources

### Documentation Files

- `README.md`: Quick start guide
- `ARCHITECTURE.md`: Detailed architecture documentation
- `ARCHITECTURE_FLOW.md`: Simplified agent orchestration flow
- `TEMPORAL_ORCHESTRATION_PAGE.md`: Temporal workflow details
- `IMPLEMENTATION_SUMMARY.md`: Implementation enhancements summary

### External Services

- **Temporal UI**: `http://localhost:8080` - Monitor workflow execution
- **MinIO Console**: `http://localhost:9001` - Manage screenshots
- **Qdrant Dashboard**: `http://localhost:6333/dashboard` - View vector collections

### Support

For issues or questions:
1. Check troubleshooting section
2. Review Temporal UI for workflow errors
3. Check logs for detailed error messages
4. Open a GitHub issue with:
   - Error message
   - Workflow ID (from Temporal UI)
   - Relevant logs

---

## Conclusion

PRD Agent is a comprehensive system for generating detailed PRDs from legacy codebases. It combines AI-powered analysis with reliable workflow orchestration to produce high-quality migration specifications.

Key strengths:
- **Reliability**: Temporal ensures workflows complete even with failures
- **Completeness**: Multi-source analysis captures all aspects of legacy systems
- **Accuracy**: Vector knowledge base enables precise code context retrieval
- **Extensibility**: Modular architecture allows easy addition of new agents

For more information, refer to the architecture documentation and implementation summary.

---

**Last Updated**: 2026-01-20  
**Version**: 1.0.0
