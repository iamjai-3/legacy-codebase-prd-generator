# PRD Agent Commands Reference

Complete command reference for PRD Agent.

---

## 1. Infrastructure Setup

### Start All Services

```bash
cd /Users/jai-d3v/Projects/Optisol/Valosoft/PRD_Agent
docker-compose up -d
```

### Verify Services

```bash
docker-compose ps
```

### Stop Services

```bash
docker-compose down
```

---

## 2. Environment Setup

### Create and Activate Virtual Environment

```bash
cd /Users/jai-d3v/Projects/Optisol/Valosoft/PRD_Agent
python3.12 -m venv venv
source venv/bin/activate
pip install -e .
```

### Configure Environment

```bash
cp env.example .env
# Edit .env and set OPENAI_API_KEY=sk-your-key-here
```

---

## 3. Start Temporal Worker

Run in a separate terminal:

```bash
cd /Users/jai-d3v/Projects/Optisol/Valosoft/PRD_Agent
source venv/bin/activate
python -m src.worker.temporal_worker
```

---

## 4. Generate PRD

### Basic Command (Using MinIO)

Automatically loads legacy codebase from `LEGACY_CODEBASE/` in MinIO:

```bash
prd-agent generate \
  --form-name le11 \
  --output ./output
```

### With Local ZIP File

```bash
prd-agent generate \
  --form-name le11 \
  --zip-path ./code.zip \
  --output ./output
```

### With Local Code Directory

```bash
prd-agent generate \
  --form-name le11 \
  --code-dir ./src/code \
  --output ./output
```

### Full Command with All Options

```bash
prd-agent generate \
  --form-name le11 \
  --zip-path ./code.zip \
  --bucket metadatas \
  --jira-project PROJECT \
  --output ./output
```

**Options:**
- `--form-name, -f` (required): Form name (e.g., le11, le07)
- `--zip-path, -z` (optional): Path to code ZIP file (if not provided, loads from MinIO `LEGACY_CODEBASE/`)
- `--code-dir, -c` (optional): Path to code directory (if not provided, loads from MinIO `LEGACY_CODEBASE/`)
- `--output, -o` (default: `./output`): Output directory for PRD
- `--bucket, -b` (optional): MinIO bucket name
- `--jira-project, -j` (optional): Jira project key

**What happens automatically:**
- Dependencies loaded from MinIO: `FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/{FORM_NAME}_dependencies.txt`
- Database analysis runs automatically
- Screenshots analyzed from MinIO: `FORMS/{FORM_NAME}/UI_SCREENSHOTS/`
- Jira issues analyzed if project key provided

---

## 5. Code Migration

### Basic Migration

```bash
prd-agent migrate-code \
  --form-name le11 \
  --output ./output/migratedCode
```

**Note:** Run `generate` first to populate the knowledge base, then run `migrate-code`.

---

## 6. Vector Store Commands

### List All Collections

```bash
prd-agent list-collections
```

### Get Collection Statistics

```bash
prd-agent stats --form-name le11
```

### Search Knowledge Base

```bash
prd-agent search --form-name le11 --query "validation rules" --limit 10
```

### Search with Document Type Filter

```bash
prd-agent search --form-name le11 --query "user flow" --type code
prd-agent search --form-name le11 --query "UI components" --type screenshot
prd-agent search --form-name le11 --query "requirements" --type jira
```

### Delete Collection

```bash
prd-agent delete-collection --form-name le11 --yes
```

**Options:**
- `--form-name, -f` (required): Form name to delete
- `--yes, -y`: Skip confirmation prompt
- `--delete-minio` (default: true): Also delete MinIO form data
- `--no-delete-minio`: Skip MinIO deletion, only delete Qdrant collection
- `--bucket, -b`: MinIO bucket name (defaults to configured bucket)

**What gets deleted:**
- Qdrant vector collection: `prd_agent_{form_name}`
- MinIO form data: `FORMS/{FORM_NAME}/*` (if `--delete-minio` is used)

---

## 7. MinIO Folder Management

### Create Base Folder Structure

```bash
prd-agent create-minio-folders
```

### Create Folders for Specific Form

```bash
prd-agent create-form-folders LE11
```

### Custom Bucket

```bash
prd-agent create-minio-folders --bucket metadatas
prd-agent create-form-folders LE11 --bucket metadatas
```

**Folder Structure:**
- `FORMS/` - Parent folder for all forms
- `FORMS/{FORM_NAME}/FORM_DOCS/` - Form documentation files
- `FORMS/{FORM_NAME}/FORM_FILE_DEPENDENCIES/` - Dependency files
- `FORMS/{FORM_NAME}/UI_SCREENSHOTS/` - UI screenshots
- `DB_PRD/` - Database PRD files
- `EXPORT_CODEBASE_PRD/` - Export codebase PRD files
- `LEGACY_CODEBASE/` - Legacy codebase ZIP files

**Note:** Folders are automatically created when running `generate` if they don't exist.

---

## 8. Delete Commands

### Delete Collection and MinIO Form Data

```bash
prd-agent delete-collection --form-name le11 --yes
```

### Delete Only Qdrant Collection (Keep MinIO Data)

```bash
prd-agent delete-collection --form-name le11 --yes --no-delete-minio
```

### Delete Entire MinIO Bucket

⚠️ **WARNING**: This deletes the entire bucket and ALL data for ALL forms!

```bash
prd-agent delete-bucket --bucket metadatas --yes
```

**Options:**
- `--bucket, -b`: Bucket name (defaults to configured bucket)
- `--yes, -y`: Skip confirmation prompt
- `--force` (default: true): Delete all objects before deleting bucket
- `--no-force`: Only delete bucket if empty

---

## 9. Utility Commands

### Check Version

```bash
prd-agent version
```

### Show Help

```bash
prd-agent --help
prd-agent generate --help
```

---

## 10. Web UIs

### Temporal UI (Workflow Monitoring)

```bash
open http://localhost:8080
```

### MinIO Console

```bash
open http://localhost:9001
# Login: minioadmin / minioadmin
```

### Qdrant Dashboard

```bash
open http://localhost:6333/dashboard
```

---

## 11. Troubleshooting

### Test Temporal Connection

```bash
python -c "
import asyncio
from temporalio.client import Client

async def test():
    client = await Client.connect('localhost:7233')
    print('Connected to Temporal successfully!')

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

### Check OpenAI API Key

```bash
python -c "
from src.config.settings import get_settings
settings = get_settings()
print(f'API Key configured: {bool(settings.openai.api_key)}')
print(f'Model: {settings.openai.model}')
"
```

---

## Quick Reference

### Most Common Commands

```bash
# Generate PRD (using MinIO)
prd-agent generate -f le11 -o ./output

# Generate PRD (with local ZIP)
prd-agent generate -f le11 -z ./code.zip -o ./output

# Migrate code
prd-agent migrate-code -f le11 -o ./output/migratedCode

# Search knowledge base
prd-agent search -f le11 -q "validation rules"

# Delete collection
prd-agent delete-collection -f le11 --yes
```
