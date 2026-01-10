---
description: Deploy Hamal AI to Render
---

1.  **Pre-flight Check**
    *   Run `npm run build` in `hamal-ai/frontend` to ensure build passes.
    *   Check `hamal-ai/render.yaml` for any uncommitted config changes.

2.  **Git Operations**
    *   Stage all changes: `git add .`
    *   Ask user for commit message.
    *   Commit and Push: `git commit -m "..." && git push origin main`

3.  **Post-Deployment**
    *   Remind user to check Render dashboard for build status.
