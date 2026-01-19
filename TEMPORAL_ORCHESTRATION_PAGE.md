# PRD Agent - Temporal Workflow Orchestration

---

## What is Temporal?

**Temporal** is a durable execution platform that ensures our PRD generation workflows run reliably to completion—even in the face of failures, timeouts, or infrastructure issues.

> 💡 **Why Temporal?** PRD generation involves multiple AI agents, external API calls (OpenAI, Jira, MinIO), and long-running LLM operations. Temporal guarantees that if any step fails, it will be retried automatically without losing progress.

### The Problem Temporal Solves

Without Temporal, a typical PRD generation process might look like this:

- ❌ If the OpenAI API times out during screenshot analysis, the entire process fails
- ❌ If the server restarts mid-workflow, all progress is lost
- ❌ Tracking which steps completed successfully requires custom state management
- ❌ Retrying failed operations requires manual intervention

**With Temporal**, all of these concerns are handled automatically:

- ✅ **Durable State**: If the worker crashes, another worker picks up exactly where it left off
- ✅ **Automatic Retries**: Transient failures (network issues, API rate limits) are retried with exponential backoff
- ✅ **Full History**: Every activity execution is logged with inputs, outputs, and timing
- ✅ **Visibility**: The Temporal UI shows real-time progress and allows debugging failed workflows

---

## Architecture Overview

The orchestration layer sits between the CLI/API and the actual processing logic, managing the execution flow:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                       TEMPORAL ORCHESTRATION LAYER                          │
└─────────────────────────────────────────────────────────────────────────────┘

                              ┌─────────────────┐
                              │  Temporal       │
                              │  Server         │
                              │  (localhost:7233)│
                              └────────┬────────┘
                                       │
                    ┌──────────────────┼──────────────────┐
                    │                  │                  │
                    ▼                  ▼                  ▼
           ┌───────────────┐  ┌───────────────┐  ┌───────────────┐
           │   Temporal    │  │   Temporal    │  │   Temporal    │
           │   Worker 1    │  │   Worker 2    │  │   Worker N    │
           │               │  │               │  │               │
           │  Task Queue:  │  │  Task Queue:  │  │  Task Queue:  │
           │  prd-agent-   │  │  prd-agent-   │  │  prd-agent-   │
           │  queue        │  │  queue        │  │  queue        │
           └───────────────┘  └───────────────┘  └───────────────┘
                    │                  │                  │
                    └──────────────────┼──────────────────┘
                                       │
                              ┌────────▼────────┐
                              │ PRDGeneration   │
                              │ Workflow        │
                              │                 │
                              │ ┌─────────────┐ │
                              │ │ Activities  │ │
                              │ │ (12 total)  │ │
                              │ └─────────────┘ │
                              └─────────────────┘
```

---

## Core Components

Understanding the three main components is essential to grasping how PRD Agent orchestration works.

### 1. Temporal Server

The **Temporal Server** is the brain of the orchestration system. It's responsible for:

- **Persisting workflow state** in a database (PostgreSQL)
- **Scheduling activities** to be executed by workers
- **Managing retries** when activities fail
- **Providing the Web UI** for monitoring and debugging

Think of it as a highly reliable task scheduler that never loses track of what needs to be done.

| Property  | Value                     |
| --------- | ------------------------- |
| Host      | `localhost:7233`          |
| Namespace | `default`                 |
| UI        | `http://localhost:8080`   |
| Database  | PostgreSQL (configurable) |

### 2. Temporal Worker

The **Worker** is the execution engine—it's where the actual code runs. Workers are long-running processes that:

- **Poll the task queue** continuously for new work
- **Execute workflow logic** and activities when assigned
- **Report results back** to the Temporal Server
- **Can be scaled horizontally** by running multiple instances

The worker doesn't store any state itself—all state is managed by the Temporal Server. This means you can stop a worker, start a new one, and it will seamlessly continue processing.

```bash
# Start the worker
python -m src.worker.temporal_worker

# Or using the CLI entry point
prd-worker
```

**Worker Configuration:**

| Setting    | Value                     |
| ---------- | ------------------------- |
| Task Queue | `prd-agent-queue`         |
| Workflows  | 1 (PRDGenerationWorkflow) |
| Activities | 12 registered             |

> 📌 **Note**: The worker must be running before you trigger a workflow. If no workers are available, workflows will queue and wait until a worker connects.

### 3. PRDGenerationWorkflow

The **Workflow** is the orchestration logic—it defines the sequence of steps, handles dependencies between activities, and manages the overall flow. Key characteristics:

- **Deterministic**: The same input always produces the same execution path
- **Stateful**: Can maintain state across long-running operations
- **Composable**: Calls activities and waits for their completion

```python
@workflow.defn
class PRDGenerationWorkflow:
    """
    Temporal workflow that orchestrates the entire PRD generation process.
    """

    @workflow.run
    async def run(self, input: PRDGenerationInput) -> PRDGenerationOutput:
        # Executes 8 phases with 12 activities
        ...
```

The workflow is decorated with `@workflow.defn` and the main entry point is the `run` method decorated with `@workflow.run`. This tells Temporal how to execute the workflow.

---

## Workflow Execution Flow

The workflow executes in **8 distinct phases**, with some phases running activities **in parallel** for efficiency.

### Why Phases Matter

Each phase has a specific purpose in the PRD generation pipeline:

1. **Phases 1-2**: Gather and store all input data (code, screenshots, Jira)
2. **Phases 3-5**: AI agents analyze the data from different perspectives
3. **Phases 6-7**: Combine all insights into a coherent PRD document
4. **Phase 8**: Persist the final output

The phase-based approach allows us to:

- **Parallelize where possible** (e.g., screenshot + Jira analysis)
- **Ensure dependencies are met** (requirements must complete before risk analysis)
- **Fail fast** if critical steps fail (e.g., code extraction)
- **Track progress** at each stage in the Temporal UI

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PRD GENERATION WORKFLOW PHASES                           │
└─────────────────────────────────────────────────────────────────────────────┘

 TIME ──────────────────────────────────────────────────────────────────────►

 PHASE 1: DATA EXTRACTION
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  ┌──────────────────┐  ┌──────────────────┐  ┌──────────────────┐      │
 │  │ extract_code     │  │ extract_         │  │ extract_jira     │      │
 │  │ _activity        │  │ screenshots      │  │ _activity        │      │
 │  │                  │  │ _activity        │  │                  │      │
 │  └──────────────────┘  └──────────────────┘  └──────────────────┘      │
 │                     (Can run in parallel)                               │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
 PHASE 2: VECTOR STORAGE
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                    ┌──────────────────────────┐                         │
 │                    │ store_vectors_activity   │                         │
 │                    │                          │                         │
 │                    │ Creates embeddings,      │                         │
 │                    │ stores in Qdrant         │                         │
 │                    └──────────────────────────┘                         │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
 PHASE 3: INITIAL ANALYSIS (PARALLEL)
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  ┌─────────────────────────────┐  ┌─────────────────────────────┐      │
 │  │ analyze_screenshots         │  │ analyze_jira_activity       │      │
 │  │ _activity                   │  │                             │      │
 │  │                             │  │                             │      │
 │  │ GPT-4 Vision analysis       │  │ GPT-4 requirements          │      │
 │  └─────────────────────────────┘  └─────────────────────────────┘      │
 │                        (Run in parallel)                                │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
 PHASE 4: REQUIREMENTS GENERATION
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                ┌────────────────────────────────────┐                   │
 │                │ generate_requirements_activity     │                   │
 │                │                                    │                   │
 │                │ Synthesizes code + Jira +          │                   │
 │                │ screenshot context                 │                   │
 │                └────────────────────────────────────┘                   │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
 PHASE 5: FLOW & RISK ANALYSIS (PARALLEL)
 ┌─────────────────────────────────────────────────────────────────────────┐
 │  ┌─────────────────────────────┐  ┌─────────────────────────────┐      │
 │  │ analyze_user_flows          │  │ analyze_risks_activity      │      │
 │  │ _activity                   │  │                             │      │
 │  │                             │  │                             │      │
 │  │ Generates flow diagrams     │  │ Identifies migration risks  │      │
 │  └─────────────────────────────┘  └─────────────────────────────┘      │
 │                        (Run in parallel)                                │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
 PHASE 6: STORE ANALYSIS RESULTS
 ┌─────────────────────────────────────────────────────────────────────────┐
 │              ┌────────────────────────────────────────┐                 │
 │              │ store_analysis_results_activity        │                 │
 │              │                                        │                 │
 │              │ Adds analysis to knowledge base        │                 │
 │              └────────────────────────────────────────┘                 │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
 PHASE 7: PRD AGGREGATION
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                  ┌──────────────────────────────────┐                   │
 │                  │ aggregate_prd_activity           │                   │
 │                  │                                  │                   │
 │                  │ Combines all agent results       │                   │
 │                  │ into final PRD document          │                   │
 │                  └──────────────────────────────────┘                   │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
 PHASE 8: SAVE PRD
 ┌─────────────────────────────────────────────────────────────────────────┐
 │                     ┌─────────────────────────────┐                     │
 │                     │ save_prd_activity           │                     │
 │                     │                             │                     │
 │                     │ Writes .md and .json files  │                     │
 │                     └─────────────────────────────┘                     │
 └─────────────────────────────────────────────────────────────────────────┘
                                    │
                                    ▼
                          WORKFLOW COMPLETE ✓
```

---

## Registered Activities

**Activities** are the building blocks of the workflow—each activity performs a specific, isolated task. Unlike workflows, activities can:

- Make network calls (API requests, database queries)
- Perform I/O operations (file reads/writes)
- Execute non-deterministic operations (like calling GPT-4)

Activities are decorated with `@activity.defn` and registered with the worker. Each activity is independent and can be retried without affecting other activities.

### Activity Categories

We organize our 12 activities into four categories based on their function:

| Category        | Count | Description                                          |
| --------------- | ----- | ---------------------------------------------------- |
| **Extraction**  | 3     | Fetch data from external sources (code, MinIO, Jira) |
| **Storage**     | 3     | Persist data to vector store or file system          |
| **Analysis**    | 5     | AI-powered analysis using GPT-4 agents               |
| **Aggregation** | 1     | Combine multiple results into final output           |

### Complete Activity List

| #   | Activity Name                     | Category    | Timeout | Purpose                            |
| --- | --------------------------------- | ----------- | ------- | ---------------------------------- |
| 1   | `extract_code_activity`           | Extraction  | 30 min  | Parse ZIP, extract Java/SQL files  |
| 2   | `extract_screenshots_activity`    | Extraction  | 30 min  | Fetch screenshots from MinIO       |
| 3   | `extract_jira_activity`           | Extraction  | 30 min  | Query Jira API for issues          |
| 4   | `store_vectors_activity`          | Storage     | 30 min  | Create embeddings, store in Qdrant |
| 5   | `analyze_screenshots_activity`    | Analysis    | 60 min  | GPT-4 Vision UI analysis           |
| 6   | `analyze_jira_activity`           | Analysis    | 60 min  | GPT-4 requirements extraction      |
| 7   | `generate_requirements_activity`  | Analysis    | 60 min  | Generate FR/NFR requirements       |
| 8   | `analyze_user_flows_activity`     | Analysis    | 60 min  | Create user flow diagrams          |
| 9   | `analyze_risks_activity`          | Analysis    | 60 min  | Identify migration risks           |
| 10  | `store_analysis_results_activity` | Storage     | 30 min  | Add analysis to knowledge base     |
| 11  | `aggregate_prd_activity`          | Aggregation | 60 min  | Combine all results into PRD       |
| 12  | `save_prd_activity`               | Storage     | 30 min  | Write output files                 |

### Activity Execution Details

Each activity follows a consistent pattern:

1. **Receive input** from the workflow (serialized as JSON)
2. **Execute the task** (API call, file I/O, AI processing)
3. **Return result** back to the workflow (serialized as JSON)
4. **Handle errors** by raising exceptions (Temporal handles retries)

---

## Retry Policy & Error Handling

One of Temporal's most powerful features is its built-in retry mechanism. Instead of writing complex retry logic in our code, we configure retry policies and let Temporal handle failures automatically.

### Why Retries Matter for PRD Generation

PRD generation relies on external services that can fail temporarily:

- **OpenAI API**: Rate limits, timeouts, temporary outages
- **MinIO**: Network issues, connection resets
- **Jira API**: Authentication token expiry, rate limits
- **Qdrant**: Connection pool exhaustion, network latency

With Temporal's retry policy, these transient failures are handled automatically—the activity is simply retried after a brief wait.

### Retry Configuration

All activities use a consistent retry policy:

```python
retry_policy = RetryPolicy(
    initial_interval=timedelta(seconds=1),     # Start with 1 second
    maximum_interval=timedelta(minutes=5),     # Cap at 5 minutes
    maximum_attempts=3,                        # Try 3 times max
    backoff_coefficient=2.0,                   # Double wait each retry
)
```

**Retry Timing Example:**

| Attempt | Wait Before Retry |
| ------- | ----------------- |
| 1       | 0 (immediate)     |
| 2       | 1 second          |
| 3       | 2 seconds         |
| Failed  | Workflow fails    |

### Activity Timeouts

| Activity Type | Timeout | Reason                                    |
| ------------- | ------- | ----------------------------------------- |
| Standard      | 30 min  | Data extraction, storage, file operations |
| LLM-Heavy     | 60 min  | AI analysis with multiple GPT-4 calls     |

### Graceful Degradation

The workflow continues even if optional components fail:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                        GRACEFUL DEGRADATION                                 │
└─────────────────────────────────────────────────────────────────────────────┘

  ┌─────────────┐     ┌─────────────┐     ┌─────────────┐
  │ Screenshots │     │    Jira     │     │    Code     │
  │  (Optional) │     │  (Optional) │     │ (Required)  │
  └──────┬──────┘     └──────┬──────┘     └──────┬──────┘
         │                   │                   │
         ▼                   ▼                   ▼
  ┌─────────────────────────────────────────────────────┐
  │                                                     │
  │  If screenshots unavailable → Skip UI analysis      │
  │  If Jira unavailable → Skip Jira analysis           │
  │  Code always required → Workflow fails without it   │
  │                                                     │
  └─────────────────────────────────────────────────────┘
         │
         ▼
  PRD Generated with Available Data
```

---

## Temporal UI Observability

One of the most valuable features of Temporal is its built-in Web UI. Unlike traditional background job systems where you're left guessing what's happening, Temporal provides complete visibility into every workflow execution.

### Accessing the Temporal UI

The Temporal Web UI is available at `http://localhost:8080` when running locally. It provides a real-time view of all workflows, their status, and detailed execution history.

> 📎 **INSERT IMAGE: Temporal Workflow Execution Screenshot**

### What You Can See:

| View                | Information                                       |
| ------------------- | ------------------------------------------------- |
| **Event History**   | Complete timeline of all activities               |
| **Input/Output**    | JSON payloads for workflow input and result       |
| **Activity Status** | Success/failure for each activity                 |
| **Timing**          | Duration of each activity and total workflow time |
| **Retries**         | Number of retry attempts per activity             |
| **Workers**         | Which worker processed the workflow               |

### Example Workflow Result

```json
{
  "form_name": "le11",
  "success": true,
  "prd_file_path": "output/le11_PRD.md",
  "vector_collection": "prd_agent_le11",
  "word_count": 6261,
  "section_count": 9,
  "execution_time_seconds": 20.19,
  "agent_results": {
    "screenshot_analysis": true,
    "jira_analysis": false,
    "requirements_analysis": true,
    "user_flow_analysis": true,
    "risk_analysis": true
  }
}
```

---

## Workflow Input & Output

### Input (PRDGenerationInput)

```python
@dataclass
class PRDGenerationInput:
    form_name: str                          # Required: e.g., "le11"
    zip_path: str | None                    # Path to code ZIP
    code_directory: str | None              # Or path to code directory
    file_mappings: list[str] | None         # Specific files to include
    dependency_file: str | None             # Filter file for dependencies
    minio_bucket: str | None                # Screenshot bucket
    minio_prefix: str | None                # Screenshot prefix
    jira_project_key: str | None            # Jira project
    jira_jql: str | None                    # Custom JQL query
    output_dir: str = "./output"            # Output directory
    recreate_vector_collection: bool = False # Force recreate collection
    skip_screenshots: bool = False          # Skip screenshot analysis
    skip_jira: bool = False                 # Skip Jira analysis
```

### Output (PRDGenerationOutput)

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

---

## How to Trigger a Workflow

There are two ways to start a PRD generation workflow: via the CLI (recommended for most users) or programmatically (for integration with other systems).

### Via CLI (Recommended)

The CLI is the easiest way to trigger a workflow. It handles connecting to Temporal and starting the workflow with the right parameters:

```bash
prd-agent generate \
  --form-name le11 \
  --zip-path src/templates_code_zip/java.zip \
  --dependency-file src/form_dependencies/le11_dependencies.txt \
  --output ./output
```

### Programmatically

For integration with other systems (like a web API or batch processing pipeline), you can trigger workflows programmatically using the Temporal Python SDK:

```python
from temporalio.client import Client
from src.workflows.prd_generation_workflow import (
    PRDGenerationWorkflow,
    PRDGenerationInput,
)

async def run_workflow():
    # Connect to Temporal server
    client = await Client.connect("localhost:7233")

    # Execute the workflow and wait for result
    result = await client.execute_workflow(
        PRDGenerationWorkflow.run,
        PRDGenerationInput(
            form_name="le11",
            zip_path="src/templates_code_zip/java.zip",
            dependency_file="src/form_dependencies/le11_dependencies.txt",
        ),
        id="prd-generation-le11",        # Unique workflow ID
        task_queue="prd-agent-queue",    # Must match worker's queue
    )

    print(f"Success: {result.success}")
    print(f"PRD: {result.prd_file_path}")
```

**Key points:**

- The `id` must be unique for each workflow execution
- The `task_queue` must match what the workers are listening on
- `execute_workflow` blocks until the workflow completes (use `start_workflow` for fire-and-forget)

---

## Parallel Execution Strategy

One of the key optimizations in our workflow design is **parallel execution** of independent activities. Since some activities don't depend on each other's output, we can run them simultaneously—significantly reducing total execution time.

### How We Identify Parallelization Opportunities

We analyze the data dependencies between activities:

- **Screenshot analysis** needs: screenshots ✓ (available after extraction)
- **Jira analysis** needs: Jira issues ✓ (available after extraction)
- Neither depends on the other → **Run in parallel**

Similarly:

- **User flow analysis** needs: screenshot analysis results
- **Risk analysis** needs: requirements results
- Neither depends on the other → **Run in parallel**

The workflow maximizes efficiency by running independent activities in parallel:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    PARALLEL EXECUTION STRATEGY                              │
└─────────────────────────────────────────────────────────────────────────────┘

 Sequential (must wait)          Parallel (run together)
 ─────────────────────          ──────────────────────────

                                ┌───────────────────────┐
 extract_code ─────────────────►│ analyze_screenshots   │
                                │                       │
                                │ analyze_jira          │
                                └───────────┬───────────┘
                                            │
 generate_requirements ◄────────────────────┘
                                            │
                                ┌───────────▼───────────┐
                                │ analyze_user_flows    │
                                │                       │
                                │ analyze_risks         │
                                └───────────┬───────────┘
                                            │
 aggregate_prd ◄────────────────────────────┘
```

**Parallel Groups:**

1. **Phase 3**: Screenshot + Jira analysis run simultaneously
2. **Phase 5**: User flow + Risk analysis run simultaneously

This reduces total workflow time by ~40% compared to sequential execution.

---

## Worker Scaling

One of Temporal's greatest strengths is its ability to scale horizontally. When you need to process more workflows concurrently, you simply start more workers—no code changes required.

### How Scaling Works

Workers are stateless—they don't hold any workflow state themselves. All state is managed by the Temporal Server. This means:

1. **Adding workers is trivial**: Just run another instance of the worker process
2. **Workers can run anywhere**: Same machine, different servers, even different data centers
3. **Load is distributed automatically**: Temporal assigns tasks to available workers
4. **Failover is seamless**: If a worker dies, another picks up its work

Multiple workers can be started to handle concurrent workflows:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                         WORKER SCALING                                      │
└─────────────────────────────────────────────────────────────────────────────┘

                        Task Queue: prd-agent-queue
                                    │
         ┌──────────────────────────┼──────────────────────────┐
         │                          │                          │
         ▼                          ▼                          ▼
 ┌───────────────┐          ┌───────────────┐          ┌───────────────┐
 │   Worker 1    │          │   Worker 2    │          │   Worker 3    │
 │   (Server 1)  │          │   (Server 2)  │          │   (Server 3)  │
 │               │          │               │          │               │
 │ Processing:   │          │ Processing:   │          │ Processing:   │
 │ le01, le02    │          │ le03, le04    │          │ le05, le06    │
 └───────────────┘          └───────────────┘          └───────────────┘

 Each worker can handle multiple concurrent workflows.
 Temporal automatically distributes work across available workers.
```

**To start additional workers:**

```bash
# Terminal 1
python -m src.worker.temporal_worker

# Terminal 2
python -m src.worker.temporal_worker

# Terminal 3
python -m src.worker.temporal_worker
```

---

## Benefits of Temporal Orchestration

Choosing Temporal for PRD Agent orchestration provides significant advantages over traditional approaches (like cron jobs, message queues, or custom state machines).

### Key Benefits Summary

| Benefit                | Description                                          | Impact                                    |
| ---------------------- | ---------------------------------------------------- | ----------------------------------------- |
| **Durability**         | Workflow state persists through crashes and restarts | No lost progress, reliable completion     |
| **Automatic Retries**  | Failed activities retry automatically with backoff   | Handles transient failures gracefully     |
| **Visibility**         | Full execution history in Temporal UI                | Easy debugging and monitoring             |
| **Scalability**        | Add more workers to handle more concurrent workflows | Process 100s of forms in parallel         |
| **Reliability**        | Guaranteed exactly-once execution of activities      | No duplicate processing, consistent state |
| **Timeout Handling**   | Activities timeout gracefully, triggering retries    | Prevents stuck workflows                  |
| **Parallel Execution** | Independent activities run concurrently              | ~40% faster execution time                |
| **State Management**   | No need to manually track workflow progress          | Cleaner code, fewer bugs                  |

### Real-World Impact

For PRD Agent specifically, Temporal provides:

- **Zero data loss**: If a GPT-4 call fails mid-analysis, we don't lose the extraction work already done
- **Predictable execution**: Every workflow either completes successfully or fails with a clear error
- **Operational visibility**: DevOps can see exactly what's happening in the Temporal UI
- **Easy scaling**: Process multiple legacy forms simultaneously by adding workers

---

## Troubleshooting

When things don't work as expected, here's how to diagnose and fix common issues.

### Common Issues and Solutions

| Issue                       | Symptoms                                 | Solution                                                |
| --------------------------- | ---------------------------------------- | ------------------------------------------------------- |
| Worker not picking up tasks | Workflow shows "Running" but no progress | Check task queue name matches between CLI and worker    |
| Activity timeout            | Workflow fails with timeout error        | Increase timeout or optimize the slow activity          |
| Connection refused          | Worker fails to start                    | Ensure Temporal server is running (`docker-compose up`) |
| Workflow stuck              | Workflow shows "Running" for hours       | Check Temporal UI → Event History for pending activity  |
| OpenAI rate limit           | Activity retries repeatedly              | Wait for rate limit to reset, or upgrade API tier       |
| Missing dependencies        | Worker crashes on import                 | Run `pip install -e .` to install all dependencies      |

### Debugging Workflow Failures

1. **Open Temporal UI** at `http://localhost:8080`
2. **Find your workflow** by ID or filter by status
3. **Click on the workflow** to see the Event History
4. **Look for failed activities** (marked in red)
5. **Click on the activity** to see the error message and stack trace

### Useful Commands

```bash
# Check Temporal server status
docker-compose ps

# View Temporal UI
open http://localhost:8080

# Check worker logs
python -m src.worker.temporal_worker 2>&1 | tee worker.log
```

---

## Summary

Temporal orchestration is the backbone of PRD Agent's reliability and scalability. By leveraging Temporal, we achieve:

```
┌─────────────────────────────────────────────────────────────────────────────┐
│                    TEMPORAL ORCHESTRATION VALUE                             │
└─────────────────────────────────────────────────────────────────────────────┘

   WITHOUT TEMPORAL                      WITH TEMPORAL
   ────────────────                      ─────────────

   ❌ Manual retry logic                 ✅ Automatic retries with backoff
   ❌ Lost progress on failures          ✅ Durable state across restarts
   ❌ Complex state management           ✅ State handled automatically
   ❌ Limited visibility                 ✅ Full UI for monitoring/debugging
   ❌ Difficult to scale                 ✅ Add workers for more throughput
   ❌ Sequential execution only          ✅ Parallel activities where possible
```

The investment in Temporal pays dividends in:

- **Developer productivity**: Focus on business logic, not infrastructure
- **Operational confidence**: Know that workflows will complete reliably
- **Easy debugging**: Full execution history for troubleshooting
- **Future-proof architecture**: Scale as the number of forms to process grows

---

_For more details on the overall PRD Agent architecture and the knowledge base approach, see the main Confluence page._
