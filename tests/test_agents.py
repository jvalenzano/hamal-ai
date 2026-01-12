import pytest
import os
from unittest.mock import patch, MagicMock
from agents.discovery import run_discovery

def test_run_discovery_success(mock_llm_response, mock_tavily_results):
    """Test full discovery pipeline with mocked external services"""
    
    # Mock LLM calls in discovery.py
    # discovery.py has two LLM calls: interrogate_problem and generate_problem_statement
    # and one gather_context call which uses tavily
    
    with patch("agents.discovery.call_llm") as mock_call_llm, \
         patch("agents.discovery.tavily") as mock_tavily:
        
        # Setup mock returns
        mock_call_llm.return_value = mock_llm_response
        mock_tavily.search.return_value = mock_tavily_results
        
        charter_text = "Standard agency charter for a forest fire detection system."
        project_name = "test-fire-project"
        
        # We need to mock os.makedirs and open to avoid writing to disk
        with patch("os.makedirs"), \
             patch("builtins.open", MagicMock()):
            
            output_path = run_discovery(charter_text, project_name)
            
        assert output_path == f"outputs/{project_name}/problem.md"
        assert mock_call_llm.call_count == 2
        assert mock_tavily.search.call_count == 3 # gather_context makes 3 queries
