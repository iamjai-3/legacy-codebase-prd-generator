# Token Usage Analysis & Mitigations

This document summarizes where tokens are consumed in the project and the changes made to reduce cost (e.g. avoiding high spend like **$50 in 2 days**).

## Where Tokens Are Consumed

### 1. Agentic migration flow (main cost driver)

- **Entry**: `MigrationOrchestrator` → `AgentRunner.run()` → `_call_claude()` every iteration.
- **Per request**: Full **system prompt** (~2.5k chars) + **entire message history** (user, assistant, tool results) sent to Claude every round.
- **Tool results**: Each tool result is capped at **20k chars** (~5k tokens) in `agent_runner.py`; large tools (e.g. `get_all_form_knowledge`, `get_code_context`) can hit this cap repeatedly.
- **Iterations**: Up to **50** rounds per migration; each round = 1 API call with growing context.
- **Output**: `max_tokens=8192` per response (default in `AgenticConfig`).

So a single migration can do **dozens of API calls**, each with **large input** (system + history + tools) and **large output allowance**, which quickly drives cost.

### 2. PRD generation workflow (Temporal)

- **Activities**: `analyze_screenshots_activity`, `generate_requirements_activity`, `analyze_user_flows_activity`, `analyze_database_activity`, plus aggregation.
- Each activity runs a **LangChain agent** (OpenAI or Anthropic) with:
  - Vector search context (multiple `retrieve_context` / `get_code_context` with limits 5–20).
  - Large prompts (e.g. `RequirementsGeneratorAgent` with many `max_contexts` 5–10).
- **Settings**: `max_tokens=4096` per request (from `settings.openai` / `settings.anthropic`).

### 3. Tools that return large payloads

| Tool                                        | Behavior                                                                      | Risk                                                                |
| ------------------------------------------- | ----------------------------------------------------------------------------- | ------------------------------------------------------------------- |
| `get_all_form_knowledge`                    | Concatenates docs (was truncated at 10k) + deps + screenshots + DB summary    | Single call can be ~20k chars after runner cap                      |
| `get_code_context`                          | Returns **full** content of up to 5 chunks (each chunk up to ~30k in storage) | 5×30k = 150k chars → runner truncates to 20k; work done for nothing |
| `search_codebase`                           | 10 results × 500 chars each = 5k                                              | Lower risk                                                          |
| `get_database_schema`, `get_table_mappings` | Variable size                                                                 | Capped by runner                                                    |

### 4. Context window handling

- **Token estimate**: `MessageHistory` uses `len(content)//4` (rough).
- **Truncation**: Only when `estimated_tokens > 180_000`; then `truncate_to_recent(max_messages=10)`.
- So we often send **very large** context before trimming, and when we trim we keep only **10** messages (aggressive).

### 5. Caching

- **Cache**: `CacheManager` supports `TOOL_RESULT` and `LLM_RESPONSE` with TTL.
- **Agentic flow**: Does **not** use cache; every tool call and every Claude call is fresh. Repeated tools (e.g. same `get_database_schema` twice) double payload.

---

## Mitigations Implemented

### 1. Agentic defaults (cost vs. quality)

- **`AgenticConfig.max_tokens`**: `8192` → **`4096`** to reduce output tokens per turn.
- **`AgenticConfig.max_iterations`**: `50` → **`25`** to cap runaway loops and total calls.

(Defaults can be overridden when constructing `AgenticConfig` if a run needs more.)

### 2. Tool result size at source

- **`get_code_context`**:
  - **Per-chunk cap**: Each retrieved chunk is limited to **4000 characters** before concatenation (constant `CODE_CONTEXT_CHUNK_MAX_CHARS`). So 5 chunks → max 20k chars, matching runner cap and avoiding wasted retrieval.
  - **Default limit**: Remains 5; orchestrator can pass a lower `limit` if desired.
- **`get_all_form_knowledge`**:
  - Form docs truncation **10k** → **6k** characters to reduce tokens while keeping enough for “knowledge first” step.

### 3. Proactive context truncation and usage logging

- **Earlier truncation**: In `agent_runner._call_claude()`, truncate when **`estimated_tokens > 100_000`** (instead of 180k) and keep **20** recent messages (instead of 10) for better continuity.
- **Token usage logging**: After each Claude call, log **input_tokens** and **output_tokens** at INFO so you can monitor spend (e.g. in CloudWatch or logs aggregation).

### 4. Constants and configuration

- **`TOOL_RESULT_MAX_CHARS`**: Kept at **20_000** in `agent_runner.py`; source-side caps above keep tool results within this.
- **`docs/TOKEN_ANALYSIS.md`**: This document for future tuning and onboarding.

---

## Optional Next Steps (not implemented)

- **Cache agentic tool results**: For idempotent tools (`get_database_schema`, `get_form_docs`, `get_conversion_prompt`, etc.), cache by `(tool_name, form_name, args_hash)` with `tool_result_ttl` to avoid re-sending same large payloads when the agent calls the same tool again.
- **Shorter system prompt**: Trim or summarize the migration system prompt and move detailed steps into a “retrieve on demand” doc.
- **Actual token counting**: Use `tiktoken` (or Anthropic’s tokenizer) for `MessageHistory.estimated_tokens` and for logging “estimated input tokens” before each call.
- **Env-driven agentic config**: Read `max_tokens` and `max_iterations` from env (e.g. `ANTHROPIC_MAX_TOKENS`, `AGENT_MAX_ITERATIONS`) so ops can tune without code change.
- **PRD workflow**: Review `RequirementsGeneratorAgent` context limits and chunk sizes; consider lowering `max_contexts` or retrieval `limit` for non-critical sections.

---

## How to Monitor Spend

1. **Logs**: After deployment, grep for `usage_input` / `usage_output` (or the new “Claude usage” log line) to sum input/output tokens per run.
2. **Anthropic dashboard**: Use usage and cost by project/model/timeframe.
3. **Alerts**: Set a budget or daily token/cost alert so issues like “$50 in 2 days” are caught early.

With these changes, the same migration should use fewer tokens per run and hit the 20k tool cap less often, reducing cost while keeping behavior acceptable. If quality drops (e.g. migrations incomplete in 25 iterations), increase `max_iterations` or `max_tokens` selectively.
