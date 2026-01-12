# Hamal Deployment Guide

## Overview
Hamal is deployed as a full-stack application on Render:
1. **Backend**: Python Web Service (FastAPI) running the agent orchestrator.
2. **Frontend**: Static Site (React/Vite) serving the UI.

## Render Configuration (`render.yaml`)
The project includes a `render.yaml` blueprint that deploys both services automatically and links them.

### Services
1. **hamal-backend** (Web Service)
   - Build: `pip install -r requirements.txt`
   - Start: `python hamal.py serve --host 0.0.0.0 --port $PORT`
   - Health Check: `/health`

2. **hamal-ui** (Static Site)
   - Build: `cd ui && npm install && npm run build`
   - Publish: `ui/dist`
   - **Auto-Configuration**: The `VITE_API_URL` environment variable is automatically set to the backend's URL.

## Environment Variables
The following environment variables must be set in the Render Dashboard:

| Variable | Description | Required |
|----------|-------------|----------|
| `ANTHROPIC_API_KEY` | For Claude 3 models | Yes |
| `OPENAI_API_KEY` | For OpenAI models (if used) | Yes |
| `TAVILY_API_KEY` | For web search capabilities | Yes |
| `PYTHON_VERSION` | Python runtime version (3.11+) | Yes |

## Manual Deployment Steps
1. Push code to GitHub `main` branch.
2. Log in to Render.
3. Select **New +** -> **Blueprint**.
4. Connect the repository.
5. Render will detect `render.yaml` and prompt for environment variables.
6. Deployment will proceed automatically.

## Verification
Once deployed, verify the service is running:
```bash
curl https://<your-service-url>.onrender.com/health
# Expected: {"status": "ok", "service": "hamal-backend"}
```

## Rollback
To rollback to a previous version:
1. Go to the Service Dashboard on Render.
2. Click **History**.
3. Find the last successful deploy.
4. Click **Rollback**.
