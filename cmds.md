# PRD Agent Commands Reference

Complete command reference for setting up and running PRD Agent.

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

### Full Cleanup (Remove Volumes)

```bash
docker-compose down -v
```

---

## 2. Virtual Environment

### Create Virtual Environment

```bash
cd /Users/jai-d3v/Projects/Optisol/Valosoft/PRD_Agent
/Users/jai-d3v/.local/bin/python3.12 -m venv venv
```

### Activate Virtual Environment

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -e .
```

### Deactivate

```bash
deactivate
```

---

## 3. Environment Configuration

### Copy Environment File

```bash
cp env.example .env
```

### Edit Environment (add your OpenAI API key)

```bash
nano .env
# or
code .env
```

**Required:** Set `OPENAI_API_KEY=sk-your-key-here`

---

## 4. Start Temporal Worker

Run in a separate terminal:

```bash
cd /Users/jai-d3v/Projects/Optisol/Valosoft/PRD_Agent
source venv/bin/activate
python -m src.worker.temporal_worker
```

---

## 5. Generate PRD Commands

### Full Generation (with Temporal workflow)

```bash
prd-agent generate \
  --form-name le01 \
  --zip-path /Users/jai-d3v/Projects/Optisol/Valosoft/oases-master.zip \
  --bucket screenshots \
  --jira-project OASES \
  --output ./output
```

### Skip Jira Integration

```bash
prd-agent generate \
  --form-name le01 \
  --zip-path ./src/templates_code_zip/ea01.zip \
  --bucket le07 \
  --output ./output \
  --skip-jira
```

### LE11 Full Command (with Database Analysis)

```bash
# Basic command (database analysis runs automatically)
prd-agent generate \
  -f le11 \
  -z src/templates_code_zip/oases-master.zip \
  -d src/form_dependencies/le11_dependencies.txt \
  -b le11 \
  -o ./output \
  --skip-jira

# With custom database documentation path
prd-agent generate \
  -f le11 \
  -z src/templates_code_zip/oases-master.zip \
  -d src/form_dependencies/le11_dependencies.txt \
  -b le11 \
  -o ./output \
  --skip-jira \
  --db-doc src/db_doc/Database_DOC.md

# Skip database analysis if needed
prd-agent generate \
  -f le11 \
  -z src/templates_code_zip/oases-master.zip \
  -d src/form_dependencies/le11_dependencies.txt \
  -b le11 \
  -o ./output \
  --skip-jira \
  --skip-db-analysis
```

### Skip Jira and Screenshots

```bash
prd-agent generate \
  --form-name le01 \
  --zip-path /Users/jai-d3v/Projects/Optisol/Valosoft/oases-master.zip \
  --output ./output \
  --skip-jira \
  --skip-screenshots
```

### Direct Mode (No Temporal Worker Needed)

```bash
prd-agent generate \
  --form-name le01 \
  --zip-path /Users/jai-d3v/Projects/Optisol/Valosoft/oases-master.zip \
  --output ./output \
  --skip-jira \
  --skip-screenshots \
  --direct
```

### With File Mappings

```bash
prd-agent generate \
  --form-name le01 \
  --zip-path /Users/jai-d3v/Projects/Optisol/Valosoft/oases-master.zip \
  --mappings "LE01Adapter.java,LE01Service.java,LE01Action.java" \
  --output ./output \
  --skip-jira \
  --direct
```

### Recreate Vector Collection

```bash
prd-agent generate \
  --form-name le01 \
  --zip-path /Users/jai-d3v/Projects/Optisol/Valosoft/oases-master.zip \
  --output ./output \
  --skip-jira \
  --skip-screenshots \
  --recreate-vectors \
  --direct
```

---

## 6. Vector Store Commands

### List All Collections

```bash
prd-agent list-collections
```

### Get Collection Statistics

```bash
prd-agent stats --form-name le01
```

### Search Knowledge Base

```bash
prd-agent search --form-name le01 --query "validation rules" --limit 10
```

### Search with Document Type Filter

```bash
prd-agent search --form-name le01 --query "user flow" --type code
prd-agent search --form-name le01 --query "UI components" --type screenshot
prd-agent search --form-name le01 --query "requirements" --type jira
```

### Delete Collection

```bash
prd-agent delete-collection --form-name le01 --yes
```

---

## 7. View Output

### List Generated Files

```bash
ls -la ./output/
```

### View PRD Markdown

```bash
cat ./output/le01_PRD.md
```

### Open in Editor

```bash
code ./output/le01_PRD.md
```

---

## 8. Web UIs

### Temporal UI (Workflow Monitoring)

```bash
open http://localhost:8080
```

### Minio Console (Screenshot Storage)

```bash
open http://localhost:9001
# Login: minioadmin / minioadmin
```

### Qdrant Dashboard (Vector Database)

```bash
open http://localhost:6333/dashboard
```

---

## 9. Quick Test Commands

### Minimal Test (Direct Mode, No External Dependencies)

```bash
cd /Users/jai-d3v/Projects/Optisol/Valosoft/PRD_Agent && \
source venv/bin/activate && \
prd-agent generate \
  --form-name le01 \
  --zip-path /Users/jai-d3v/Projects/Optisol/Valosoft/oases-master.zip \
  --output ./output \
  --skip-jira \
  --skip-screenshots \
  --direct
```

### Test with Sample ZIP

```bash
prd-agent generate \
  --form-name ea01 \
  --zip-path ./src/templates_code_zip/ea01.zip \
  --output ./output \
  --skip-jira \
  --skip-screenshots \
  --direct
```

---

## 10. Utility Commands

### Check Version

```bash
prd-agent version
```

### Show Help

```bash
prd-agent --help
prd-agent generate --help
```

### Check Python Version

```bash
python --version
```

### Check Installed Packages

```bash
pip list | grep -E "(langchain|qdrant|temporal)"
```

---

## 11. Docker Commands

### View Container Logs

```bash
docker-compose logs temporal
docker-compose logs qdrant
docker-compose logs minio
```

### Follow Logs in Real-time

```bash
docker-compose logs -f temporal
```

### Restart a Service

```bash
docker-compose restart qdrant
```

### Check Container Health

```bash
docker ps --format "table {{.Names}}\t{{.Status}}"
```

---

## 12. Code Migration Commands

### Basic Code Migration (with Database Analysis)

```bash
prd-agent migrate-code \
  --form-name le07 \
  --output ./output/migratedCode
```

### Code Migration with Custom Database Documentation

```bash
prd-agent migrate-code \
  --form-name le07 \
  --output ./output/migratedCode \
  --db-doc src/db_doc/Database_DOC.md
```

### Code Migration without Database Analysis

```bash
prd-agent migrate-code \
  --form-name le07 \
  --output ./output/migratedCode \
  --skip-db-analysis
```

### Short Form

```bash
prd-agent migrate-code -f le07 -o ./output/migratedCode
```

### Code Migration for LE11 (with dependencies)

```bash
prd-agent migrate-code \
  -f le11 \
  -o ./output/migratedCode \
  --db-doc src/db_doc/Database_DOC.md
```

**Note:** The database analysis step automatically:
- Analyzes database table mappings from `src/db_doc/Database_DOC.md`
- Extracts table structures, relationships, and schema mappings
- Stores database context in the knowledge base for enhanced code migration
- Provides complete context: business logic, database mappings, API flows

**Important:** Before running migrate-code, ensure you have:
1. Generated the PRD first (to populate the knowledge base):
```bash
prd-agent generate \
  -f le11 \
  -z src/templates_code_zip/oases-master.zip \
  -d src/form_dependencies/le11_dependencies.txt \
  -b le11 \
  -o ./output \
  --skip-jira
```
2. Then run code migration:
```bash
prd-agent migrate-code -f le11 -o ./output/migratedCode
```

---

## 13. Troubleshooting

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

### Test Minio Connection

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
