# Migrating Hamal to Google Cloud Platform (GCP)

## Overview
This guide documents how to "graduate" Hamal from a Render POC to a production-grade containerized application on Google Cloud Platform (GCP).

**Target Architecture**: Google Cloud Run (Serverless Containers).
**Why Cloud Run?**: It behaves exactly like Render (scales to zero, stateless, HTTP-based) but runs inside your private GCP VPC with enterprise security.

---

## Phase 1: Containerization (The Code)
Render guesses how to run your app. On GCP, we must be explicit. You need to verify a `Dockerfile` in the root of your project.

### 1. Create `Dockerfile`
Create a file named `Dockerfile` (no extension) in the project root:

```dockerfile
# Use an official Python runtime with a smaller footprint
FROM python:3.11-slim

# Set the working directory in the container
WORKDIR /app

# 1. Install System Dependencies (GLib/GCC needed for some Python libs)
# We install these before python packages to cache this layer
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# 2. Install Python Dependencies
# Copy requirements first to leverage Docker Layer Caching
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 3. Copy Application Code
COPY . .

# 4. Configuration
# Cloud Run injects the PORT env var (usually 8080)
ENV PORT=8080
EXPOSE 8080

# 5. Start the Application
# Matches your Render Start Command
CMD exec uvicorn hamal:app --host 0.0.0.0 --port ${PORT}
```

---

## Phase 2: Infrastructure (The Cloud)

### 1. Enable APIs
You (or your DevOps team) need to enable these services in the GCP Console:
*   **Artifact Registry API**: To store the Docker image.
*   **Cloud Run API**: To run the container.

### 2. Create an Artifact Repository
```bash
gcloud artifacts repositories create hamal-repo \
    --repository-format=docker \
    --location=us-central1 \
    --description="Docker repository for Hamal"
```

---

## Phase 3: Deployment (The Action)

### 1. Build & Push
Instead of pushing to GitHub, you submit the build to GCP.

```bash
# Submit build to Cloud Build
gcloud builds submit --tag us-central1-docker.pkg.dev/[PROJECT_ID]/hamal-repo/hamal:v1 .
```

### 2. Deploy to Cloud Run
```bash
gcloud run deploy hamal-service \
    --image us-central1-docker.pkg.dev/[PROJECT_ID]/hamal-repo/hamal:v1 \
    --platform managed \
    --region us-central1 \
    --allow-unauthenticated \  # REMOVE this for internal-only apps
    --set-env-vars ANTHROPIC_API_KEY=...,OPENAI_API_KEY=...
```

---

## Phase 4: Production Refinements

### 1. Secrets Management
**DO NOT** pass API keys in the deployment command (like above).
**Instead**:
1.  Use **Secret Manager**.
2.  Mount secrets into Cloud Run.
3.  Update code to read from mounted paths if necessary (though env vars are usually fine).

### 2. CI/CD (GitHub Actions)
For a real "TechTrend" workflow, you wouldn't run commands manually. You would create a `.github/workflows/deploy.yaml` that runs `gcloud run deploy` whenever you push to `main`.
