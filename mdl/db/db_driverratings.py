"""Module of mdl database functions.

Classes for driverrating data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.db import db
from mdl.db.db_orm import DriverRatings


class GetIDXDriverRatings(object):
    """Class to return driverrating data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_driverrating):
        """Function for intializing the class.

        Args:
            idx_driverrating: DriverRatings idx_driverrating

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_driverrating', 'rating_value', 'rating_timestamp',
            'idx_driver', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_driverrating, int) is False:
            idx_driverrating = None

        # Only work if the value is an integer
        if (isinstance(idx_driverrating, int) is True) and (
                idx_driverrating is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(DriverRatings).filter(
                DriverRatings.idx_driverrating == idx_driverrating)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_driverrating'] = idx_driverrating
                    self.data_dict['rating_value'] = instance.rating_value
                    self.data_dict['idx_driver'] = instance.idx_driver
                    self.data_dict[
                        'rating_timestamp'] = instance.rating_timestamp
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

    def idx_driverrating(self):
        """Get idx_driverrating value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_driverrating']
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

    def rating_timestamp(self):
        """Get rating_timestamp value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['rating_timestamp']
        return value

    def rating_value(self):
        """Get driverrating rating_value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['rating_value']
        return value

    def enabled(self):
        """Get driverrating enabled.

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
        """Get all driverrating data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_driverrating_exists(idx_driverrating):
    """Determine whether the idx_driverrating exists.

    Args:
        idx_driverrating: idx_driverrating value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_driverrating, int) is False:
        idx_driverrating = None

    # Get information on driverrating from database
    data = GetIDXDriverRatings(idx_driverrating)
    if data.exists() is True:
        exists = True

    # Return
    return exists
