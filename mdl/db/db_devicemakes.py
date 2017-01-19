"""Module of mdl database functions.

Classes for make data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import DeviceMakes


class GetIDXDeviceMake(object):
    """Class to return make data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_devicemake):
        """Function for intializing the class.

        Args:
            idx_devicemake: Make idx_devicemake

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_devicemake', 'make_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_devicemake, int) is False:
            idx_devicemake = None

        # Only work if the value is an integer
        if (isinstance(idx_devicemake, int) is True) and (
                idx_devicemake is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(DeviceMakes).filter(
                DeviceMakes.idx_devicemake == idx_devicemake)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_devicemake'] = idx_devicemake
                    self.data_dict[
                        'make_name'] = general.decode(instance.make_name)
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

    def idx_devicemake(self):
        """Get idx_devicemake value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_devicemake']
        return value

    def make_name(self):
        """Get make make_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['make_name']
        return value

    def enabled(self):
        """Get make enabled.

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
        """Get all make data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_devicemake_exists(idx_devicemake):
    """Determine whether the idx_devicemake exists.

    Args:
        idx_devicemake: idx_devicemake value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_devicemake, int) is False:
        idx_devicemake = None

    # Get information on make from database
    data = GetIDXDeviceMake(idx_devicemake)
    if data.exists() is True:
        exists = True

    # Return
    return exists
