"""
Test suite for ADF Library.

This package contains all tests for the ADF Library. The test suite uses pytest
and is organized to mirror the structure of the main package.

Test Modules:
    - test_document.py: Tests for ADF document creation and manipulation
    - test_link.py: Tests for link handling and formatting
    - test_table.py: Tests for table creation and configuration
    - test_text.py: Tests for text formatting and marks
"""

import os
import sys

# Add the parent directory to sys.path to allow importing the package
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

# Version of the test suite
__version__ = '0.1.0'

# Test configuration
TEST_DATA_DIR = os.path.join(os.path.dirname(__file__), 'data')