"""Module of mdl database functions.

Classes for vehiclecategory data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import VehicleCategories


class GetIDXVehicleCategory(object):
    """Class to return vehiclecategory data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_vehiclecategory):
        """Function for intializing the class.

        Args:
            idx_vehiclecategory: VehicleCategory idx_vehiclecategory

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_vehiclecategory', 'vehiclecategory_name',
            'idx_vehiclemodel', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_vehiclecategory, int) is False:
            idx_vehiclecategory = None

        # Only work if the value is an integer
        if isinstance(idx_vehiclecategory, int) is (
                True and idx_vehiclecategory is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(VehicleCategories).filter(
                VehicleCategories.idx_vehiclecategory == idx_vehiclecategory)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_vehiclecategory'] = idx_vehiclecategory
                    self.data_dict[
                        'vehiclecategory_name'] = general.decode(
                            instance.vehiclecategory_name)
                    self.data_dict[
                        'idx_vehiclemodel'] = instance.idx_vehiclemodel
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

    def idx_vehiclecategory(self):
        """Get idx_vehiclecategory value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_vehiclecategory']
        return value

    def idx_vehiclemodel(self):
        """Get idx_vehiclemodel value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_vehiclemodel']
        return value

    def vehiclecategory_name(self):
        """Get vehiclecategory vehiclecategory_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['vehiclecategory_name']
        return value

    def enabled(self):
        """Get vehiclecategory enabled.

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
        """Get all vehiclecategory data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_vehiclecategory_exists(idx_vehiclecategory):
    """Determine whether the idx_vehiclecategory exists.

    Args:
        idx_vehiclecategory: idx_vehiclecategory value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_vehiclecategory, int) is False:
        idx_vehiclecategory = None

    # Get information on vehiclecategory from database
    data = GetIDXVehicleCategory(idx_vehiclecategory)
    if data.exists() is True:
        exists = True

    # Return
    return exists
