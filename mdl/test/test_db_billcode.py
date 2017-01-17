#!/usr/bin/env python3
"""Test the db_billcode library in the mdl.db module."""

import unittest

from mdl.db import db_billcode
from mdl.test import unittest_setup_db
from mdl.test import unittest_setup


class TestGetIDXBillcode(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Setup database
    expected = unittest_setup_db.setup_db_billcode()

    # Retrieve data
    good_agent = db_billcode.GetIDXBillcode(expected['idx_billcode'])

    def test_init_(self):
        """Testing method init."""
        # Test with non existent AgentIDX
        record = db_billcode.GetIDXBillcode(-1)
        self.assertEqual(record.exists(), False)

    def test_idx_billcode(self):
        """Testing method idx_billcode."""
        # Testing with known good value
        result = self.good_agent.idx_billcode()
        self.assertEqual(result, self.expected['idx_billcode'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.idx_billcode()
        self.assertNotEqual(result, expected)

    def test_name(self):
        """Testing method name."""
        # Testing with known good value
        result = self.good_agent.name()
        self.assertEqual(result, self.expected['name'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.name()
        self.assertNotEqual(result, expected)

    def test_code(self):
        """Testing method code."""
        # Testing with known good value
        result = self.good_agent.code()
        self.assertEqual(result, self.expected['code'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.code()
        self.assertNotEqual(result, expected)

    def test_exists(self):
        """Testing method exists."""
        # Testing with known good value
        result = self.good_agent.exists()
        self.assertEqual(result, True)

    def test_enabled(self):
        """Testing method enabled."""
        # Testing with known good value
        result = self.good_agent.enabled()
        self.assertEqual(result, self.expected['enabled'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.enabled()
        self.assertNotEqual(result, expected)


class TestGetCodeBillcode(unittest.TestCase):
    """Checks all functions and methods."""

    # Setup database
    expected = unittest_setup_db.setup_db_billcode()

    # Retrieve data
    good_agent = db_billcode.GetCodeBillcode(expected['code'])

    def test_init_getcode(self):
        """Testing method __init__."""
        # Test with non existent AgentID
        record = db_billcode.GetCodeBillcode('bogus')
        self.assertEqual(record.exists(), False)

    def test_idx_billcode(self):
        """Testing method idx_billcode."""
        # Testing with known good value
        result = self.good_agent.idx_billcode()
        self.assertEqual(result, self.expected['idx_billcode'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.idx_billcode()
        self.assertNotEqual(result, expected)

    def test_name(self):
        """Testing method name."""
        # Testing with known good value
        result = self.good_agent.name()
        self.assertEqual(result, self.expected['name'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.name()
        self.assertNotEqual(result, expected)

    def test_code(self):
        """Testing method code."""
        # Testing with known good value
        result = self.good_agent.code()
        self.assertEqual(result, self.expected['code'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.code()
        self.assertNotEqual(result, expected)

    def test_exists(self):
        """Testing method exists."""
        # Testing with known good value
        result = self.good_agent.exists()
        self.assertEqual(result, True)

    def test_enabled(self):
        """Testing method enabled."""
        # Testing with known good value
        result = self.good_agent.enabled()
        self.assertEqual(result, self.expected['enabled'])

        # Testing with known bad value
        expected = ('bogus')
        result = self.good_agent.enabled()
        self.assertNotEqual(result, expected)


class TestFunctions(unittest.TestCase):
    """Checks all functions and methods."""

    # Setup database
    expected = unittest_setup_db.setup_db_billcode()

    def test_code_exists(self):
        """Testing function code_exists."""
        # Testing with known good value
        expected = True
        result = db_billcode.code_exists(self.expected['code'])
        self.assertEqual(result, expected)

        # Testing with known bad value
        expected = False
        result = db_billcode.code_exists('bogus')
        self.assertEqual(result, expected)

    def test_idx_billcode_exists(self):
        """Testing function idx_billcode_exists."""
        # Testing with known good value
        expected = True
        result = db_billcode.idx_billcode_exists(self.expected['idx_billcode'])
        self.assertEqual(result, expected)

        # Testing with known bad value
        expected = False
        result = db_billcode.idx_billcode_exists(None)
        self.assertEqual(result, expected)


if __name__ == '__main__':
    # Test the environment variables
    unittest_setup.ready()

    # Do the unit test
    unittest.main()
