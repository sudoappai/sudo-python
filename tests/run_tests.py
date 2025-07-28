#!/usr/bin/env python3
"""
Test runner for SUDO Python SDK integration tests.

This script helps run the comprehensive integration tests with proper setup.

Usage:
    python run_tests.py

Environment variables:
    SUDO_API_KEY - Required: Your SUDO API key
    SUDO_SERVER_URL - Optional: Server URL (defaults to production)
"""

import os
import sys
import subprocess
from pathlib import Path


def main():
    """Run the integration tests with proper setup."""
    
    # Check for API key
    api_key = os.getenv("SUDO_API_KEY")
    if not api_key:
        print("❌ Error: SUDO_API_KEY environment variable is required")
        print("   Please set your API key:")
        print("   export SUDO_API_KEY='your-api-key-here'")
        sys.exit(1)
    
    print("✅ Found SUDO_API_KEY environment variable")
    
    # Get the directory containing this script
    test_dir = Path(__file__).parent.absolute()
    
    # Check if pytest is available
    try:
        import pytest
        print("✅ pytest is available")
    except ImportError:
        print("❌ pytest not found. Installing...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pytest", "requests"])
        print("✅ Installed test dependencies")
    
    # Run the tests
    print(f"\n🚀 Running integration tests from {test_dir}")
    print("   This may take several minutes as it tests multiple AI models...")
    print("   Use Ctrl+C to cancel\n")
    
    test_file = test_dir / "test_integration.py"
    
    # Run pytest with verbose output
    result = subprocess.run([
        sys.executable, "-m", "pytest", 
        str(test_file),
        "-v",                    # Verbose output
        "--tb=short",           # Short traceback format
        "--color=yes",          # Colored output
        "-x"                    # Stop on first failure
    ])
    
    if result.returncode == 0:
        print("\n🎉 All tests passed!")
    else:
        print(f"\n❌ Tests failed with exit code {result.returncode}")
        sys.exit(result.returncode)


if __name__ == "__main__":
    main() 