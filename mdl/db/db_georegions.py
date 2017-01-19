"""Module of mdl database functions.

Classes for georegion data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import GeoRegions


class GetIDXGeoCity(object):
    """Class to return georegion data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_georegion):
        """Function for intializing the class.

        Args:
            idx_georegion: GeoCity idx_georegion

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_georegion', 'georegion_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_georegion, int) is False:
            idx_georegion = None

        # Only work if the value is an integer
        if (isinstance(idx_georegion, int) is True) and (
                idx_georegion is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(GeoRegions).filter(
                GeoRegions.idx_georegion == idx_georegion)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_georegion'] = idx_georegion
                    self.data_dict[
                        'georegion_name'] = general.decode(
                            instance.georegion_name)
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

    def georegion_name(self):
        """Get georegion georegion_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['georegion_name']
        return value

    def enabled(self):
        """Get georegion enabled.

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
        """Get all georegion data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_georegion_exists(idx_georegion):
    """Determine whether the idx_georegion exists.

    Args:
        idx_georegion: idx_georegion value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_georegion, int) is False:
        idx_georegion = None

    # Get information on georegion from database
    data = GetIDXGeoCity(idx_georegion)
    if data.exists() is True:
        exists = True

    # Return
    return exists
