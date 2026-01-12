# Hamal TechTrend Troubleshooting

Common errors and solutions for the Hamal AI validation framework.

***

## Installation Issues

### `ModuleNotFoundError: No module named 'litellm'`

**Cause:** Dependencies not installed or wrong Python environment

**Solution:**
```bash
# Activate virtual environment
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Reinstall dependencies
pip install -r requirements.txt

# Verify installation
python -c "import litellm; print(litellm.__version__)"
```

### `ImportError: cannot import name 'completion' from 'litellm'`

**Cause:** Outdated litellm version

**Solution:**
```bash
pip install --upgrade litellm
```

***

## API Key Issues

### `AuthenticationError: Invalid API key`

**Cause:** Missing or incorrect API key in `.env`

**Solution:**
```bash
# Check .env file exists
ls -la .env

# Verify API key format
cat .env | grep ANTHROPIC_API_KEY

# Anthropic keys start with: sk-ant-api03-
# Tavily keys start with: tvly-
# OpenRouter keys start with: sk-or-v1-
```

**Test API keys:**
```bash
python test_litellm.py
```

### `Error: ANTHROPIC_API_KEY not found`

**Cause:** `.env` file not loaded or missing

**Solution:**
```bash
# Create .env from template
cp .env.example .env

# Edit with your keys
nano .env  # or vim, code, etc.

# Verify environment loading
python -c "from dotenv import load_dotenv; import os; load_dotenv(); print(os.getenv('ANTHROPIC_API_KEY'))"
```

***

## Model Errors

### `litellm.exceptions.NotFoundError: model claude-3-5-sonnet-20241022 does not exist`

**Cause:** Invalid model name or typo

**Solution:**

Check `agents/utils.py` for correct model name:

```python
# ❌ Wrong
DEFAULT_MODEL = "claude-3-5-sonnet-20241022"

# ✅ Correct
DEFAULT_MODEL = "claude-sonnet-4-20250514"
```

**Valid Anthropic models:**
- `claude-sonnet-4-20250514`
- `claude-opus-4-20250514`
- `claude-3-5-sonnet-20241022` (legacy)

### `Model not supported by provider`

**Cause:** Using provider-specific model with wrong prefix

**Solution:**

```python
# Anthropic (direct)
model = "claude-sonnet-4-20250514"

# OpenRouter (requires prefix)
model = "openrouter/anthropic/claude-sonnet-4"

# Vertex AI (requires prefix)
model = "vertex_ai/claude-sonnet-4@20250514"

# Gemini (requires prefix)
model = "gemini/gemini-1.5-pro"
```

***

## Pipeline Errors

### Pipeline hangs at "Discovery Agent: Interrogating problem..."

**Cause:** API timeout or network issue

**Solution:**
```bash
# Check API connectivity
curl -I https://api.anthropic.com

# Test with minimal example
python test_litellm.py

# Check for rate limits
# Anthropic: 50 requests/min (Tier 1)
# Tavily: 1000 requests/month (free tier)
```

### `FileNotFoundError: [Errno 2] No such file or directory: 'outputs/...'`

**Cause:** Output directory not created

**Solution:**
```bash
# Create outputs directory
mkdir -p outputs

# Run pipeline again
python hamal.py run data/peace-corps-charter.txt
```

### `JSONDecodeError: Expecting value: line 1 column 1 (char 0)`

**Cause:** LLM returned non-JSON response (common with fallback parsing)

**This is expected behavior** - agents use fallback text parsing when JSON fails.

**To reduce noise:**
```python
# In agents/*.py, the code already handles this:
try:
    data = json.loads(response_text)
except json.JSONDecodeError:
    # Fallback to text parsing (this is normal)
    pass
```

***

## Agent-Specific Errors

### Discovery Agent: "Search error for '...': 401 Unauthorized"

**Cause:** Invalid Tavily API key

**Solution:**
```bash
# Check Tavily key
cat .env | grep TAVILY_API_KEY

# Get new key: https://tavily.com/
# Add to .env:
TAVILY_API_KEY=tvly-...
```

### Research Agent: "No similar projects found"

**Cause:** `data/projects.json` missing or empty

**Solution:**
```bash
# Verify file exists
ls -lh data/projects.json

# Should contain TechTrend project history
# If missing, create minimal version:
echo '{"projects": []}' > data/projects.json
```

### Validation Agent: "KeyError: 'problem_statement'"

**Cause:** `problem.md` missing or malformed

**Solution:**
```bash
# Check problem.md exists
cat outputs/peace-corps-charter/problem.md

# Re-run Discovery Agent
python agents/discovery.py data/peace-corps-charter.txt
```

### Architecture Agent: "No matching projects in database"

**Cause:** Empty `data/projects.json`

**This is expected** for first run - agent will use TechTrend defaults.

### Summary Agent: "Missing required file: validation.md"

**Cause:** Previous agent failed

**Solution:**
```bash
# Check pipeline status
python hamal.py status outputs/peace-corps-charter/

# Re-run missing agents
python agents/validation.py outputs/peace-corps-charter/
python agents/summary.py outputs/peace-corps-charter/
```

***

## Performance Issues

### Pipeline takes >15 minutes

**Expected runtime:** 8-12 minutes for full pipeline

**Causes:**
1. Using `claude-opus-4` (slower, higher quality)
2. Network latency
3. Tavily search timeouts

**Solutions:**
```python
# Switch to faster model
DEFAULT_MODEL = "claude-sonnet-4-20250514"  # Faster

# Or use Gemini for speed
DEFAULT_MODEL = "gemini/gemini-1.5-flash"  # Fastest
```

### High API costs

**Expected cost:** ~$1.00 per validation (Claude Sonnet 4)

**Cost optimization:**
```python
# Use Gemini for testing
DEFAULT_MODEL = "gemini/gemini-1.5-pro"  # ~$0.20 per run

# Or cache results
# Hamal automatically skips completed agents via state.json
```

***

## Output Quality Issues

### Validation scores always 0/50

**Cause:** LLM parsing error in `validation.py`

**Debug:**
```bash
# Check raw validation.md
cat outputs/peace-corps-charter/validation.md

# Look for "Feasibility Score" section
# Should contain: Technical Complexity: X/10
```

**Fix:** Re-run with verbose logging:
```python
# In agents/validation.py, add:
print(f"DEBUG: Raw LLM response:\n{response_text}")
```

### Architecture costs unrealistic ($0 or $1M+)

**Cause:** LLM hallucination or missing context

**Solution:**
```bash
# Check data/projects.json has examples
cat data/projects.json | grep -A 5 "cost"

# Manually review architecture.md
cat outputs/peace-corps-charter/architecture.md
```

### Summary HTML not rendering charts

**Cause:** Missing Chart.js or malformed HTML

**Solution:**
```bash
# Check HTML file size
ls -lh outputs/peace-corps-charter/summary.html

# Should be >50KB with embedded Chart.js
# If <10KB, re-run summary agent:
python agents/summary.py outputs/peace-corps-charter/
```

***

## Environment Issues

### `Pydantic UserWarning: Valid config keys have changed in V2`

**This is a warning, not an error** - can be safely ignored.

**To suppress:**
```bash
export PYTHONWARNINGS="ignore::UserWarning"
python hamal.py run data/peace-corps-charter.txt
```

### `DeprecationWarning: pkg_resources is deprecated`

**This is a warning from dependencies** - does not affect functionality.

**To suppress:**
```bash
pip install --upgrade setuptools
```

***

## Debugging Tips

### Enable verbose logging

```python
# In agents/utils.py, add:
import logging
logging.basicConfig(level=logging.DEBUG)
```

### Test LiteLLM directly

```python
from litellm import completion

response = completion(
    model="claude-sonnet-4-20250514",
    messages=[{"role": "user", "content": "Hello"}]
)
print(response.choices[0].message.content)
```

### Check state.json

```bash
# View pipeline state
cat outputs/peace-corps-charter/state.json | python -m json.tool
```

### Clear cache and retry

```bash
# Remove outputs and start fresh
rm -rf outputs/peace-corps-charter/
python hamal.py run data/peace-corps-charter.txt
```

***

## Getting Help

### Check logs

```bash
# Run with verbose output
python hamal.py run data/peace-corps-charter.txt 2>&1 | tee hamal.log
```

### Minimal reproducible example

```bash
# Test with minimal charter
echo "Test problem: Agency needs chatbot" > data/test.txt
python agents/discovery.py data/test.txt
```

### Report issues

Include:
1. Error message (full traceback)
2. `.env` contents (redact API keys)
3. Python version: `python --version`
4. LiteLLM version: `pip show litellm`
5. Command that failed

***

## Known Limitations

1. **No streaming:** Agents wait for full LLM response (8-30s per call)
2. **No retry logic:** API failures require manual re-run
3. **No parallel execution:** Agents run sequentially
4. **No caching:** Each run makes fresh API calls (except via state.json)

**These are POC limitations** - will be addressed in production version.

***

## Quick Checklist

Before reporting an issue:

- [ ] Activated virtual environment (`source venv/bin/activate`)
- [ ] Installed dependencies (`pip install -r requirements.txt`)
- [ ] Created `.env` with valid API keys
- [ ] Tested API keys (`python test_litellm.py`)
- [ ] Verified model name in `agents/utils.py`
- [ ] Checked `outputs/` directory exists
- [ ] Reviewed error message carefully
- [ ] Tried clearing cache (`rm -rf outputs/...`)
