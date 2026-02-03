# PRD Agent - Working Commands Reference

Complete reference for all working PRD Agent commands.

---

## Quick Start

```bash
# 1. Start services
docker-compose up -d

# 2. Install dependencies
pip install -e .

# 3. Start Temporal worker (in separate terminal)
python -m src.worker.temporal_worker

# 4. Generate PRD
prd-agent generate -f le11 -o ./output

# 5. Migrate code with AI
prd-agent migrate-agentic -f le11 -o ./output/agentic
```

---

## Infrastructure Setup

### Start All Services

```bash
docker-compose up -d
```

Starts: PostgreSQL, Temporal, Temporal UI, Qdrant, MinIO, n8n

### Verify Services

```bash
docker-compose ps
```

### Stop Services

```bash
docker-compose down
```

### Web UIs

```bash
# Temporal UI (workflow monitoring)
open http://localhost:8080

# MinIO Console (object storage)
open http://localhost:9001
# Login: minioadmin / minioadmin

# Qdrant Dashboard (vector database)
open http://localhost:6333/dashboard
```

---

## Environment Setup

### Install Dependencies

```bash
python3 -m venv venv
source venv/bin/activate
pip install -e .
```

### Configure Environment

```bash
cp env.example .env
# Edit .env and set:
# - OPENAI_API_KEY or ANTHROPIC_API_KEY
# - LLM_PROVIDER (openai or anthropic)
```

---

## Temporal Worker

**Required**: Must be running for `generate` command

```bash
# In separate terminal
source venv/bin/activate
python -m src.worker.temporal_worker
```

---

## PRD Generation

### Basic Command (Using MinIO)

```bash
prd-agent generate -f le11 -o ./output
```

Automatically loads:

- Legacy codebase from `LEGACY_CODEBASE/` in MinIO
- Dependencies from `FORMS/LE11/FORM_FILE_DEPENDENCIES/le11_dependencies.txt`
- Screenshots from `FORMS/LE11/UI_SCREENSHOTS/`

### With Local ZIP File

```bash
prd-agent generate -f le11 -z ./code.zip -o ./output
```

### With Local Code Directory

```bash
prd-agent generate -f le11 -c ./src/code -o ./output
```

### All Options

```bash
prd-agent generate \
  --form-name le11 \
  --zip-path ./code.zip \
  --output ./output
```

**Options:**

- `-f, --form-name` (required): Form name (e.g., le11, le07)
- `-z, --zip-path`: Path to code ZIP file
- `-c, --code-dir`: Path to code directory
- `-o, --output`: Output directory (default: `./output`)

---

## Agentic Code Migration

### Basic Migration

```bash
prd-agent migrate-agentic -f le11 -o ./output/agentic
```

Uses AI agents (Anthropic Claude) to:

1. Read form documentation from MinIO
2. Search vector knowledge base
3. Generate .NET backend + React frontend

### With Verbose Output

```bash
prd-agent migrate-agentic -f le11 -o ./output/agentic -v
```

### With Custom Prompt

```bash
prd-agent migrate-agentic -f le11 -o ./output/agentic \
  -p "Focus on database entities and API endpoints"
```

**Options:**

- `-f, --form-name` (required): Form name
- `-o, --output`: Output directory (default: `./output/agentic`)
- `-p, --prompt`: Custom migration prompt
- `-v, --verbose`: Enable verbose output

**Output Structure:**

```
output/agentic/
├── backend/
│   └── {FormName}Management/
│       ├── {FormName}Management.API/        # ASP.NET Core API
│       ├── {FormName}Management.Business/   # Business logic
│       ├── {FormName}Management.Data/       # EF Core entities
│       └── {FormName}Management.Common/     # Shared models
└── frontend/
    └── {form-name}-management/
        ├── src/
        │   ├── components/
        │   ├── pages/
        │   ├── services/
        │   └── types/
        └── package.json
```

**Note:** Run `generate` first to populate knowledge base

---

## Vector Store Commands

### List All Collections

```bash
prd-agent list-collections
```

### Get Collection Statistics

```bash
prd-agent stats -f le11
```

### Search Knowledge Base

```bash
prd-agent search -f le11 -q "validation rules" -l 10
```

### Search with Type Filter

```bash
prd-agent search -f le11 -q "user flow" -t code
prd-agent search -f le11 -q "UI components" -t screenshot
prd-agent search -f le11 -q "requirements" -t jira
```

**Options:**

- `-f, --form-name` (required): Form name
- `-q, --query` (required): Search query
- `-l, --limit`: Maximum results (default: 5)
- `-t, --type`: Filter by doc type (code, screenshot, jira)

### Delete Collection

```bash
prd-agent delete-collection -f le11 --yes
```

Deletes:

- Qdrant vector collection
- MinIO form data (FORMS/LE11/\*)

**Options:**

- `-f, --form-name` (required): Form name
- `-y, --yes`: Skip confirmation
- `--delete-minio` / `--no-delete-minio`: Control MinIO deletion (default: true)

---

## MinIO Management

### Create Base Folder Structure

```bash
prd-agent create-minio-folders
```

Creates:

- `FORMS/` (parent folder)
- `DB_PRD/`
- `EXPORT_CODEBASE_PRD/BE/` and `FE/`
- `LEGACY_CODEBASE/`

### Create Folders for Specific Form

```bash
prd-agent create-form-folders LE11
```

Creates:

- `FORMS/LE11/FORM_DOCS/`
- `FORMS/LE11/FORM_FILE_DEPENDENCIES/`
- `FORMS/LE11/UI_SCREENSHOTS/`

### MinIO Folder Structure

```
metadata/ (bucket)
├── DB_PRD/                          # Database schema docs
│   └── schema.md
├── EXPORT_CODEBASE_PRD/             # Migration prompt templates
│   ├── BE/
│   │   └── dotnet_backend_conversion_prompt.txt
│   └── FE/
│       └── react_frontend_conversion_prompt.txt
├── FORMS/                           # Form-specific data
│   └── {FORM_NAME}/                 # e.g., LE11 (UPPERCASE)
│       ├── FORM_DOCS/               # Requirements, specs
│       ├── FORM_FILE_DEPENDENCIES/  # Dependency lists
│       └── UI_SCREENSHOTS/          # UI images
└── LEGACY_CODEBASE/                 # Legacy code archives
    └── oases-master.zip
```

### Delete Entire Bucket

⚠️ **WARNING**: Deletes ALL data for ALL forms!

```bash
prd-agent delete-bucket --bucket metadatas --yes
```

---

## Cache Management

### View Cache Statistics

```bash
prd-agent cache-stats
```

Shows:

- Total entries per cache type
- Active (non-expired) entries
- Hit counts and averages

### Clear Specific Cache Type

```bash
prd-agent cache-clear -t llm_response --yes
prd-agent cache-clear -t vector_search --yes
prd-agent cache-clear -t tool_result --yes
```

### Clear All Cache

```bash
prd-agent cache-clear --yes
```

**Cache Types:**

- `llm_response`: Claude/GPT-4 API responses
- `vector_search`: Qdrant search results
- `tool_result`: Tool execution results

**Cache Configuration** (in `.env`):

```bash
CACHE_ENABLED=true
CACHE_HOST=localhost
CACHE_PORT=5432
CACHE_DATABASE=temporal
CACHE_USER=temporal
CACHE_PASSWORD=temporal
CACHE_LLM_RESPONSE_TTL=86400    # 24 hours
CACHE_VECTOR_SEARCH_TTL=3600    # 1 hour
CACHE_TOOL_RESULT_TTL=1800      # 30 minutes
```

---

## Utility Commands

### Check Version

```bash
prd-agent version
```

### Show Help

```bash
prd-agent --help
prd-agent generate --help
prd-agent migrate-agentic --help
```

---

## Troubleshooting

### Test Temporal Connection

```bash
python -c "
import asyncio
from temporalio.client import Client

async def test():
    client = await Client.connect('localhost:7233')
    print('✓ Connected to Temporal')

asyncio.run(test())
"
```

### Test Qdrant Connection

```bash
curl http://localhost:6333/health
```

### Test MinIO Connection

```bash
curl http://localhost:9000/minio/health/live
```

### Test PostgreSQL Connection

```bash
docker exec -it prd-agent-temporal-db psql -U temporal -d temporal -c "SELECT version();"
```

### Check API Keys

```bash
python -c "
from src.config.settings import get_settings
s = get_settings()
print(f'LLM Provider: {s.llm.provider}')
print(f'OpenAI Key: {'✓' if s.openai.api_key else '✗'}')
print(f'Anthropic Key: {'✓' if s.anthropic.api_key else '✗'}')
"
```

---

## Common Workflows

### 1. First Time Setup

```bash
# Clone repo and install
git clone <repo>
cd PRD_Agent
python3 -m venv venv
source venv/bin/activate
pip install -e .

# Configure
cp env.example .env
# Edit .env with API keys

# Start services
docker-compose up -d

# Create MinIO folders
prd-agent create-minio-folders
prd-agent create-form-folders LE11

# Upload files to MinIO (via UI at localhost:9001):
# - LEGACY_CODEBASE/oases-master.zip
# - FORMS/LE11/FORM_FILE_DEPENDENCIES/le11_dependencies.txt
# - FORMS/LE11/UI_SCREENSHOTS/*.png
```

### 2. Generate PRD for New Form

```bash
# Terminal 1: Start worker
python -m src.worker.temporal_worker

# Terminal 2: Generate PRD
prd-agent generate -f le11 -o ./output

# Check results
ls ./output/le11/
cat ./output/le11/prd.md
```

### 3. Migrate Form to Modern Stack

```bash
# Generate PRD first (populates knowledge base)
prd-agent generate -f le11 -o ./output

# Run agentic migration
prd-agent migrate-agentic -f le11 -o ./output/agentic -v

# Check generated code
ls ./output/agentic/backend/
ls ./output/agentic/frontend/
```

### 4. Search and Explore Knowledge Base

```bash
# List what's available
prd-agent list-collections

# Get stats
prd-agent stats -f le11

# Search for specific logic
prd-agent search -f le11 -q "validation rules" -l 10
prd-agent search -f le11 -q "database operations" -t code
```

### 5. Clean Up After Testing

```bash
# Delete specific form
prd-agent delete-collection -f le11 --yes

# Or delete everything
prd-agent delete-bucket --bucket metadatas --yes
```

---

## Performance Tips

### Use Cache for Faster Results

Cache automatically speeds up:

- ✅ Repeated LLM calls (3-5s → 100ms)
- ✅ Vector searches (500ms → 50ms)
- ✅ Tool executions (1-2s → 50ms)

Check cache effectiveness:

```bash
prd-agent cache-stats
```

### Monitor Progress

```bash
# View Temporal UI for workflow progress
open http://localhost:8080

# Use verbose mode for detailed output
prd-agent migrate-agentic -f le11 -v
```

---

## All Available Commands

| Command                | Description                        |
| ---------------------- | ---------------------------------- |
| `generate`             | Generate PRD from legacy code      |
| `migrate-agentic`      | Migrate code with AI agents        |
| `list-collections`     | List all vector collections        |
| `stats`                | Get collection statistics          |
| `search`               | Search knowledge base              |
| `delete-collection`    | Delete collection and form data    |
| `create-minio-folders` | Create base MinIO folder structure |
| `create-form-folders`  | Create form-specific folders       |
| `delete-bucket`        | Delete entire MinIO bucket         |
| `cache-stats`          | Show cache statistics              |
| `cache-clear`          | Clear cache entries                |
| `version`              | Show version information           |

---

## Environment Variables

**Required:**

```bash
# LLM Provider (openai or anthropic)
LLM_PROVIDER=anthropic
ANTHROPIC_API_KEY=sk-ant-your-key-here

# Or OpenAI
LLM_PROVIDER=openai
OPENAI_API_KEY=sk-your-key-here

# Embeddings (always use OpenAI)
EMBEDDING_PROVIDER=openai
```

**Optional** (with defaults):

```bash
# Qdrant
QDRANT_HOST=localhost
QDRANT_PORT=6333

# Temporal
TEMPORAL_HOST=localhost
TEMPORAL_PORT=7233

# MinIO
MINIO_ENDPOINT=localhost:9000
MINIO_ACCESS_KEY=minioadmin
MINIO_SECRET_KEY=minioadmin
MINIO_BUCKET=metadatas

# Cache (uses Temporal PostgreSQL)
CACHE_ENABLED=true
CACHE_HOST=localhost
CACHE_PORT=5432
CACHE_DATABASE=temporal
CACHE_USER=temporal
CACHE_PASSWORD=temporal
```

---

## Notes

- **Temporal Worker**: Must be running for `generate` command
- **Knowledge Base**: Run `generate` before `migrate-agentic`
- **MinIO Structure**: Form names are UPPERCASE in paths
- **Cache**: Uses existing PostgreSQL (no extra infrastructure)
- **Vector DB**: Collections are named `prd_agent_{form_name}`

---

✅ All commands tested and working!
