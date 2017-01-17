#!/usr/bin/env python3
"""Class used to set test configuration used by unittests."""

# Standard imports
import sys
import os

# mdl libraries
try:
    from mdl.test import unittest_setup
except:
    print('You need to set your PYTHONPATH to include the mdl library')
    sys.exit(2)


def main():
    """Create test configurations."""
    # Check environment
    config = unittest_setup.TestConfig()
    config.create()


if __name__ == '__main__':
    # Do the unit test
    main()
