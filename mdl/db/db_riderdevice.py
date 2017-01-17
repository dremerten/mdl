"""Module of mdl database functions.

Classes for rider data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import RiderDevice


class GetIDXRiderDevice(object):
    """Class to return rider data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_riderdevice):
        """Function for intializing the class.

        Args:
            idx_riderdevice: RiderDevice idx_riderdevice

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_riderdevice', 'id_riderdevice', 'idx_rider',
            'serial_riderdevice', 'idx_devicemodel', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_riderdevice, int) is False:
            idx_riderdevice = None

        # Only work if the value is an integer
        if (isinstance(idx_riderdevice, int) is True) and (
                idx_riderdevice is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(RiderDevice).filter(
                RiderDevice.idx_riderdevice == idx_riderdevice)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_riderdevice'] = idx_riderdevice
                    self.data_dict[
                        'idx_devicemodel'] = instance.idx_devicemodel
                    self.data_dict[
                        'serial_riderdevice'] = general.decode(
                            instance.serial_riderdevice)
                    self.data_dict[
                        'id_riderdevice'] = general.decode(
                            instance.id_riderdevice)
                    self.data_dict['idx_rider'] = instance.idx_rider
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

    def idx_riderdevice(self):
        """Get idx_riderdevice value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_riderdevice']
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

    def id_riderdevice(self):
        """Get id_riderdevice value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['id_riderdevice']
        return value

    def idx_rider(self):
        """Get rider idx_rider.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_rider']
        return value

    def serial_riderdevice(self):
        """Get rider serial_riderdevice.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['serial_riderdevice']
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


def idx_riderdevice_exists(idx_riderdevice):
    """Determine whether the idx_riderdevice exists.

    Args:
        idx_riderdevice: idx_riderdevice value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_riderdevice, int) is False:
        idx_riderdevice = None

    # Get information on rider from database
    data = GetIDXRiderDevice(idx_riderdevice)
    if data.exists() is True:
        exists = True

    # Return
    return exists
