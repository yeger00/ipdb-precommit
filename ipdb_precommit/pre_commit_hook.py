#!/usr/bin/env python3
"""Pre-commit hook to remove ipdb statements from Python files."""

import sys
from pathlib import Path
from typing import List

from .remove_ipdb import process_file


def main() -> int:
    """Main entry point for the pre-commit hook."""
    # Get the list of files from pre-commit
    files = sys.argv[1:]
    
    if not files:
        print("No files provided")
        return 0
    
    removed_statements: List[str] = []
    
    for file_path in files:
        if not file_path.endswith('.py'):
            continue
            
        file_removed = process_file(file_path)
        if file_removed:
            removed_statements.extend(file_removed)
    
    if removed_statements:
        print("\nRemoved ipdb statements:")
        for statement in removed_statements:
            print(f"  - {statement.strip()}")
        return 1
    
    return 0


if __name__ == '__main__':
    sys.exit(main()) 