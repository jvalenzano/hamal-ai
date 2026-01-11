# Hamal AI: Deployment Guide

## 1. Backend Deployment (Render.com)
**Context:** You are on the Render Dashboard. You have a `render.yaml` file in your repo.

1.  **Select "Blueprint":** In the "+ New" dropdown (from your screenshot), click the last option: **Blueprint**.
2.  **Connect GitHub:**
    *   Click "Connect GitHub" / "Authorize Render".
    *   Select the repo: `jvalenzano/hamal-ai`.
3.  **Configure:**
    *   Render will automatically detect the `hamal-api` service from our `render.yaml`.
    *   You will see a field for `GROQ_API_KEY`.
    *   **Action:** Paste your Groq API Key there.
4.  **Deploy:**
    *   Click **"Apply Blueprint"**.
    *   Wait ~2 minutes. You will see "Service is live".
    *   **Copy the URL:** It will look like `https://hamal-api-xyz.onrender.com`.

## 2. Frontend Deployment (Vercel)
**Context:** I installed the Vercel CLI. If you ran `vercel login`, I can do this for you. Otherwise, use the UI:

1.  Go to [vercel.com/new](https://vercel.com/new).
2.  Import `jvalenzano/hamal-ai`.
3.  **Root Directory:** Click "Edit" and select `frontend`.
4.  **Environment Variables:**
    *   Name: `VITE_API_URL`
    *   Value: `[PASTE_YOUR_RENDER_URL_HERE]` (e.g., `https://hamal-api-xyz.onrender.com`)
    *   *Note: Do not add /analyze at the end, just the base URL.*
5.  Click **Deploy**.

## 3. Verification
Once both are live:
1.  Open your Vercel URL.
2.  Type a startup idea.
3.  Click "Validate".
4.  See the Risk Score 🚀.
