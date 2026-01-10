# Operations & Security

## Security
*   **Secrets**: NEVER commit `.env` files. Ensure they are in `.gitignore`.
*   **API Keys**: verify `GROQ_API_KEY` and others are loaded from environment variables.
*   **Sanitization**: Validate all incoming Pydantic models.

## Deployment (Render)
*   **Config**: Maintain `render.yaml` as the source of truth for infrastructure.
*   **Build Command**: Verify `pip install -r requirements.txt` is present/correct.
*   **Start Command**: Ensure `uvicorn` binds to `0.0.0.0` and uses `$PORT`.
