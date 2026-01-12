
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
