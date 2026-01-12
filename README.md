# Hamal: AI-Powered Validation Framework

**Version:** 0.1.0 (MVP)  
**Status:** Proof-of-Concept  
**Purpose:** Validate government AI project opportunities through autonomous agent research

***

## What is Hamal?

Hamal transforms rough agency requests into validated project specifications in 15-20 minutes. When an opportunity is received (e.g., "Forest Service needs post-fire AI"), Hamal:

1. **Discovery Agent:** Validates the core problem (5 Whys, stakeholder mapping)
2. **Research Agent:** Finds similar government projects, competitors, failures
3. **Validation Agent:** Scores feasibility (0-50), identifies risks
4. **Architecture Agent:** Generates stack recommendation, cost estimate, timeline
5. **Summary Agent:** Produces executive summary with visualizations (charts, metrics)

**Output:** Complete Design phase artifacts (problem.md, research.md, validation.md, architecture.md, summary.html)

***

## Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Configure API Keys

Hamal uses **LiteLLM**, so you have flexibility in which AI provider you use.

1. Copy the template:
   ```bash
   cp .env.example .env
   ```

2. Open `.env` and follow the detailed instructions inside. You only need **ONE** LLM provider key:
   - **Recommended:** `ANTHROPIC_API_KEY` (Best results with Claude 3.5 Sonnet)
   - **Alternative:** `OPENAI_API_KEY` (GPT-4o)
   - **Alternative:** `GEMINI_API_KEY` (Google Gemini 1.5)

3. Add your web search key (Required for research):
   - `TAVILY_API_KEY` (Get free key at tavily.com)

### 3. Run Discovery Agent (Test)

```bash
python agents/discovery.py data/test_charter.txt
```

### 4. Run Full Pipeline (After all agents built)

```bash
python hamal.py run data/ranger_charter.txt
```

***

## AI Provider Flexibility

Thanks to LiteLLM, Hamal isn't locked to one vendor. You can switch models by simply changing environment variables.

**Supported Providers:**
- **Anthropic** (Default) - Optimized for complex reasoning.
- **OpenAI** - Compatible with GPT-4 class models.
- **OpenRouter** - Access to Llama 3, Mistral, and others via single API.
- **Local (Ollama)** - Possible, but requires model override in `.env`.

**To switch models globally:**
In your `.env` file, uncomment and set `DEFAULT_MODEL`:

```bash
# Example: Switch to GPT-4o
DEFAULT_MODEL=gpt-4o
```

📖 **Detailed Setup:** See [docs/SETUP.md](docs/SETUP.md)

***

## Project Structure

- **agents/** - Individual agent implementations (discovery, research, validation, architecture, summary)
- **data/** - TechTrend project history, domain context, test inputs
- **outputs/** - Generated reports per validation run (outputs/project-name/)
- **tests/** - Test cases for agents
- **hamal.py** - Main orchestrator CLI

***

## Example Output

**Peace Corps Recruitment Chatbot Validation:**
- [Executive Summary (HTML)](outputs/peace-corps-demo-charter-v1.md/summary.html) - Interactive report with charts
- [Validation Report](outputs/peace-corps-demo-charter-v1.md/validation.md) - 25/50 CONDITIONAL GO
- [Architecture Spec](outputs/peace-corps-demo-charter-v1.md/architecture.md) - $101K, 12 weeks, detailed stack

***

## Development Philosophy

⚠️ **READ FIRST:** [KEEP_IT_SIMPLE.md](KEEP_IT_SIMPLE.md)

This is a POC to validate that agent swarms save time on Design phases. Our goal is to test agent prompts, not build production infrastructure.

**Core principles:**
- Use single-file Python scripts, hardcoded values, JSON files for storage
- No databases or auth until we prove agents work
- Ship ugly code weekly, iterate on prompts aggressively
- Functional > perfect. Speed > elegance. Learning > scaling.

***

## Testing

Hamal uses `pytest` for unit and integration testing. Tests are located in the `tests/` directory and use mocks to avoid real API calls.

### Run Tests Locally

```bash
# Run all tests
pytest

# Run with coverage report
pytest --cov=agents
```

Automated tests run on every push and pull request via GitHub Actions.

***

## Tech Stack

- **Language:** Python 3.11+
- **LLM Interface:** LiteLLM (unified API for Anthropic, OpenRouter, Gemini, Vertex AI)
- **Primary Model:** Claude Sonnet 4 (via Anthropic)
- **Web Search:** Tavily API
- **Storage:** Local JSON files (outputs/ directory)
- **UI:** React + Vite + TailwindCSS

***

## Success Metrics

**MVP is successful if:**
- [ ] Saves 5+ hours per Design phase (measurable via time tracking)
- [ ] Produces 3+ insights per project that AI Lead wouldn't find manually
- [ ] Runs on 3 different projects (RANGER, TrailWatch, 1 new)
- [ ] A2UI demonstrates real-time agent progress (not just loading spinner)

***

## Documentation

- 📖 [Setup Guide](docs/SETUP.md) - LiteLLM provider configuration
- 🚀 [Usage Guide](docs/USAGE.md) - CLI examples and workflows
- 🔧 [Troubleshooting](docs/TROUBLESHOOTING.md) - Common errors and solutions

***

## Contributing

This is an internal tool (for now). If you're a contributor:

1. Read `KEEP_IT_SIMPLE.md` first
2. Each agent is a self-contained Python file
3. Test on real projects (RANGER, TrailWatch)
4. Focus on prompt quality, not infrastructure

***

## License

Internal project. Not open source (yet).

***

**Contact:** AI Lead
