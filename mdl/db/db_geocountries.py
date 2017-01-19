"""Module of mdl database functions.

Classes for geocountry data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import GeoCountries


class GetIDXGeoCountry(object):
    """Class to return geocountry data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_geocountry):
        """Function for intializing the class.

        Args:
            idx_geocountry: GeoCountry idx_geocountry

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_geocountry', 'geocountry_name', 'idx_georegion', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_geocountry, int) is False:
            idx_geocountry = None

        # Only work if the value is an integer
        if (isinstance(idx_geocountry, int) is True) and (
                idx_geocountry is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(GeoCountries).filter(
                GeoCountries.idx_geocountry == idx_geocountry)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_geocountry'] = idx_geocountry
                    self.data_dict[
                        'geocountry_name'] = general.decode(
                            instance.geocountry_name)
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

    def idx_geocountry(self):
        """Get idx_geocountry value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_geocountry']
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

    def geocountry_name(self):
        """Get geocountry geocountry_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['geocountry_name']
        return value

    def enabled(self):
        """Get geocountry enabled.

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
        """Get all geocountry data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_geocountry_exists(idx_geocountry):
    """Determine whether the idx_geocountry exists.

    Args:
        idx_geocountry: idx_geocountry value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_geocountry, int) is False:
        idx_geocountry = None

    # Get information on geocountry from database
    data = GetIDXGeoCountry(idx_geocountry)
    if data.exists() is True:
        exists = True

    # Return
    return exists
