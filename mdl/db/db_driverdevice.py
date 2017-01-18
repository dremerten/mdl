"""Module of mdl database functions.

Classes for driver data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import DriverDevices


class GetIDXDriverDevice(object):
    """Class to return driver data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_driverdevice):
        """Function for intializing the class.

        Args:
            idx_driverdevice: DriverDevice idx_driverdevice

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_driverdevice', 'id_driverdevice', 'idx_driver', 'idx_route',
            'serial_driverdevice', 'idx_devicemodel', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_driverdevice, int) is False:
            idx_driverdevice = None

        # Only work if the value is an integer
        if (isinstance(idx_driverdevice, int) is True) and (
                idx_driverdevice is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(DriverDevices).filter(
                DriverDevices.idx_driverdevice == idx_driverdevice)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_driverdevice'] = idx_driverdevice
                    self.data_dict[
                        'idx_devicemodel'] = instance.idx_devicemodel
                    self.data_dict[
                        'idx_route'] = instance.idx_route
                    self.data_dict[
                        'serial_driverdevice'] = general.decode(
                            instance.serial_driverdevice)
                    self.data_dict[
                        'id_driverdevice'] = general.decode(
                            instance.id_driverdevice)
                    self.data_dict['idx_driver'] = instance.idx_driver
                    self.data_dict['enabled'] = bool(instance.enabled)
                    self.data_dict['exists'] = True
                    break

            # Return the session to the database pool after processing
            database.close()

    def exists(self):
        """Tell if row is exists.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['exists']
        return value

    def idx_driverdevice(self):
        """Get idx_driverdevice value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_driverdevice']
        return value

    def idx_route(self):
        """Get idx_route value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_route']
        return value

    def idx_devicemodel(self):
        """Get idx_devicemodel value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_devicemodel']
        return value

    def id_driverdevice(self):
        """Get id_driverdevice value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['id_driverdevice']
        return value

    def idx_driver(self):
        """Get driver idx_driver.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_driver']
        return value

    def serial_driverdevice(self):
        """Get driver serial_driverdevice.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['serial_driverdevice']
        return value

    def enabled(self):
        """Get driver enabled.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['enabled']

        # Return
        return value

    def everything(self):
        """Get all driver data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_driverdevice_exists(idx_driverdevice):
    """Determine whether the idx_driverdevice exists.

    Args:
        idx_driverdevice: idx_driverdevice value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_driverdevice, int) is False:
        idx_driverdevice = None

    # Get information on driver from database
    data = GetIDXDriverDevice(idx_driverdevice)
    if data.exists() is True:
        exists = True

    # Return
    return exists
