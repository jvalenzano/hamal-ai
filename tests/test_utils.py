import pytest
import time
from unittest.mock import patch, MagicMock
from agents.utils import (
    retry_with_backoff, 
    call_llm, 
    FatalError, 
    RetryableError,
    get_response_content
)

def test_retry_with_backoff_success():
    """Test successful execution on first try"""
    mock_func = MagicMock(return_value="success")
    decorator = retry_with_backoff(max_attempts=3, base_delay=0.01)
    decorated_func = decorator(mock_func)
    
    result = decorated_func()
    
    assert result == "success"
    assert mock_func.call_count == 1

def test_retry_with_backoff_retry_then_success():
    """Test retryable error that eventually succeeds"""
    mock_func = MagicMock(side_effect=[Exception("rate limit"), "success"])
    
    # Mock time.sleep to speed up tests
    with patch("time.sleep"):
        decorator = retry_with_backoff(max_attempts=3, base_delay=0.01)
        decorated_func = decorator(mock_func)
        result = decorated_func()
    
    assert result == "success"
    assert mock_func.call_count == 2

def test_retry_with_backoff_fatal_error():
    """Test that fatal errors aren't retried"""
    mock_func = MagicMock(side_effect=FatalError("invalid api key"))
    
    decorator = retry_with_backoff(max_attempts=3, base_delay=0.01)
    decorated_func = decorator(mock_func)
    
    with pytest.raises(FatalError):
        decorated_func()
    
    assert mock_func.call_count == 1

def test_retry_with_backoff_max_attempts_exceeded():
    """Test that max attempts are respected"""
    mock_func = MagicMock(side_effect=Exception("temporary error"))
    
    with patch("time.sleep"):
        decorator = retry_with_backoff(max_attempts=2, base_delay=0.01)
        decorated_func = decorator(mock_func)
        with pytest.raises(Exception) as excinfo:
            decorated_func()
    
    assert "temporary error" in str(excinfo.value)
    assert mock_func.call_count == 2

@patch("agents.utils.completion")
def test_call_llm_success(mock_completion, mock_llm_response):
    """Test successful LLM call"""
    mock_completion.return_value = mock_llm_response
    
    messages = [{"role": "user", "content": "hi"}]
    response = call_llm(messages)
    
    assert get_response_content(response) == "Mocked LLM Response"
    mock_completion.assert_called_once()

@patch("agents.utils.completion")
def test_call_llm_retryable_error(mock_completion, mock_llm_response):
    """Test LLM call with retryable error"""
    mock_completion.side_effect = [Exception("rate limit"), mock_llm_response]
    
    messages = [{"role": "user", "content": "hi"}]
    with patch("time.sleep"):
        response = call_llm(messages)
    
    assert get_response_content(response) == "Mocked LLM Response"
    assert mock_completion.call_count == 2

@patch("agents.utils.completion")
def test_call_llm_fatal_error(mock_completion):
    """Test LLM call with fatal error"""
    mock_completion.side_effect = Exception("invalid api key")
    
    messages = [{"role": "user", "content": "hi"}]
    with pytest.raises(FatalError):
        call_llm(messages)
    
    assert mock_completion.call_count == 1
