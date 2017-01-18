"""Module of mdl database functions.

Classes for rider data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import Riders


class GetIDXRider(object):
    """Class to return rider data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_rider):
        """Function for intializing the class.

        Args:
            idx_rider: Rider idx_rider

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_rider', 'first_name', 'last_name',
            'password', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_rider, int) is False:
            idx_rider = None

        # Only work if the value is an integer
        if isinstance(idx_rider, int) is True and idx_rider is not None:
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(Riders).filter(
                Riders.idx_rider == idx_rider)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_rider'] = idx_rider
                    self.data_dict[
                        'password'] = general.decode(instance.password)
                    self.data_dict[
                        'first_name'] = general.decode(instance.first_name)
                    self.data_dict[
                        'last_name'] = general.decode(instance.last_name)
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

    def idx_rider(self):
        """Get idx_rider value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_rider']
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
        """Get rider last_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['last_name']
        return value

    def password(self):
        """Get rider password.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['password']
        return value

    def enabled(self):
        """Get rider enabled.

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
        """Get all rider data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_rider_exists(idx_rider):
    """Determine whether the idx_rider exists.

    Args:
        idx_rider: idx_rider value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_rider, int) is False:
        idx_rider = None

    # Get information on rider from database
    data = GetIDXRider(idx_rider)
    if data.exists() is True:
        exists = True

    # Return
    return exists
