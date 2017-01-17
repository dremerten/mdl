#!/usr/bin/env python3
"""Test the db_deviceagent library in the mdl.db module."""

import unittest
import time

# Import mdl stuff
from mdl.db import db_deviceagent
from mdl.utils import general
from mdl.test import unittest_setup_db
from mdl.test import unittest_setup


class TestGetDeviceAgent(unittest.TestCase):
    """Checks all functions and methods."""

    #########################################################################
    # General object setup
    #########################################################################

    # Initiazlize key variables
    data = {}
    data['devicename'] = general.randomstring()
    data['id_agent'] = general.randomstring()
    data['agent'] = general.randomstring()
    data['timestamp'] = int(time.time())

    # Setup database
    unittest_setup_db.initialize_db()
    (idx_device_good, idx_agent_good) = unittest_setup_db.setup_db_deviceagent(data)

    # Create device object
    good_device = db_deviceagent.GetDeviceAgent(
        idx_device_good, idx_agent_good)

    def test___init__(self):
        """Testing method __init__."""
        # Test with non existent IDXDevice
        record = db_deviceagent.GetDeviceAgent('bogus', 'bogus')
        self.assertEqual(record.exists(), False)

    def test_exists(self):
        """Testing method exists."""
        # Testing with known good value
        result = self.good_device.exists()
        self.assertEqual(result, True)

        # Test with known bad value
        expected = db_deviceagent.GetDeviceAgent(None, None)
        result = expected.exists()
        self.assertEqual(result, False)

    def test_enabled(self):
        """Testing method enabled."""
        # Testing with known good value
        result = self.good_device.enabled()
        self.assertEqual(result, True)

    def test_last_timestamp(self):
        """Testing method last_timestamp."""
        # Testing with known good value
        result = self.good_device.last_timestamp()
        self.assertEqual(result, self.data['timestamp'])

    def test_idx_deviceagent(self):
        """Testing method idx_deviceagent."""
        # Testing with known good value
        result = self.good_device.idx_deviceagent()
        self.assertEqual(result, 1)


class TestFunctions(unittest.TestCase):
    """Checks all functions."""

    #########################################################################
    # General object setup
    #########################################################################

    # Initiazlize key variables
    data = {}
    data['devicename'] = general.randomstring()
    data['id_agent'] = general.randomstring()
    data['agent'] = general.randomstring()
    data['timestamp'] = int(time.time())

    # Setup database
    unittest_setup_db.initialize_db()
    (idx_device_good, idx_agent_good) = unittest_setup_db.setup_db_deviceagent(data)

    def test_device_agent_exists(self):
        """Testing function device_agent_exists."""
        # Testing with known good value
        result = db_deviceagent.device_agent_exists(
            self.idx_device_good, self.idx_agent_good)
        self.assertEqual(result, True)

        # Testing with known good value
        result = db_deviceagent.device_agent_exists(None, None)
        self.assertEqual(result, False)

    def test_all_device_indices(self):
        """Testing function all_device_indices."""
        # Testing with known good value
        result = db_deviceagent.all_device_indices()
        self.assertEqual(result, [1])

    def test_device_indices(self):
        """Testing function device_indices."""
        # Testing with known good value
        result = db_deviceagent.device_indices(self.idx_agent_good)
        self.assertEqual(result, [1])

    def test_agent_indices(self):
        """Testing function agent_indices."""
        # Testing with known good value
        result = db_deviceagent.agent_indices(
            self.idx_agent_good)
        self.assertEqual(result, [1])

    def test_get_all_device_agents(self):
        """Testing function get_all_device_agents."""
        results = db_deviceagent.get_all_device_agents()
        for result in results:
            for key, _ in result.items():
                self.assertEqual(result[key], 1)


if __name__ == '__main__':
    # Test the environment variables
    unittest_setup.ready()

    # Do the unit test
    unittest.main()
