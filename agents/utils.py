
import os
import time
import functools
from litellm import completion
from dotenv import load_dotenv

load_dotenv()

# Centralized model configuration
DEFAULT_MODEL = os.getenv("LLM_MODEL", "claude-sonnet-4-20250514")
FAST_MODEL = os.getenv("LLM_FAST_MODEL", "claude-sonnet-4-5")

# Global verbose flag (set by CLI)
VERBOSE = False


# Custom Error Types
class RetryableError(Exception):
    """Transient errors that should be retried (rate limits, timeouts)"""
    pass


class FatalError(Exception):
    """Non-retryable errors (invalid API key, bad input)"""
    pass


def set_verbose(enabled: bool):
    """Set global verbose logging flag"""
    global VERBOSE
    VERBOSE = enabled


def log_verbose(message: str):
    """Log message if verbose mode is enabled"""
    if VERBOSE:
        print(f"[VERBOSE] {message}")


def retry_with_backoff(max_attempts=3, base_delay=1.0, max_delay=10.0):
    """
    Retry decorator with exponential backoff.
    
    Args:
        max_attempts: Maximum number of retry attempts (default: 3)
        base_delay: Initial delay in seconds (default: 1.0)
        max_delay: Maximum delay between retries (default: 10.0)
    """
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            attempt = 0
            delay = base_delay
            
            while attempt < max_attempts:
                try:
                    return func(*args, **kwargs)
                except FatalError:
                    # Don't retry fatal errors
                    raise
                except Exception as e:
                    attempt += 1
                    
                    # Check if error is retryable
                    error_str = str(e).lower()
                    is_retryable = any(keyword in error_str for keyword in [
                        'rate limit', 'timeout', 'connection', 'temporary', 
                        'service unavailable', '429', '503', '504',
                        'overloaded', 'internal server error'
                    ])
                    
                    # Check for fatal errors
                    is_fatal = any(keyword in error_str for keyword in [
                        'invalid api key', 'authentication', 'unauthorized', 
                        'invalid_api_key', '401', '403'
                    ])
                    
                    if is_fatal:
                        log_verbose(f"Fatal error detected: {e}")
                        raise FatalError(f"Fatal error: {e}") from e
                    
                    if not is_retryable or attempt >= max_attempts:
                        log_verbose(f"Non-retryable error or max attempts reached: {e}")
                        raise
                    
                    log_verbose(f"Attempt {attempt}/{max_attempts} failed: {e}")
                    log_verbose(f"Retrying in {delay:.1f}s...")
                    time.sleep(delay)
                    
                    # Exponential backoff
                    delay = min(delay * 2, max_delay)
            
            raise Exception(f"Max retry attempts ({max_attempts}) exceeded")
        
        return wrapper
    return decorator


def get_response_content(response):
    """
    Extract content from LiteLLM response.
    
    Args:
        response: LiteLLM response object
        
    Returns:
        str: The message content
    """
    return response.choices[0].message.content


@retry_with_backoff(max_attempts=3, base_delay=1.0, max_delay=10.0)
def call_llm(messages, system=None, model=None, temperature=0.7, max_tokens=4096):
    """
    Centralized LLM caller using LiteLLM with retry logic.
    
    Args:
        messages (list): List of message dicts (role/content).
        system (str): Optional system prompt.
        model (str): Optional model override. Defaults to DEFAULT_MODEL.
        temperature (float): Generation temperature.
        max_tokens (int): Max tokens to generate.
        
    Returns:
        Response object (LiteLLM/OpenAI format). 
        Use get_response_content(response) to extract text.
        
    Raises:
        FatalError: For non-retryable errors (auth, invalid key)
        RetryableError: For transient errors (rate limits, timeouts)
    """
    if not model:
        model = DEFAULT_MODEL
    
    log_verbose(f"Calling LLM: model={model}, messages={len(messages)}, max_tokens={max_tokens}")
    
    try:
        response = completion(
            model=model,
            messages=messages,
            system=system,
            temperature=temperature,
            max_tokens=max_tokens
        )
        log_verbose(f"LLM call successful")
        return response
    except Exception as e:
        error_msg = str(e)
        log_verbose(f"LLM call error: {error_msg}")
        
        # Classify error type for better error messages
        if any(keyword in error_msg.lower() for keyword in ['invalid api key', 'authentication', 'unauthorized']):
            raise FatalError(f"Authentication error - check your API key in .env: {error_msg}") from e
        elif any(keyword in error_msg.lower() for keyword in ['rate limit', '429']):
            raise RetryableError(f"Rate limit exceeded - will retry: {error_msg}") from e
        elif any(keyword in error_msg.lower() for keyword in ['timeout', 'connection']):
            raise RetryableError(f"Network error - will retry: {error_msg}") from e
        else:
            # Re-raise for retry logic to handle
            raise


@retry_with_backoff(max_attempts=3, base_delay=1.0, max_delay=10.0)
def call_tavily_search(tavily_client, query: str, max_results: int = 5):
    """
    Wrapper for Tavily search with retry logic and graceful degradation.
    
    Args:
        tavily_client: TavilyClient instance
        query: Search query string
        max_results: Maximum number of results to return
        
    Returns:
        dict: Search results or empty dict with error info on failure
    """
    log_verbose(f"Tavily search: query='{query}', max_results={max_results}")
    
    try:
        results = tavily_client.search(query, max_results=max_results)
        log_verbose(f"Tavily search successful: {len(results.get('results', []))} results")
        return results
    except Exception as e:
        error_msg = str(e)
        log_verbose(f"Tavily search error: {error_msg}")
        
        # Classify error type
        if any(keyword in error_msg.lower() for keyword in ['invalid api key', 'authentication', 'unauthorized']):
            raise FatalError(f"Tavily authentication error - check TAVILY_API_KEY in .env: {error_msg}") from e
        elif any(keyword in error_msg.lower() for keyword in ['rate limit', '429']):
            raise RetryableError(f"Tavily rate limit - will retry: {error_msg}") from e
        else:
            # Re-raise for retry logic
            raise


def safe_tavily_search(tavily_client, query: str, max_results: int = 5, fallback_empty: bool = True):
    """
    Safe Tavily search with graceful degradation.
    
    If Tavily fails after retries, returns empty results instead of crashing.
    
    Args:
        tavily_client: TavilyClient instance
        query: Search query string
        max_results: Maximum number of results
        fallback_empty: If True, return empty results on failure instead of raising
        
    Returns:
        dict: Search results or {"results": [], "error": "..."} on failure
    """
    try:
        return call_tavily_search(tavily_client, query, max_results)
    except Exception as e:
        error_msg = f"Tavily search failed for '{query}': {e}"
        log_verbose(error_msg)
        
        if fallback_empty:
            print(f"⚠️  {error_msg}")
            print(f"⚠️  Continuing with empty search results...")
            return {"results": [], "error": str(e)}
        else:
            raise


def clean_json_output(text: str) -> str:
    """
    Clean LLM output to extract just the JSON part.
    
    Removes:
    - Markdown code fences (e.g. ```json ... ```)
    - Introductory text
    - Trailing text
    
    Args:
        text (str): Raw output from LLM
        
    Returns:
        str: Cleaned JSON string
    """
    if not text:
        return ""
        
    # Strip whitespace
    text = text.strip()
    
    # Remove markdown code fences
    # Using simple replacements first to handle variations
    lines = text.split('\n')
    cleaned_lines = []
    
    for line in lines:
        if line.strip().startswith('```'):
            continue
        cleaned_lines.append(line)
        
    text = '\n'.join(cleaned_lines).strip()
    
    # Extract just the JSON object/array if there's extra text
    # Find first { or [
    first_brace = text.find("{")
    first_bracket = text.find("[")
    
    start_idx = -1
    end_char = ""
    
    if first_brace != -1 and (first_bracket == -1 or first_brace < first_bracket):
        start_idx = first_brace
        end_char = "}"
    elif first_bracket != -1:
        start_idx = first_bracket
        end_char = "]"
        
    if start_idx != -1:
        # Find last matching end char
        end_idx = text.rfind(end_char)
        if end_idx != -1:
            text = text[start_idx:end_idx+1]
            
    return text
