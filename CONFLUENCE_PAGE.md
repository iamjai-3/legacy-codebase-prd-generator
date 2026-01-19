# PRD Agent - AI-Powered Requirements Document Generator

---

## Overview

**PRD Agent** is an AI-powered system that automatically generates comprehensive **Product Requirements Documents (PRDs)** by fetching and analyzing **already documented legacy forms**. It collects source code, UI screenshots, and Jira documentation for each form, combines them into a **unified knowledge base**, and uses specialized AI agents to produce detailed migration specifications.

> 💡 **Key Value**: Creates a dedicated knowledge base for each legacy form by combining all available documentation, enabling AI-driven analysis and accurate migration to modern frameworks.

---

## The Knowledge Base Approach

PRD Agent follows a **"Collect → Combine → Analyze"** methodology:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        KNOWLEDGE BASE CREATION                              │
└─────────────────────────────────────────────────────────────────────────────┘

   STEP 1: FETCH                    STEP 2: COMBINE                STEP 3: USE
   Already Documented               Create Knowledge Base          For Migration
   Form Data                        Per Form

   ┌─────────────┐                  ┌─────────────────┐           ┌───────────┐
   │ Source Code │──────┐           │                 │           │  AI Agent │
   └─────────────┘      │           │   Vector Store  │           │  Analysis │
                        ├──────────►│   (Qdrant)      │──────────►│           │
   ┌─────────────┐      │           │                 │           │  PRD for  │
   │ Screenshots │──────┤           │  Collection:    │           │ Migration │
   └─────────────┘      │           │  prd_agent_le11 │           │           │
                        │           │                 │           └───────────┘
   ┌─────────────┐      │           └─────────────────┘
   │ Jira Docs   │──────┘
   └─────────────┘

   (Existing legacy form           (Unified, searchable           (Comprehensive PRD
    documentation)                  knowledge base)                ready for dev team)
```

Each legacy form (e.g., `le01`, `le07`, `le11`) gets its **own dedicated knowledge base**, making the migration process organized and traceable.

---

## Input Sources

The system fetches three types of **existing documentation** for each legacy form:

| Input Type      | Source                        | Description                                                                                     |
| --------------- | ----------------------------- | ----------------------------------------------------------------------------------------------- |
| **Code Files**  | ZIP archive + Dependency file | Existing Java source files, adapters, services, models—filtered by the form's dependency config |
| **Screenshots** | MinIO Object Storage          | Previously captured UI screenshots documenting the legacy form's interface                      |
| **Jira Issues** | Jira API                      | Historical requirements, user stories, acceptance criteria, and stakeholder feedback            |

> 📌 **Note**: All inputs are **pre-existing documentation** for the legacy forms. PRD Agent does not create new documentation—it intelligently combines and analyzes what already exists to generate migration-ready PRDs.

---

## Architecture Flow Diagram

The following diagram illustrates the complete data flow from input sources through AI agents to the final PRD output:

> 📎 **INSERT IMAGE: PRD_Agent_Arch.png**

---

## How Input Is Processed

### Step 1: Input Ingestion

When the user triggers PRD generation via CLI, the system receives:

```
prd-agent generate \
  --form-name le11 \
  --zip-path src/templates_code_zip/java.zip \
  --dependency-file src/form_dependencies/le11_dependencies.txt \
  --output ./output
```

The **dependency file** acts as a filter—only code files referenced in this file are extracted and processed, ensuring focused analysis on relevant components.

---

### Step 2: Data Extraction (Parallel Activities)

Three extractors run **in parallel** to gather all source data:

| Extractor          | Function                                                             | Output                                                |
| ------------------ | -------------------------------------------------------------------- | ----------------------------------------------------- |
| **CodeExtractor**  | Parses ZIP, filters by dependency file, extracts Java/SQL/Form files | `CodeFile[]` objects with content, path, and metadata |
| **MinioExtractor** | Connects to MinIO, retrieves form screenshots                        | `Screenshot[]` objects with image data and names      |
| **JiraExtractor**  | Queries Jira API for form-related issues                             | `JiraIssue[]` objects with requirements and context   |

---

### Step 3: Knowledge Base Creation (Per Form)

All extracted data is **combined** into a unified **vector knowledge base** for the form using OpenAI embeddings and **Qdrant**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   FORM KNOWLEDGE BASE (Vector Store)                        │
├─────────────────────────────────────────────────────────────────────────────┤
│                                                                             │
│  Collection: prd_agent_{form_name}   (e.g., prd_agent_le11)                │
│                                                                             │
│  ┌─────────────────┐  ┌─────────────────┐  ┌─────────────────┐             │
│  │   CODE CHUNKS   │  │   SCREENSHOTS   │  │   JIRA ISSUES   │             │
│  │                 │  │                 │  │                 │             │
│  │ • Adapters      │  │ • UI Layouts    │  │ • Requirements  │             │
│  │ • Services      │  │ • Form Fields   │  │ • User Stories  │             │
│  │ • Models        │  │ • Buttons       │  │ • Acceptance    │             │
│  │ • Validation    │  │ • Navigation    │  │   Criteria      │             │
│  │ • Business Logic│  │ • Error States  │  │ • Comments      │             │
│  └─────────────────┘  └─────────────────┘  └─────────────────┘             │
│                                                                             │
│  ✅ All data unified with vector embeddings                                │
│  ✅ Semantic search across code, UI, and requirements                      │
│  ✅ Each form has its own isolated knowledge base                          │
│  ✅ Persistent storage for future queries and migration reference          │
│                                                                             │
└─────────────────────────────────────────────────────────────────────────────┘
```

This **form-specific knowledge base** serves as the foundation for all AI agent analysis. Each form (le01, le07, le11, etc.) gets its own collection, ensuring clean separation and enabling targeted migration efforts.

---

## Orchestration Flow

The workflow is orchestrated by **Temporal**, providing reliable execution with automatic retries, timeout handling, and full observability.

> 📎 **INSERT IMAGE: Temporal Workflow Execution Screenshot**

### Workflow Execution Timeline

The Temporal UI shows the complete execution history with all activities and their durations:

---

## AI Agent Pipeline

The system employs **6 specialized AI agents**, each with a specific analysis responsibility:

### Layer 1: Initial Analysis (Parallel)

These agents run concurrently to maximize throughput:

| Agent                         | Input                      | Output                                                      | LLM Used     |
| ----------------------------- | -------------------------- | ----------------------------------------------------------- | ------------ |
| **Screenshot Analysis Agent** | UI screenshots             | UI elements, patterns, screen classifications, flow summary | GPT-4 Vision |
| **Jira Analysis Agent**       | Jira issues + code context | Requirements summary, business context                      | GPT-4        |

---

### Layer 2: Requirements Generation

The **Requirements Generator Agent** synthesizes outputs from Layer 1:

```
┌─────────────────────────────────────────────────────────────┐
│              Requirements Generator Agent                    │
├─────────────────────────────────────────────────────────────┤
│                                                             │
│  INPUTS:                                                    │
│  ├── Jira context (from Jira Analysis Agent)               │
│  ├── Screenshot context (from Screenshot Analysis Agent)   │
│  └── Code context (from Vector Store queries)              │
│                                                             │
│  OUTPUTS:                                                   │
│  ├── Functional Requirements (FR-XXX)                       │
│  ├── Non-Functional Requirements (NFR-XXX)                  │
│  ├── Data Model Requirements                                │
│  ├── Validation Rules                                       │
│  └── Business Rules                                         │
│                                                             │
└─────────────────────────────────────────────────────────────┘
```

---

### Layer 3: Secondary Analysis (Parallel)

With requirements complete, two more agents run in parallel:

| Agent                   | Receives                           | Produces                                                                    |
| ----------------------- | ---------------------------------- | --------------------------------------------------------------------------- |
| **User Flow Agent**     | Screenshot Analysis + Code Context | User flow diagrams (Mermaid), step-by-step flows, actor definitions         |
| **Risk Analysis Agent** | Requirements Result + Code Context | Technical risks, business risks, dependency analysis, mitigation strategies |

---

### Layer 4: Aggregation

The **PRD Aggregator Agent** combines all results into the final document:

```
                    ┌─────────────────────────────┐
                    │    PRD Aggregator Agent     │
                    └─────────────────────────────┘
                                 ▲
                                 │
        ┌────────────────────────┼────────────────────────┐
        │            │           │           │            │
┌───────────┐ ┌───────────┐ ┌────────┐ ┌──────────┐ ┌──────────┐
│Screenshot │ │   Jira    │ │Require-│ │User Flow │ │  Risk    │
│ Analysis  │ │ Analysis  │ │ ments  │ │  Result  │ │ Analysis │
│  Result   │ │  Result   │ │ Result │ │          │ │  Result  │
└───────────┘ └───────────┘ └────────┘ └──────────┘ └──────────┘
```

---

## Agent Communication Pattern

All AI agents leverage the **form's knowledge base** to retrieve relevant context. They communicate through **structured data passing** and **semantic queries** to the vector store:

```
┌─────────────────────────────────────────────────────────────────┐
│                   Knowledge Base Query Pattern                   │
└─────────────────────────────────────────────────────────────────┘

     Agent needs context about "validation logic"
                        │
                        ▼
          ┌──────────────────────────┐
          │   Query Form's           │
          │   Knowledge Base         │
          │   (prd_agent_le11)       │
          └────────────┬─────────────┘
                       │
                       ▼
          ┌──────────────────────────┐
          │  Semantic Search Returns │
          │  • Relevant code chunks  │
          │  • Related screenshots   │
          │  • Matching Jira issues  │
          └────────────┬─────────────┘
                       │
                       ▼
          ┌──────────────────────────┐
          │   Include in LLM Prompt  │
          │   for Contextual Analysis│
          └──────────────────────────┘
```

This pattern ensures:

- ✅ Agents query the **unified knowledge base** (code + UI + requirements combined)
- ✅ Semantically relevant information from all sources
- ✅ Scales to large codebases without passing full files
- ✅ Context maintained across agent executions
- ✅ Same knowledge base available for developer queries during migration

---

## Output Generation

### Final PRD Structure

The generated PRD document includes:

1. **Executive Summary** - High-level overview and key findings
2. **User Interface Analysis** - Screen types, UI patterns, component hierarchy
3. **Functional Requirements** - Detailed FR specifications with acceptance criteria
4. **Non-Functional Requirements** - Performance, security, scalability requirements
5. **Data Model** - Entities, fields, relationships, and data types
6. **User Flows** - Step-by-step journeys with Mermaid diagrams
7. **Business Rules** - Validation logic and business constraints
8. **Risk Assessment** - Technical/business risks with mitigation strategies
9. **Migration Recommendations** - Suggested approach and priorities

### Output Files

```
output/
├── le11_PRD.md           # Complete PRD document (Markdown)
└── le11_PRD_metadata.json # Execution metrics and statistics
```

---

## How the Knowledge Base Enables Migration

The created knowledge base serves multiple purposes beyond PRD generation:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                   KNOWLEDGE BASE USAGE FOR MIGRATION                        │
└─────────────────────────────────────────────────────────────────────────────┘

   ┌─────────────────────────────────────────────────────────────────────────┐
   │                    prd_agent_{form_name}                                │
   │                    (Persistent Vector Store)                            │
   └───────────────────────────────┬─────────────────────────────────────────┘
                                   │
           ┌───────────────────────┼───────────────────────┐
           │                       │                       │
           ▼                       ▼                       ▼
   ┌───────────────┐       ┌───────────────┐       ┌───────────────┐
   │  PRD          │       │  Developer    │       │  Future       │
   │  Generation   │       │  Queries      │       │  Analysis     │
   │               │       │               │       │               │
   │  • Initial    │       │  • "How does  │       │  • Code       │
   │    analysis   │       │    validation │       │    migration  │
   │  • Requirements│      │    work?"     │       │    assistance │
   │  • Risk       │       │  • "Show me   │       │  • Impact     │
   │    assessment │       │    related    │       │    analysis   │
   │               │       │    code"      │       │               │
   └───────────────┘       └───────────────┘       └───────────────┘
```

**The knowledge base is persistent**, meaning:

- ✅ Developers can query it directly using `prd-agent search` commands
- ✅ Multiple PRD regenerations use the same knowledge base (unless recreated)
- ✅ Enables context-aware answers about the legacy form during migration
- ✅ Serves as a reference point throughout the entire migration lifecycle

---

## Execution Metrics

The workflow tracks comprehensive metrics:

| Metric                   | Description                    |
| ------------------------ | ------------------------------ |
| `execution_time_seconds` | Total workflow duration        |
| `word_count`             | Words in generated PRD         |
| `section_count`          | Number of PRD sections         |
| `vector_collection`      | Qdrant collection name         |
| `agent_results`          | Success/failure for each agent |

**Example Output Metadata:**

```json
{
  "success": true,
  "form_name": "le11",
  "execution_time_seconds": 20.19,
  "word_count": 6261,
  "section_count": 9,
  "vector_collection": "prd_agent_le11",
  "agent_results": {
    "requirements_analysis": true,
    "risk_analysis": true,
    "screenshot_analysis": true,
    "user_flow_analysis": true
  }
}
```

---

## Technology Stack

| Component          | Technology                    | Purpose                                    |
| ------------------ | ----------------------------- | ------------------------------------------ |
| **Orchestration**  | Temporal                      | Workflow execution, retries, observability |
| **Vector Store**   | Qdrant                        | Semantic search, embeddings storage        |
| **LLM**            | OpenAI GPT-4 / GPT-4 Vision   | AI analysis and generation                 |
| **Embeddings**     | OpenAI text-embedding-3-large | Vector embeddings                          |
| **Object Storage** | MinIO                         | Screenshot storage                         |
| **Issue Tracking** | Jira API                      | Requirements extraction                    |
| **CLI**            | Typer                         | Command-line interface                     |
| **Runtime**        | Python 3.11+                  | Application runtime                        |

---

## Resilience & Reliability

The system includes robust error handling:

### Temporal Retry Policy

- **Initial Interval**: 1 second
- **Maximum Interval**: 5 minutes
- **Maximum Attempts**: 3
- **Backoff Coefficient**: 2.0

### Activity Timeouts

- Standard activities: 30 minutes
- LLM-heavy activities: 60 minutes

### Graceful Degradation

- Agents return partial results on failure
- Workflow continues even if optional inputs (screenshots, Jira) are unavailable

---

## Summary

PRD Agent transforms the migration preparation process by **fetching existing form documentation**, **combining it into a unified knowledge base**, and **generating AI-analyzed PRDs**:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         PRD AGENT WORKFLOW                                  │
└─────────────────────────────────────────────────────────────────────────────┘

   ┌──────────────────────────────────────┐
   │   EXISTING FORM DOCUMENTATION        │
   │                                      │
   │   • Source Code (Java, SQL, Forms)   │
   │   • UI Screenshots (MinIO)           │
   │   • Jira Issues & Requirements       │
   └──────────────────┬───────────────────┘
                      │
                      ▼
   ┌──────────────────────────────────────┐
   │   KNOWLEDGE BASE CREATION            │
   │                                      │
   │   Combine all inputs into a          │
   │   searchable vector store            │
   │   per form (prd_agent_le11)          │
   └──────────────────┬───────────────────┘
                      │
                      ▼
   ┌──────────────────────────────────────┐
   │   AI AGENT ANALYSIS                  │
   │                                      │
   │   6 specialized agents analyze       │
   │   the knowledge base (~5 min)        │
   └──────────────────┬───────────────────┘
                      │
                      ▼
   ┌──────────────────────────────────────┐
   │   PRD OUTPUT FOR MIGRATION           │
   │                                      │
   │   Comprehensive requirements doc     │
   │   ready for development team         │
   └──────────────────────────────────────┘
```

**Benefits:**

- 🗄️ **Unified Knowledge Base**: All form documentation combined into one searchable store
- 🚀 **Speed**: Generates comprehensive PRDs in minutes, not days
- 🎯 **Accuracy**: AI analysis catches patterns humans might miss
- 📊 **Consistency**: Standardized PRD format across all forms
- 🔄 **Scalability**: Process multiple forms in parallel with Temporal workers
- 📈 **Observability**: Full workflow history and metrics in Temporal UI
- 🔍 **Reusable**: Knowledge base persists for future queries and migration reference

---

_For technical details and contribution guidelines, see the project README and ARCHITECTURE documentation._
