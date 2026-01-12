# Hamal Setup Guide

Complete installation and configuration instructions for the Hamal AI validation framework.

***

## Prerequisites

- **Python:** 3.11 or higher
- **pip:** Latest version
- **Git:** For cloning the repository
- **API Keys:** Anthropic, Tavily (required); OpenRouter, Google Cloud (optional)

***

## Installation

### 1. Clone Repository

```bash
git clone <repository-url>
cd hamal
```

### 2. Create Virtual Environment

```bash
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

**Core dependencies:**
- `litellm` - Unified LLM interface
- `anthropic` - Claude API client
- `tavily-python` - Web search
- `python-dotenv` - Environment configuration
- `pydantic` - Data validation

***

## LiteLLM Configuration

Hamal uses [LiteLLM](https://docs.litellm.ai/) for unified LLM access across multiple providers.

### Supported Providers

| Provider | Models | Use Case |
|----------|--------|----------|
| **Anthropic** | Claude Sonnet 4, Claude Opus 4 | Primary reasoning (default) |
| **OpenRouter** | GPT-4, Claude, Gemini | Fallback/testing |
| **Vertex AI** | Gemini Pro, Claude via GCP | Enterprise deployments |
| **Gemini** | Gemini 1.5 Pro/Flash | Cost optimization |

### Provider Setup

#### Anthropic (Required)

1. Get API key: https://console.anthropic.com/
2. Add to `.env`:
   ```bash
   ANTHROPIC_API_KEY=sk-ant-api03-...
   ```

**Supported models:**
- `claude-sonnet-4-20250514` (default)
- `claude-opus-4-20250514`
- `claude-3-5-sonnet-20241022`

#### Tavily (Required)

1. Get API key: https://tavily.com/
2. Add to `.env`:
   ```bash
   TAVILY_API_KEY=tvly-...
   ```

#### OpenRouter (Optional)

1. Get API key: https://openrouter.ai/
2. Add to `.env`:
   ```bash
   OPENROUTER_API_KEY=sk-or-v1-...
   ```

**Available models:**
- `openrouter/anthropic/claude-sonnet-4`
- `openrouter/openai/gpt-4-turbo`
- `openrouter/google/gemini-pro-1.5`

#### Vertex AI (Optional - Enterprise)

1. Create GCP project: https://console.cloud.google.com/
2. Enable Vertex AI API
3. Create service account with Vertex AI User role
4. Download JSON key
5. Add to `.env`:
   ```bash
   GOOGLE_CLOUD_PROJECT=your-project-id
   GOOGLE_APPLICATION_CREDENTIALS=/path/to/service-account.json
   VERTEX_PROJECT=your-project-id
   VERTEX_LOCATION=us-central1
   ```

**Available models:**
- `vertex_ai/gemini-1.5-pro`
- `vertex_ai/claude-sonnet-4@20250514`

#### Gemini (Optional)

1. Get API key: https://makersuite.google.com/app/apikey
2. Add to `.env`:
   ```bash
   GEMINI_API_KEY=AIza...
   ```

**Available models:**
- `gemini/gemini-1.5-pro`
- `gemini/gemini-1.5-flash`

***

## Environment Configuration

### 1. Copy Template

```bash
cp .env.example .env
```

### 2. Edit `.env`

```bash
# Required
ANTHROPIC_API_KEY=sk-ant-api03-...
TAVILY_API_KEY=tvly-...

# Optional (choose one or more)
OPENROUTER_API_KEY=sk-or-v1-...
GEMINI_API_KEY=AIza...

# Optional (Vertex AI)
GOOGLE_CLOUD_PROJECT=your-project-id
GOOGLE_APPLICATION_CREDENTIALS=/path/to/key.json
VERTEX_PROJECT=your-project-id
VERTEX_LOCATION=us-central1

# Optional (model override)
DEFAULT_MODEL=claude-sonnet-4-20250514
```

### 3. Verify Configuration

```bash
python test_litellm.py
```

**Expected output:**
```
✅ LiteLLM configured successfully
✅ Anthropic API key valid
✅ Tavily API key valid
Model: claude-sonnet-4-20250514
```

***

## Model Selection

### Default Model

Hamal uses `claude-sonnet-4-20250514` by default. Override in `.env`:

```bash
DEFAULT_MODEL=claude-opus-4-20250514
```

### Per-Agent Override

Edit `agents/utils.py`:

```python
DEFAULT_MODEL = "claude-sonnet-4-20250514"  # Change here
```

### Runtime Override

Pass model to `call_llm()`:

```python
from agents.utils import call_llm

response = call_llm(
    model="claude-opus-4-20250514",  # Override
    messages=[{"role": "user", "content": "..."}]
)
```

***

## Verification

### Test Individual Components

```bash
# Test LiteLLM connection
python test_litellm.py

# Test Discovery Agent
python agents/discovery.py data/test_charter.txt

# Test full pipeline
python hamal.py run data/ranger_charter.txt
```

### Expected Directory Structure

```
hamal/
├── .env                    # Your API keys (gitignored)
├── .env.example            # Template
├── agents/
│   ├── discovery.py
│   ├── research.py
│   ├── validation.py
│   ├── architecture.py
│   ├── summary.py
│   └── utils.py            # LiteLLM wrapper
├── data/
│   ├── projects.json       # Project history
│   └── test_charter.txt
├── outputs/                # Generated reports
└── hamal.py                # Main orchestrator
```

***

## Troubleshooting

See [TROUBLESHOOTING.md](TROUBLESHOOTING.md) for common errors and solutions.

**Quick fixes:**
- `ModuleNotFoundError: No module named 'litellm'` → Run `pip install -r requirements.txt`
- `AuthenticationError` → Check API keys in `.env`
- `Model not found` → Verify model name in `agents/utils.py`

***

## Next Steps

1. ✅ Complete setup
2. 📖 Read [USAGE.md](USAGE.md) for CLI examples
3. 🚀 Run your first validation: `python hamal.py run data/ranger_charter.txt`
