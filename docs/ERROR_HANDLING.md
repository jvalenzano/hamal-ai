# Error Handling Implementation - Quick Reference

## New CLI Flags

```bash
# Enable verbose logging
python hamal.py run charter.txt --verbose

# Continue pipeline even if an agent fails
python hamal.py run charter.txt --skip-on-error

# Combine both
python hamal.py run charter.txt --verbose --skip-on-error
```

## Key Features

### 1. Automatic Retry Logic
- **Max attempts**: 3
- **Backoff**: Exponential (1s → 2s → 4s)
- **Handles**: Rate limits, timeouts, network errors

### 2. Graceful Tavily Degradation
- Returns empty results instead of crashing
- Pipeline continues with LLM-only analysis

### 3. Error Tracking
All errors logged to `state.json`:
```json
{
  "errors": [
    {
      "agent": "discovery",
      "error": "...",
      "timestamp": "..."
    }
  ]
}
```

## Testing

```bash
# Activate venv first
cd .
source venv/bin/activate

# Run test script
python test_error_handling.py

# Test with real charter
python hamal.py run data/ranger_charter.txt --verbose
```

## Files Modified

1. `agents/utils.py` - Retry decorator, error types, Tavily wrapper
2. `agents/discovery.py` - Safe Tavily search, error handling
3. `agents/research.py` - Safe Tavily search, JSON parsing
4. `agents/validation.py` - File read error handling
5. `agents/architecture.py` - File read error handling
6. `hamal.py` - Per-agent error handling, --verbose, --skip-on-error

## Error Types

- **FatalError**: Invalid API key, auth failures → No retry
- **RetryableError**: Rate limits, timeouts → Auto-retry
- **Tavily failures**: Graceful degradation → Continue with empty results
