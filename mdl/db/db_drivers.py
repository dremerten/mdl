"""Module of mdl database functions.

Classes for driver data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import Drivers


class GetIDXDriver(object):
    """Class to return driver data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_driver):
        """Function for intializing the class.

        Args:
            idx_driver: Driver idx_driver

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_driver', 'first_name', 'last_name', 'idx_drivercompany',
            'password', 'off_duty', 'idx_billaddress', 'idx_address',
            'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_driver, int) is False:
            idx_driver = None

        # Only work if the value is an integer
        if isinstance(idx_driver, int) is True and idx_driver is not None:
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(Drivers).filter(
                Drivers.idx_driver == idx_driver)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_driver'] = idx_driver
                    self.data_dict[
                        'idx_address'] = instance.idx_address
                    self.data_dict[
                        'idx_billaddress'] = instance.idx_billaddress
                    self.data_dict[
                        'password'] = general.decode(instance.password)
                    self.data_dict[
                        'first_name'] = general.decode(instance.first_name)
                    self.data_dict[
                        'last_name'] = general.decode(instance.last_name)
                    self.data_dict['off_duty'] = instance.off_duty
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

    def idx_address(self):
        """Get idx_address value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_address']
        return value

    def idx_billaddress(self):
        """Get idx_billaddress value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_billaddress']
        return value

    def idx_driver(self):
        """Get idx_driver value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_driver']
        return value

    def off_duty(self):
        """Get off_duty value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['off_duty']
        return value

    def idx_drivercompany(self):
        """Get idx_drivercompany value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_drivercompany']
        return value

    def first_name(self):
        """Get first_name value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['first_name']
        return value

    def last_name(self):
        """Get driver last_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['last_name']
        return value

    def password(self):
        """Get driver password.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['password']
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


def idx_driver_exists(idx_driver):
    """Determine whether the idx_driver exists.

    Args:
        idx_driver: idx_driver value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_driver, int) is False:
        idx_driver = None

    # Get information on driver from database
    data = GetIDXDriver(idx_driver)
    if data.exists() is True:
        exists = True

    # Return
    return exists
