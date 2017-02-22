"""Module of mdl database functions.

Classes for drivercompanyrating data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.db import db
from mdl.db.db_orm import DriverCompanyRatings


class GetIDXDriverCompanyRatings(object):
    """Class to return drivercompanyrating data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_drivercompanyrating):
        """Function for intializing the class.

        Args:
            idx_drivercompanyrating: DriverCompanyRatings
                idx_drivercompanyrating

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_drivercompanyrating', 'rating_value', 'rating_timestamp',
            'idx_drivercompany', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_drivercompanyrating, int) is False:
            idx_drivercompanyrating = None

        # Only work if the value is an integer
        if (isinstance(idx_drivercompanyrating, int) is True) and (
                idx_drivercompanyrating is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(DriverCompanyRatings).filter(
                DriverCompanyRatings.idx_drivercompanyrating == idx_drivercompanyrating)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict[
                        'idx_drivercompanyrating'] = idx_drivercompanyrating
                    self.data_dict['rating_value'] = instance.rating_value
                    self.data_dict['idx_drivercompany'] = instance.idx_drivercompany
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

    def idx_drivercompanyrating(self):
        """Get idx_drivercompanyrating value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_drivercompanyrating']
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
        """Get drivercompanyrating rating_value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['rating_value']
        return value

    def enabled(self):
        """Get drivercompanyrating enabled.

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
        """Get all drivercompanyrating data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_drivercompanyrating_exists(idx_drivercompanyrating):
    """Determine whether the idx_drivercompanyrating exists.

    Args:
        idx_drivercompanyrating: idx_drivercompanyrating value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_drivercompanyrating, int) is False:
        idx_drivercompanyrating = None

    # Get information on drivercompanyrating from database
    data = GetIDXDriverCompanyRatings(idx_drivercompanyrating)
    if data.exists() is True:
        exists = True

    # Return
    return exists
