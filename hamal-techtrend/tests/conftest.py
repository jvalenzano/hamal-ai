import pytest
import os
from unittest.mock import MagicMock, patch

@pytest.fixture(autouse=True)
def mock_env():
    """Mock environment variables to prevent accidental API leak"""
    with patch.dict(os.environ, {
        "ANTHROPIC_API_KEY": "mock-key",
        "TAVILY_API_KEY": "mock-key",
        "LLM_MODEL": "claude-mock",
        "LLM_FAST_MODEL": "claude-fast-mock"
    }):
        yield

@pytest.fixture
def mock_llm_response():
    """Fixture for a standard LiteLLM success response"""
    mock_response = MagicMock()
    mock_response.choices = [MagicMock()]
    mock_response.choices[0].message.content = "Mocked LLM Response"
    return mock_response

@pytest.fixture
def mock_tavily_results():
    """Fixture for standard Tavily search results"""
    return {
        "results": [
            {"title": "Result 1", "url": "http://example.com/1", "content": "Content 1"},
            {"title": "Result 2", "url": "http://example.com/2", "content": "Content 2"}
        ]
    }
