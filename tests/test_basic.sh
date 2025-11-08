#!/bin/bash
# Basic smoke tests for mist-api-info scripts

set -e

echo "Running basic tests for mist-api-info..."

# Test 1: Check if main scripts exist
echo "Test 1: Checking if scripts exist..."
if [ -f "mist_api_info.sh" ]; then
    echo "  ✓ mist_api_info.sh exists"
else
    echo "  ✗ mist_api_info.sh not found"
    exit 1
fi

# Test 2: Check if scripts are executable
echo "Test 2: Checking if scripts are executable..."
if [ -x "mist_api_info.sh" ]; then
    echo "  ✓ mist_api_info.sh is executable"
else
    echo "  ⚠ mist_api_info.sh is not executable (fixing...)"
    chmod +x mist_api_info.sh
fi

# Test 3: Check script syntax
echo "Test 3: Checking script syntax..."
bash -n mist_api_info.sh && echo "  ✓ Syntax check passed" || exit 1

echo ""
echo "All tests passed! ✓"
