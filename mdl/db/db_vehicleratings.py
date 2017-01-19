"""Module of mdl database functions.

Classes for vehicleratings data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.db import db
from mdl.db.db_orm import VehicleRatings


class GetIDXVehicleRatings(object):
    """Class to return vehicleratings data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_vehiclerating):
        """Function for intializing the class.

        Args:
            idx_vehiclerating: VehicleRatings idx_vehiclerating

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_vehiclerating', 'rating_value', 'rating_timestamp',
            'idx_vehicle', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_vehiclerating, int) is False:
            idx_vehiclerating = None

        # Only work if the value is an integer
        if (isinstance(idx_vehiclerating, int) is True) and (
                idx_vehiclerating is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(VehicleRatings).filter(
                VehicleRatings.idx_vehiclerating == idx_vehiclerating)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_vehiclerating'] = idx_vehiclerating
                    self.data_dict['rating_value'] = instance.rating_value
                    self.data_dict['idx_vehicle'] = instance.idx_vehicle
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

    def idx_vehiclerating(self):
        """Get idx_vehiclerating value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_vehiclerating']
        return value

    def idx_vehicle(self):
        """Get idx_vehicle value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_vehicle']
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
        """Get vehicleratings rating_value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['rating_value']
        return value

    def enabled(self):
        """Get vehicleratings enabled.

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
        """Get all vehicleratings data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_vehiclerating_exists(idx_vehiclerating):
    """Determine whether the idx_vehiclerating exists.

    Args:
        idx_vehiclerating: idx_vehiclerating value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_vehiclerating, int) is False:
        idx_vehiclerating = None

    # Get information on vehicleratings from database
    data = GetIDXVehicleRatings(idx_vehiclerating)
    if data.exists() is True:
        exists = True

    # Return
    return exists
