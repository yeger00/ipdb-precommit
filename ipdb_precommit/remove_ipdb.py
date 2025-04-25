"""Module to remove ipdb statements from Python files."""

import re
from typing import List, Tuple


def remove_ipdb_statements(content: str) -> Tuple[str, List[str]]:
    """
    Remove ipdb statements from Python code.
    
    Args:
        content: The Python code content as a string
        
    Returns:
        Tuple containing:
        - The modified code with ipdb statements removed
        - List of removed statements
    """
    # Pattern to match ipdb statements
    # This will match:
    # - import ipdb
    # - from ipdb import ...
    # - ipdb.set_trace()
    # - ipdb.breakpoint()
    pattern = r'^(?:import\s+ipdb|from\s+ipdb\s+import.*|.*ipdb\.(?:set_trace|breakpoint)\(\))$'
    
    lines = content.split('\n')
    modified_lines = []
    removed_statements = []
    
    for line in lines:
        if re.match(pattern, line.strip()):
            removed_statements.append(line)
        else:
            modified_lines.append(line)
    
    return '\n'.join(modified_lines), removed_statements


def process_file(file_path: str) -> List[str]:
    """
    Process a Python file and remove ipdb statements.
    
    Args:
        file_path: Path to the Python file
        
    Returns:
        List of removed statements
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        modified_content, removed_statements = remove_ipdb_statements(content)
        
        if removed_statements:
            with open(file_path, 'w', encoding='utf-8') as f:
                f.write(modified_content)
        
        return removed_statements
    except Exception as e:
        print(f"Error processing {file_path}: {str(e)}")
        return [] 