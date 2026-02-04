# Agentic Migration – Technical Documentation

**Document purpose:** Technical overview of the Agentic Migration feature for JIRA/Confluence.  
**Audience:** Engineering, Product, and stakeholders.  
**Last updated:** February 2025.

---

## 1. Overview

### 1.1 What Is Agentic Migration?

**Agentic Migration** is an AI-driven code migration system that automates the conversion of legacy Java/Swing codebases to a modern stack:

| Source (Legacy)    | Target (Modern)      |
| ------------------ | -------------------- |
| Java / Java Swing  | .NET (C#) backend    |
| Oracle DB patterns | PostgreSQL / EF Core |
| Monolithic UI      | React (TypeScript)   |

The system uses an **AI agent** (Anthropic Claude) that behaves like an expert developer: it gathers context via tools, reasons over the codebase and documentation, and generates backend and frontend code in a structured output directory. No manual code generation is required for the initial pass.

### 1.2 Goals

- **Knowledge-first:** All relevant form knowledge (docs, schema, business logic, templates) is gathered before any code is generated.
- **Tool-augmented:** The agent uses a fixed set of tools (file, code search, database, MinIO) instead of relying only on a single prompt.
- **Structured output:** Generated code follows a standard layout (backend/frontend, templates) and uses Oracle→PostgreSQL mappings and existing conversion prompts.
- **Parity:** Generated code aims for behavioral parity with the legacy system (validation, business rules, UI flow).

---

## 2. Approach

### 2.1 High-Level Flow

1. **User** runs the migration command for a form (e.g. `LE11`) and an output directory.
2. **Migration Orchestrator** is created with that form name and output path; it has a system prompt and a registered set of tools.
3. **Agent Runner** runs a loop:
   - Send conversation history (including optional user prompt) to Claude.
   - If Claude returns **tool use** → execute tools, append results to history, call Claude again.
   - If Claude returns **end of turn** (no tool use) → treat as final response and exit.
4. **Tools** provide: form docs, dependencies, DB schema, code search, template prompts, file read/write within the output directory.
5. **Output** is a directory tree of generated backend (.NET) and frontend (React) code.

### 2.2 Knowledge-First Discipline

The system prompt enforces a **mandatory order of operations**:

1. **Gather knowledge** – e.g. `get_all_form_knowledge`, `list_export_templates`, `get_conversion_prompt("backend"|"frontend")`, `get_oracle_to_postgres_mapping`.
2. **Understand schema** – e.g. `get_database_schema`, `search_legacy_schema`, `get_highly_connected_tables`.
3. **Extract business logic** – e.g. `search_codebase`, `get_code_context`, `get_business_logic`.
4. **Generate backend** – Entities, Repositories, Services, DTOs, Controllers (using templates and mappings).
5. **Generate frontend** – React components, pages, services, types (using templates and screenshots).
6. **Verify** – Check logic, mappings, and UI alignment.

The agent is instructed **not** to generate code until the relevant knowledge steps have been performed.

### 2.3 Why an Agentic Design?

- **Context limits:** A single prompt cannot hold full codebases and all docs. Tools let the agent pull only what it needs per step.
- **Accuracy:** Using real schema, real templates, and real business-logic search reduces hallucination and keeps output aligned with existing standards.
- **Flexibility:** The same orchestrator and tools can support different forms and slight variations in process without changing core code.
- **Auditability:** Message history (user, assistant, tool calls/results) can be logged for debugging and compliance.

---

## 3. Architecture

### 3.1 Components

| Component                 | Responsibility                                                                                                                              |
| ------------------------- | ------------------------------------------------------------------------------------------------------------------------------------------- |
| **AgenticAgent**          | Base class: Anthropic client, message history, tool registry, working-directory validation.                                                 |
| **MigrationOrchestrator** | Concrete agent: form name, output dir, system prompt, and full tool set for migration.                                                      |
| **AgentRunner**           | Execution loop: call Claude, handle tool_use (including parallel tool calls), append tool results, repeat until end_turn or max iterations. |
| **MessageHistory**        | Converts in-memory conversation (user/assistant/tool) to Anthropic API message format; supports truncation.                                 |
| **ToolRegistry**          | Registers tools (name, description, parameters, function); validates and executes; exposes schema for Claude.                               |

### 3.2 Data Flow

```
User / CLI
    → migrate_agentic(form_name, output_dir)
        → MigrationOrchestrator(form_name, output_dir)
        → orchestrator.migrate(prompt?)
            → AgentRunner(orchestrator).run()
                → loop:
                    → message_history → Claude API (messages + tools)
                    → Claude → tool_use or end_turn
                    → if tool_use: execute tools → tool_result → message_history → repeat
                    → if end_turn: return final text
        → result summary + listing of generated files
```

### 3.3 Configuration

- **Working directory:** The output directory; all file tools (read/write/list/find) are restricted to this tree.
- **Max iterations:** Cap on agent loop steps (e.g. 50) to avoid runaway runs.
- **Model:** Claude (e.g. `claude-sonnet-4-5-20250929`), with configurable `max_tokens` and `temperature`.
- **Verbose:** Optional logging of each tool call and response for debugging.

---

## 4. Tools Available to the Agent

The Migration Orchestrator registers the following tools. All are read-only except file write operations scoped to the output directory.

### 4.1 File Tools

| Tool               | Purpose                                              |
| ------------------ | ---------------------------------------------------- |
| `get_files_info`   | List files and directories in the output tree.       |
| `get_file_content` | Read contents of a file.                             |
| `write_file`       | Write content to a file (creates parents if needed). |
| `find_files`       | Find files by glob pattern (e.g. `**/*.cs`).         |

### 4.2 Code / Knowledge Base Tools

| Tool                 | Purpose                                                                |
| -------------------- | ---------------------------------------------------------------------- |
| `search_codebase`    | Semantic search over form knowledge base (code, docs, business logic). |
| `get_code_context`   | Get relevant code context for a topic (optional doc_type filter).      |
| `get_business_logic` | Get business logic for a given topic.                                  |

### 4.3 Database Tools

| Tool                             | Purpose                                                     |
| -------------------------------- | ----------------------------------------------------------- |
| `get_database_schema`            | Get database schema for the form.                           |
| `get_table_mappings`             | Get table relationships and mappings (optional table_name). |
| `search_legacy_schema`           | Search legacy (Oases) table schema and relationships.       |
| `search_target_schema`           | Search target (Lumina) table schema and relationships.      |
| `get_oracle_to_postgres_mapping` | Get Oracle → PostgreSQL data type mapping guide.            |
| `get_highly_connected_tables`    | Get highly connected tables (critical for migration).       |
| `get_table_relationships`        | Get relationships for a specific table.                     |

### 4.4 MinIO / Form Knowledge Tools

| Tool                     | Purpose                                                           |
| ------------------------ | ----------------------------------------------------------------- |
| `get_form_docs`          | Get all form documentation from MinIO.                            |
| `get_dependencies`       | Get list of files that belong to the form.                        |
| `list_screenshots`       | List UI screenshots for the form.                                 |
| `get_db_prd`             | Get global database PRD documentation.                            |
| `get_conversion_prompt`  | Get conversion prompt template (backend or frontend).             |
| `get_all_form_knowledge` | Aggregated knowledge: docs, dependencies, screenshots, DB schema. |
| `list_export_templates`  | List available BE/FE export code templates.                       |
| `get_export_template`    | Get a specific backend or frontend export template.               |
| `get_ui_flow_docs`       | Get UI flow documentation.                                        |

---

## 5. Migration Process (As Enforced by System Prompt)

The agent is instructed to follow this sequence:

1. **Step 1 – Gather knowledge**  
   Call `get_all_form_knowledge`, `list_export_templates`, `get_conversion_prompt("backend")`, `get_conversion_prompt("frontend")`, `get_oracle_to_postgres_mapping`.

2. **Step 2 – Database schema**  
   Call `get_database_schema`, `search_legacy_schema` where needed, `get_highly_connected_tables`.

3. **Step 3 – Business logic**  
   Call `search_codebase`, `get_code_context`, `get_business_logic` as needed.

4. **Step 4 – Backend (.NET)**  
   Generate Entities, Repositories, Services, DTOs, Controllers using the backend conversion template and Oracle→PostgreSQL mappings.

5. **Step 5 – Frontend (React)**  
   Use `list_screenshots` and frontend template to generate components, pages, services, types.

6. **Step 6 – Verify**  
   Ensure business logic, entity-to-table mappings, and UI alignment are consistent.

Critical rules passed to the agent:

- Generate **only** code files (e.g. .cs, .tsx, .ts, .json, .csproj). No standalone documentation files (e.g. .md, README, MANIFEST).
- Follow exact output format from templates.
- Use Oracle→PostgreSQL type mappings for entities.
- Prefer inline code comments over separate doc files.

---

## 6. Output Structure

The agent writes under the configured output directory. Expected layout (from templates):

```
output/
├── backend/
│   ├── {ProjectName}.Data/Entities/
│   ├── {ProjectName}.Data/Repositories/
│   ├── {ProjectName}.Business/Services/
│   ├── {ProjectName}.Business/DTOs/
│   └── {ProjectName}.API/Controllers/
└── frontend/
    ├── components/
    ├── pages/
    ├── services/
    └── types/
```

The CLI reports a summary of the agent’s final response and, when the output directory exists, shows file counts under `backend` and `frontend`.

---

## 7. Usage

### 7.1 Prerequisites

- Form name (e.g. `le11`, `ea01`).
- MinIO (or compatible store) populated with form docs, dependencies, templates, and conversion prompts.
- Vector store (e.g. Qdrant) with form knowledge indexed for `search_codebase` / `get_code_context`.
- Database knowledge (legacy/target schema, Oracle→PostgreSQL mapping) available via the registered tools.
- Anthropic API key and any required embedding/vector store configuration.

### 7.2 Command

```bash
prd-agent migrate-agentic --form-name le11 --output ./output/agentic
```

Optional:

- `--prompt` / `-p`: Custom migration prompt (overrides default form-specific prompt).
- `--verbose` / `-v`: Enable verbose logging (e.g. per-tool call).

### 7.3 Programmatic Usage

```python
from pathlib import Path
from src.core.agentic import AgenticConfig
from src.core.migration import get_migration_orchestrator

config = AgenticConfig(
    working_directory=Path("./output/agentic"),
    verbose=False,
    max_iterations=50,
)
orchestrator = get_migration_orchestrator()(
    form_name="le11",
    output_dir=Path("./output/agentic"),
    config=config,
)
result = await orchestrator.migrate()  # or migrate(prompt="...")
```

---

## 8. Technical Stack

| Layer        | Technology / Component                                     |
| ------------ | ---------------------------------------------------------- |
| LLM          | Anthropic Claude (e.g. claude-sonnet-4-5-20250929)         |
| Embeddings   | OpenAI (or configured embedding service for vector search) |
| Vector store | Qdrant (for code/knowledge search)                         |
| Object store | MinIO (form docs, templates, conversion prompts)           |
| Runtime      | Python 3.x, asyncio for agent loop                         |
| CLI          | Typer                                                      |

---

## 9. Related Agents (Optional Use)

The codebase also includes specialized agents that can be used for narrower tasks or future extensions:

- **DatabaseMigrationAgent** – Focused on EF Core entities, repositories, DbContext from legacy schema.
- **UIMigrationAgent** – Focused on React frontend (TypeScript, components, services).
- **CodeGenerationAgent** – Focused on ASP.NET Core API and React code generation.

The **Migration Orchestrator** is the single entry point used by the `migrate-agentic` command and performs the full flow (knowledge → backend → frontend) using the shared tool set.

---

## 10. Summary

| Item               | Description                                                                                                |
| ------------------ | ---------------------------------------------------------------------------------------------------------- |
| **Feature**        | Agentic Migration – AI-driven migration from legacy Java/Oracle to .NET + React.                           |
| **Approach**       | Knowledge-first, tool-augmented agent (Claude) with a fixed process and tool set.                          |
| **Main component** | MigrationOrchestrator (AgenticAgent) + AgentRunner + ToolRegistry + MessageHistory.                        |
| **Execution**      | Loop: Claude request → tool_use or end_turn → execute tools → append results → repeat.                     |
| **Output**         | Structured backend (e.g. .NET) and frontend (e.g. React) code under a configurable output directory.       |
| **Usage**          | CLI: `prd-agent migrate-agentic -f <form_name> -o <output_dir>`; or programmatic `orchestrator.migrate()`. |

This document is intended for publication in JIRA/Confluence as the technical reference for the Agentic Migration feature.
