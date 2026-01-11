# Green Field Setup Plan: Hamal (Personal Cloud)

**Goal:** Initialize a brand new GCP Project, GitHub Repo, and Developer Environment for "Hamal" (The Founder's Brain).
**Tools:** `gcloud`, `gh`, `gemini-conductor`.

## 1. The Identity
*   **Project Name:** Hamal (The Head of the Ram)
*   **GCP Project ID:** `hamal-founder-brain-[RANDOM]`
*   **Repo Name:** `hamal-founder-brain`

## 2. Pre-Flight Checklist (User Actions Needed)
We cannot proceed without these 3 things:
1.  **Authentication:** You must be logged in to Google (`gcloud auth login`) and GitHub (`gh auth login`).
2.  **Billing ID:** We need your generic GCP Billing Account ID to link to the new project.
3.  **GitHub Token:** Ensure `gh` has permission to create private repos.

## 3. The Execution Script (I will run this)

### Phase 1: Cloud Foundation (GCP)
```bash
# 1. Create Project
gcloud projects create hamal-founder-brain-[RANDOM] --name="Hamal Founder Brain"

# 2. Link Billing (CRITICAL)
gcloud beta billing projects link hamal-founder-brain-[RANDOM] --billing-account=[YOUR_BILLING_ID]

# 3. Enable The Stack
gcloud services enable aiplatform.googleapis.com run.googleapis.com cloudbuild.googleapis.com firestore.googleapis.com artifactregistry.googleapis.com --project=hamal-founder-brain-[RANDOM]
```

### Phase 2: Code Foundation (GitHub)
```bash
# 1. Initialize Git
git init
git checkout -b main

# 2. Create Remote Repo
gh repo create hamal-founder-brain --private --source=. --description="Hamal: The AI-Native Founder's Brain"

# 3. Push Initial Commit
git add .
git commit -m "feat: Initial commit (Incubator OS Structure)"
git push -u origin main
```

### Phase 3: The "Conductor" (New Workflow)
```bash
# 1. Install Gemini CLI & Conductor
npm install -g @google/gemini-cli
gemini install conductor

# 2. Initialize Conductor
conductor setup
```

## 4. Next Steps
Once you provide the **Billing ID** and confirm **Auth**, I will:
1.  Generate a unique Project ID.
2.  Run the GCP setup.
3.  Run the GitHub setup.
4.  Install Conductor.
