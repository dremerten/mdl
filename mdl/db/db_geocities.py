"""Module of mdl database functions.

Classes for geocity data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import GeoCities


class GetIDXGeoCity(object):
    """Class to return geocity data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_geocity):
        """Function for intializing the class.

        Args:
            idx_geocity: GeoCity idx_geocity

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_geocity', 'geocity_name', 'idx_georegion', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_geocity, int) is False:
            idx_geocity = None

        # Only work if the value is an integer
        if isinstance(idx_geocity, int) is True and idx_geocity is not None:
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(GeoCities).filter(
                GeoCities.idx_geocity == idx_geocity)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_geocity'] = idx_geocity
                    self.data_dict[
                        'geocity_name'] = general.decode(instance.geocity_name)
                    self.data_dict['idx_georegion'] = instance.idx_georegion
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

    def idx_geocity(self):
        """Get idx_geocity value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_geocity']
        return value

    def idx_georegion(self):
        """Get idx_georegion value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_georegion']
        return value

    def geocity_name(self):
        """Get geocity geocity_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['geocity_name']
        return value

    def enabled(self):
        """Get geocity enabled.

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
        """Get all geocity data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_geocity_exists(idx_geocity):
    """Determine whether the idx_geocity exists.

    Args:
        idx_geocity: idx_geocity value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_geocity, int) is False:
        idx_geocity = None

    # Get information on geocity from database
    data = GetIDXGeoCity(idx_geocity)
    if data.exists() is True:
        exists = True

    # Return
    return exists
