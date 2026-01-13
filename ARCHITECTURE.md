# PRD Agent - High-Level Architecture

## Overview

PRD Agent is an AI-powered system that generates comprehensive Product Requirements Documents (PRDs) from legacy codebases. It uses specialized AI agents orchestrated through Temporal workflows to analyze code, UI screenshots, and Jira documentation, creating a vector knowledge base and producing detailed migration specifications.

## System Architecture

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
└───────┬───────┘      │ - User Flow    │      └───────┬───────┘
        │              │ - Risk         │              │
        └──────────────┼────────────────┘              │
                       │                               │
                       ▼                               ▼
              ┌─────────────────┐            ┌─────────────────┐
              │  Vector Store   │            │  Output Files   │
              │  (Qdrant)       │            │  (Markdown)     │
              └─────────────────┘            └─────────────────┘
```

## Workflow Orchestration Flow

### Phase-by-Phase Execution

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PRD Generation Workflow Phases                       │
└─────────────────────────────────────────────────────────────────────────┘

Phase 1: Data Extraction (Parallel)
├── Code Extraction Activity
│   └── CodeExtractor
│       ├── Extract from ZIP/Directory
│       ├── Parse Java/SQL/Form files
│       └── Filter by dependency file
│
├── Screenshot Extraction Activity (if not skipped)
│   └── MinioExtractor
│       ├── List screenshots from Minio bucket
│       └── Download image data
│
└── Jira Extraction Activity (if not skipped)
    └── JiraExtractor
        ├── Query Jira API
        └── Fetch issues and documentation

Phase 2: Vector Storage
└── Store Vectors Activity
    └── QdrantManager
        ├── Create/Recreate collection
        ├── Generate embeddings (OpenAI)
        └── Store code, screenshots, Jira as vectors

Phase 3: Initial Analysis (Parallel)
├── Screenshot Analysis Activity (if not skipped)
│   └── ScreenshotAnalysisAgent
│       ├── Analyze UI screenshots with GPT-4 Vision
│       ├── Extract UI elements and patterns
│       └── Generate UI flow summary
│
└── Jira Analysis Activity (if not skipped)
    └── AtlassianIntegrationAgent
        ├── Analyze Jira issues
        └── Extract requirements and context

Phase 4: Requirements Generation
└── Generate Requirements Activity
    └── RequirementsGeneratorAgent
        ├── Query vector store for code context
        ├── Generate functional requirements
        ├── Generate non-functional requirements
        ├── Generate data requirements
        └── Extract validation rules and business rules

Phase 5: Flow & Risk Analysis (Parallel)
├── User Flow Analysis Activity
│   └── UserFlowAgent
│       ├── Analyze screenshot analysis results
│       ├── Query code context from vector store
│       └── Generate user flow diagrams and steps
│
└── Risk Analysis Activity
    └── RiskAnalysisAgent
        ├── Analyze requirements
        ├── Query vector store for code context
        └── Identify technical and business risks

Phase 6: Store Analysis Results
└── Store Analysis Results Activity
    └── QdrantManager
        └── Store all analysis results as vectors

Phase 7: PRD Aggregation
└── Aggregate PRD Activity
    └── PRDAggregatorAgent
        ├── Combine all analysis results
        ├── Generate comprehensive PRD structure
        ├── Format sections and content
        └── Calculate metrics

Phase 8: Save PRD
└── Save PRD Activity
    └── File Writer
        ├── Write Markdown file
        └── Write metadata JSON
```

## Agent Architecture

### Base Agent Pattern

All agents inherit from `BaseAgent` which provides:

```
┌─────────────────────────────────────────────────────────────┐
│                      BaseAgent                              │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  Core Capabilities:                                         │
│  ├── LLM Integration (OpenAI ChatOpenAI)                   │
│  ├── Vector Store Access (QdrantManager)                   │
│  ├── Context Retrieval (semantic search)                    │
│  ├── JSON Response Parsing                                  │
│  ├── Retry Logic with exponential backoff                   │
│  ├── Execution Timing                                       │
│  └── Structured Logging                                     │
│                                                             │
│  Abstract Method:                                           │
│  └── analyze(context, **kwargs) -> AgentResult[T]          │
│                                                             │
└─────────────────────────────────────────────────────────────┘
                              │
        ┌─────────────────────┼─────────────────────┐
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Screenshot    │   │ Requirements  │   │ User Flow     │
│ Analysis      │   │ Generator     │   │ Agent         │
│ Agent         │   │ Agent         │   │               │
└───────────────┘   └───────────────┘   └───────────────┘
        │                     │                     │
        ▼                     ▼                     ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Atlassian     │   │ Risk Analysis │   │ PRD           │
│ Integration   │   │ Agent         │   │ Aggregator    │
│ Agent         │   │               │   │ Agent         │
└───────────────┘   └───────────────┘   └───────────────┘
```

### Agent Responsibilities

#### 1. ScreenshotAnalysisAgent

- **Purpose**: Analyze UI screenshots to understand user interface patterns
- **Input**: Screenshot images from Minio
- **LLM**: GPT-4 Vision (gpt-4o)
- **Output**:
  - UI element analysis
  - Screen type classification
  - Layout descriptions
  - User action identification
  - Validation rules extraction
  - UI flow summary

#### 2. AtlassianIntegrationAgent

- **Purpose**: Extract and analyze requirements from Jira
- **Input**: Jira issues and documentation
- **LLM**: GPT-4
- **Output**:
  - Requirements summary
  - Issue categorization
  - Business context extraction

#### 3. RequirementsGeneratorAgent

- **Purpose**: Generate comprehensive functional and non-functional requirements
- **Input**: Code files, Jira context, Screenshot context
- **LLM**: GPT-4
- **Vector Store**: Queries code context
- **Output**:
  - Functional requirements with acceptance criteria
  - Non-functional requirements
  - Data model requirements
  - Integration requirements
  - Validation rules
  - Business rules

#### 4. UserFlowAgent

- **Purpose**: Generate user flow diagrams and step-by-step flows
- **Input**: Screenshot analysis, Code context
- **LLM**: GPT-4
- **Vector Store**: Queries code context
- **Output**:
  - User flow diagrams (Mermaid format)
  - Step-by-step user flows
  - Actor definitions
  - Success criteria

#### 5. RiskAnalysisAgent

- **Purpose**: Identify technical and business risks
- **Input**: Requirements analysis, Code context
- **LLM**: GPT-4
- **Vector Store**: Queries code context
- **Output**:
  - Technical risks
  - Business risks
  - Migration risks
  - Mitigation strategies
  - Risk categorization

#### 6. PRDAggregatorAgent

- **Purpose**: Combine all analysis results into a comprehensive PRD
- **Input**: All previous agent results
- **LLM**: GPT-4
- **Output**:
  - Structured PRD document
  - Executive summary
  - All sections formatted
  - Metrics and statistics

## Data Flow

```
┌─────────────────────────────────────────────────────────────────────┐
│                         Data Flow Diagram                           │
└─────────────────────────────────────────────────────────────────────┘

Input Sources:
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Code ZIP     │  │ Screenshots  │  │ Jira Issues  │
│ + Dependencies│  │ (Minio)      │  │              │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Extraction Layer    │
              │  (Activities)        │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Structured Data     │
              │  - CodeFile objects   │
              │  - Screenshot objects│
              │  - JiraIssue objects  │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Vector Store        │
              │  (Qdrant)            │
              │  - Embeddings        │
              │  - Metadata          │
              │  - Searchable        │
              └──────────┬───────────┘
                         │
                         │ (Semantic Search)
                         │
        ┌────────────────┼────────────────┐
        │                │                │
        ▼                ▼                ▼
┌──────────────┐  ┌──────────────┐  ┌──────────────┐
│ Agent 1      │  │ Agent 2      │  │ Agent 3      │
│ (Context)    │  │ (Context)    │  │ (Context)    │
└──────┬───────┘  └──────┬───────┘  └──────┬───────┘
       │                 │                 │
       └─────────────────┼─────────────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  Agent Results       │
              │  (Structured Data)   │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  PRD Aggregator      │
              │  (Final Assembly)    │
              └──────────┬───────────┘
                         │
                         ▼
              ┌──────────────────────┐
              │  PRD Document        │
              │  (Markdown + JSON)   │
              └──────────────────────┘
```

## Technology Stack

### Core Technologies

- **Python 3.11+**: Primary language
- **Temporal**: Workflow orchestration
- **Qdrant**: Vector database for embeddings
- **OpenAI API**: LLM and embeddings
- **LangChain**: LLM integration framework

### Key Libraries

- **typer**: CLI interface
- **pydantic**: Settings management
- **dataclasses**: Data structures
- **asyncio**: Async operations
- **Pillow**: Image processing
- **minio**: Object storage client
- **jira**: Jira API client

### External Services

- **Temporal Server**: Workflow execution
- **Qdrant Server**: Vector storage
- **OpenAI API**: LLM and embeddings
- **Minio**: Screenshot storage
- **Jira**: Issue tracking

## Component Details

### 1. CLI Layer (`src/cli/commands.py`)

- Entry point for user interactions
- Parses command-line arguments
- Routes to workflow or direct execution
- Provides progress feedback

### 2. Workflow Layer (`src/workflows/`)

- **PRDGenerationWorkflow**: Main orchestrator
- **Activities**: Individual work units
  - `extraction.py`: Data extraction activities
  - `analysis.py`: Agent execution activities
  - `aggregation.py`: PRD assembly activity
  - `storage.py`: Vector storage activities

### 3. Agent Layer (`src/agents/`)

- **BaseAgent**: Common functionality
- **Specialized Agents**: Task-specific analysis
- All agents use:
  - Vector store for context retrieval
  - LLM for analysis
  - Structured output parsing

### 4. Extractor Layer (`src/extractors/`)

- **CodeExtractor**: Parses code files
- **MinioExtractor**: Retrieves screenshots
- **JiraExtractor**: Fetches Jira data

### 5. Vector Store (`src/vector_store/`)

- **QdrantManager**: Manages collections and vectors
- **Embeddings**: OpenAI text-embedding-3-small
- Stores: Code, screenshots, Jira, analysis results

### 6. Utilities (`src/utils/`)

- **Serialization**: Dataclass conversion
- **Dependency Parser**: File filtering
- **Data Reconstruction**: Restore objects from dicts
- **Logging**: Structured logging with timing

## Execution Modes

### 1. Temporal Workflow Mode (Default)

- **Advantages**:
  - Reliable execution with retries
  - Scalable worker pool
  - Workflow history and observability
  - Fault tolerance
- **Use Case**: Production environments

### 2. Direct Execution Mode

- **Advantages**:
  - Simpler for development
  - No Temporal dependency
  - Faster for small tests
- **Use Case**: Development and testing

## Agent Communication Pattern

```
┌─────────────────────────────────────────────────────────────┐
│              Agent Communication Flow                       │
└─────────────────────────────────────────────────────────────┘

Workflow Orchestrator
        │
        ├───► ScreenshotAnalysisAgent
        │     │
        │     ├───► Vector Store (query code context)
        │     ├───► LLM (GPT-4 Vision)
        │     └───► Returns: ScreenshotAnalysisResult
        │
        ├───► AtlassianIntegrationAgent
        │     │
        │     ├───► Vector Store (query code context)
        │     ├───► LLM (GPT-4)
        │     └───► Returns: AtlassianAnalysisResult
        │
        ├───► RequirementsGeneratorAgent
        │     │
        │     ├───► Vector Store (query code context)
        │     ├───► Receives: Jira context, Screenshot context
        │     ├───► LLM (GPT-4)
        │     └───► Returns: RequirementsResult
        │
        ├───► UserFlowAgent
        │     │
        │     ├───► Vector Store (query code context)
        │     ├───► Receives: ScreenshotAnalysisResult
        │     ├───► LLM (GPT-4)
        │     └───► Returns: UserFlowResult
        │
        ├───► RiskAnalysisAgent
        │     │
        │     ├───► Vector Store (query code context)
        │     ├───► Receives: RequirementsResult
        │     ├───► LLM (GPT-4)
        │     └───► Returns: RiskAnalysisResult
        │
        └───► PRDAggregatorAgent
              │
              ├───► Receives: All previous results
              ├───► LLM (GPT-4)
              └───► Returns: PRDContent
```

## Error Handling & Resilience

### Retry Strategy

- **Workflow Level**: Temporal retry policy
  - Initial interval: 1 second
  - Maximum interval: 5 minutes
  - Maximum attempts: 3
  - Backoff coefficient: 2.0

### Agent Level

- **LLM Calls**: Automatic retries with exponential backoff
- **Vector Store**: Connection retries
- **Graceful Degradation**: Agents return empty results on failure

### Activity Timeouts

- **Short Activities**: 30 minutes
- **Long Activities** (LLM-heavy): 60 minutes

## Scalability Considerations

### Horizontal Scaling

- **Temporal Workers**: Can scale to multiple workers
- **Qdrant**: Can be clustered
- **Activities**: Stateless, can run on any worker

### Performance Optimization

- **Parallel Execution**: Multiple agents run in parallel
- **Vector Store Caching**: Context retrieval is cached
- **Batch Processing**: Multiple files processed together

## Security & Configuration

### Configuration Management

- **Settings**: Pydantic-based settings from environment
- **Secrets**: Environment variables for API keys
- **Validation**: Type checking and validation

### Data Privacy

- **Local Processing**: Code processed locally
- **API Keys**: Stored securely in environment
- **Vector Store**: Can be self-hosted

## Future Enhancements

1. **Multi-Form Analysis**: Process multiple forms in parallel
2. **Incremental Updates**: Update PRDs as code changes
3. **Custom Agents**: Plugin system for custom analysis
4. **Web UI**: Browser-based interface
5. **Real-time Updates**: WebSocket progress updates
6. **Export Formats**: PDF, Word, Confluence export

## Conclusion

PRD Agent uses a modular, agent-based architecture orchestrated through Temporal workflows. Each agent specializes in a specific analysis task, and they communicate through shared vector stores and structured data passing. This design enables:

- **Reliability**: Temporal ensures workflow completion
- **Scalability**: Stateless agents can scale horizontally
- **Maintainability**: Clear separation of concerns
- **Extensibility**: Easy to add new agents or analysis types

The system transforms legacy codebases into comprehensive PRDs that guide modern migration efforts, combining AI analysis with structured workflow orchestration.
