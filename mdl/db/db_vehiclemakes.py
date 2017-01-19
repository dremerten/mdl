"""Module of mdl database functions.

Classes for make data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import VehicleMakes


class GetIDXVehicleMake(object):
    """Class to return make data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_vehiclemake):
        """Function for intializing the class.

        Args:
            idx_vehiclemake: Make idx_vehiclemake

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_vehiclemake', 'make_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_vehiclemake, int) is False:
            idx_vehiclemake = None

        # Only work if the value is an integer
        if (isinstance(idx_vehiclemake, int) is True) and (
                idx_vehiclemake is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(VehicleMakes).filter(
                VehicleMakes.idx_vehiclemake == idx_vehiclemake)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_vehiclemake'] = idx_vehiclemake
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

    def idx_vehiclemake(self):
        """Get idx_vehiclemake value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_vehiclemake']
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


def idx_vehiclemake_exists(idx_vehiclemake):
    """Determine whether the idx_vehiclemake exists.

    Args:
        idx_vehiclemake: idx_vehiclemake value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_vehiclemake, int) is False:
        idx_vehiclemake = None

    # Get information on make from database
    data = GetIDXVehicleMake(idx_vehiclemake)
    if data.exists() is True:
        exists = True

    # Return
    return exists
