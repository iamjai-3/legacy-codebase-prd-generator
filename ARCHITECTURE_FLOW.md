# PRD Agent - Simplified Agent Orchestration Flow

## Quick Reference: Agent Execution Flow

```
┌─────────────────────────────────────────────────────────────────────────┐
│                    PRD Generation - Agent Orchestration                  │
└─────────────────────────────────────────────────────────────────────────┘

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
└─► [Activity] extract_jira_activity (if not skipped)
    └─► JiraExtractor.get_form_issues()
        └─► Return: JiraIssue[] objects
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
        └─► Store Jira as vectors
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
│       ├─► Identify common patterns
│       └─► Return: ScreenshotAnalysisResult
│
└─► [Activity] analyze_jira_activity (if not skipped)
    └─► AtlassianIntegrationAgent.analyze()
        ├─► Query vector store for code context
        ├─► Analyze Jira issues with GPT-4
        ├─► Extract requirements context
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
        ├─► Extract business rules
        └─► Return: RequirementsResult
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 5: FLOW & RISK ANALYSIS (Parallel Agents)                     │
└─────────────────────────────────────────────────────────────────────┘
│
├─► [Activity] analyze_user_flows_activity
│   └─► UserFlowAgent.analyze()
│       ├─► Query vector store for code context
│       ├─► Receive: ScreenshotAnalysisResult
│       ├─► Generate user flow diagrams (Mermaid)
│       ├─► Create step-by-step flows
│       └─► Return: UserFlowResult
│
└─► [Activity] analyze_risks_activity
    └─► RiskAnalysisAgent.analyze()
        ├─► Query vector store for code context
        ├─► Receive: RequirementsResult
        ├─► Identify technical risks
        ├─► Identify business risks
        ├─► Generate mitigation strategies
        └─► Return: RiskAnalysisResult
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 6: STORE ANALYSIS RESULTS                                     │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] store_analysis_results_activity
    └─► QdrantManager
        ├─► Store screenshot analysis as vectors
        ├─► Store requirements as vectors
        ├─► Store user flows as vectors
        └─► Store risk analysis as vectors
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 7: PRD AGGREGATION                                            │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] aggregate_prd_activity
    └─► PRDAggregatorAgent.analyze()
        ├─► Receive: All previous agent results
        │   ├─► ScreenshotAnalysisResult
        │   ├─► AtlassianAnalysisResult
        │   ├─► RequirementsResult
        │   ├─► UserFlowResult
        │   └─► RiskAnalysisResult
        ├─► Generate PRD structure (GPT-4)
        ├─► Format all sections
        ├─► Create executive summary
        ├─► Calculate metrics
        └─► Return: PRDContent (Markdown)
│
┌─────────────────────────────────────────────────────────────────────┐
│ PHASE 8: SAVE PRD                                                   │
└─────────────────────────────────────────────────────────────────────┘
│
└─► [Activity] save_prd_activity
    ├─► Write PRD markdown file
    └─► Write metadata JSON file
│
END: Return PRDGenerationOutput
```

## Agent Dependencies Graph

```
                    ┌─────────────────────┐
                    │  Code Extraction    │
                    └──────────┬──────────┘
                               │
                               ▼
                    ┌─────────────────────┐
                    │  Vector Store       │
                    │  (Qdrant)           │
                    └──────────┬──────────┘
                               │
        ┌──────────────────────┼──────────────────────┐
        │                      │                      │
        ▼                      ▼                      ▼
┌───────────────┐    ┌───────────────┐    ┌───────────────┐
│ Screenshot    │    │ Jira          │    │ Requirements  │
│ Analysis      │    │ Analysis      │    │ Generator     │
│ Agent         │    │ Agent         │    │ Agent         │
└───────┬───────┘    └───────┬───────┘    └───────┬───────┘
        │                    │                    │
        │                    └──────────┬─────────┘
        │                               │
        │                               ▼
        │                    ┌─────────────────────┐
        │                    │ Requirements Result │
        │                    └──────────┬──────────┘
        │                               │
        └───────────────┬───────────────┘
                        │
        ┌───────────────┼───────────────┐
        │               │               │
        ▼               ▼               ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ User Flow     │ │ Risk Analysis │ │ PRD           │
│ Agent         │ │ Agent         │ │ Aggregator    │
│               │ │               │ │ Agent         │
└───────┬───────┘ └───────┬───────┘ └───────┬───────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
                 ┌─────────────────────┐
                 │  Final PRD          │
                 │  Document           │
                 └─────────────────────┘
```

## Data Flow Between Agents

```
Input Data Sources
    │
    ├─► Code Files ──────────┐
    ├─► Screenshots ─────────┤
    └─► Jira Issues ─────────┤
                              │
                              ▼
                    ┌─────────────────┐
                    │  Vector Store   │
                    │  (Context DB)   │
                    └────────┬────────┘
                             │
        ┌────────────────────┼────────────────────┐
        │                    │                    │
        ▼                    ▼                    ▼
┌───────────────┐   ┌───────────────┐   ┌───────────────┐
│ Screenshot    │   │ Jira          │   │ Requirements  │
│ Analysis      │   │ Analysis      │   │ Generator     │
│               │   │               │   │               │
│ Output:       │   │ Output:       │   │ Output:       │
│ - UI Elements │   │ - Requirements│   │ - Functional  │
│ - Patterns    │   │ - Context     │   │   Requirements│
│ - Flow Summary│   │               │   │ - Data Models │
└───────┬───────┘   └───────┬───────┘   └───────┬───────┘
        │                   │                   │
        │                   └─────────┬─────────┘
        │                             │
        │                             ▼
        │                   ┌─────────────────┐
        │                   │ Requirements    │
        │                   │ Result          │
        │                   └────────┬────────┘
        │                            │
        └────────────┬───────────────┘
                     │
        ┌────────────┼────────────┐
        │            │            │
        ▼            ▼            ▼
┌───────────────┐ ┌───────────────┐ ┌───────────────┐
│ User Flow     │ │ Risk Analysis │ │ PRD           │
│ Agent         │ │ Agent         │ │ Aggregator    │
│               │ │               │ │               │
│ Uses:         │ │ Uses:         │ │ Uses:        │
│ - Screenshot  │ │ - Requirements│ │ - All Results│
│   Analysis    │ │   Result      │ │               │
│               │ │               │ │               │
│ Output:       │ │ Output:       │ │ Output:       │
│ - Flow Diagrams│ │ - Risks      │ │ - Complete PRD│
│ - Steps       │ │ - Mitigations │ │ - Metrics     │
└───────┬───────┘ └───────┬───────┘ └───────┬───────┘
        │                 │                 │
        └─────────────────┼─────────────────┘
                          │
                          ▼
                 ┌─────────────────┐
                 │  Final PRD      │
                 │  (Markdown)     │
                 └─────────────────┘
```

## Key Agent Interactions

### 1. ScreenshotAnalysisAgent → UserFlowAgent

- **Data Passed**: ScreenshotAnalysisResult
- **Purpose**: UserFlowAgent uses UI analysis to create flow diagrams

### 2. AtlassianIntegrationAgent → RequirementsGeneratorAgent

- **Data Passed**: Jira context summary
- **Purpose**: RequirementsGeneratorAgent incorporates Jira requirements

### 3. ScreenshotAnalysisAgent → RequirementsGeneratorAgent

- **Data Passed**: UI flow summary
- **Purpose**: RequirementsGeneratorAgent understands UI requirements

### 4. RequirementsGeneratorAgent → RiskAnalysisAgent

- **Data Passed**: RequirementsResult
- **Purpose**: RiskAnalysisAgent identifies risks in requirements

### 5. All Agents → PRDAggregatorAgent

- **Data Passed**: All analysis results
- **Purpose**: PRDAggregatorAgent combines everything into final PRD

## Vector Store Usage Pattern

All agents query the vector store for relevant code context:

```
Agent needs context about "validation logic"
    │
    ▼
Query Vector Store
    │
    ├─► Search: "validation", "required", "pattern"
    │
    ├─► Retrieve: Top 5 relevant code snippets
    │
    └─► Use in LLM prompt
```

This pattern allows agents to:

- Access code context without passing large files
- Get semantically relevant information
- Scale to large codebases
- Maintain context across agent executions
