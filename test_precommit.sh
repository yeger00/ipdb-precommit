#!/bin/bash

# Create a temporary directory for testing
TEST_DIR=$(mktemp -d)
cd "$TEST_DIR"

echo "Created test directory: $TEST_DIR"

# Initialize a new git repository
git init

# Create a virtual environment and install the package
python3 -m venv venv
source venv/bin/activate
pip install -e /Users/aviyeger/projects/ipdb-precommit

# Install pre-commit
pip install pre-commit

# Create .pre-commit-config.yaml
cat > .pre-commit-config.yaml << EOL
repos:
-   repo: local
    hooks:
    -   id: remove-ipdb
        name: Remove ipdb statements
        entry: remove-ipdb
        language: python
        types: [python]
        pass_filenames: true
EOL

# Install the pre-commit hook
pre-commit install

echo "Running Test 1: File with ipdb statements"
# Create a test file with ipdb statements
cat > test1.py << EOL
import ipdb
ipdb.set_trace()
print("Hello, World!")
EOL

# Stage the file
git add test1.py

# Run pre-commit
echo "Running pre-commit on test1.py..."
pre-commit run --files test1.py

# Check if the file was modified
if grep -q "ipdb" test1.py; then
    echo "❌ Test 1 failed: ipdb statements were not removed"
    exit 1
else
    echo "✅ Test 1 passed: ipdb statements were removed"
fi

echo "Running Test 2: File without ipdb statements"
# Create a test file without ipdb statements
cat > test2.py << EOL
print("Hello, World!")
print("Something, else!")
EOL

# Stage the file
git add test2.py

# Run pre-commit
echo "Running pre-commit on test2.py..."
pre-commit run --files test2.py

# Check if the file was modified
if ! grep -q "Hello, World!" test2.py; then
    echo "❌ Test 2 failed: File was modified when it shouldn't have been"
    exit 1
else
    echo "✅ Test 2 passed: File was not modified"
fi

echo "All tests passed!"
deactivate
rm -rf "$TEST_DIR" 