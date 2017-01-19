"""Module of mdl database functions.

Classes for vehicle data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import Vehicles


class GetIDXVehicle(object):
    """Class to return vehicle data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_vehicle):
        """Function for intializing the class.

        Args:
            idx_vehicle: Vehicle idx_vehicle

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_vehicle', 'license_plate', 'vehicle_seats',
            'vehicle_year', 'rating_value', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_vehicle, int) is False:
            idx_vehicle = None

        # Only work if the value is an integer
        if isinstance(idx_vehicle, int) is True and idx_vehicle is not None:
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(Vehicles).filter(
                Vehicles.idx_vehicle == idx_vehicle)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_vehicle'] = idx_vehicle
                    self.data_dict[
                        'license_plate'] = general.decode(
                            instance.license_plate)
                    self.data_dict['vehicle_year'] = instance.vehicle_year
                    self.data_dict['vehicle_seats'] = instance.vehicle_seats
                    self.data_dict['rating_value'] = instance.rating_value
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

    def vehicle_seats(self):
        """Get vehicle_seats value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['vehicle_seats']
        return value

    def vehicle_year(self):
        """Get vehicle_year value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['vehicle_year']
        return value

    def rating_value(self):
        """Get rating_value value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['rating_value']
        return value

    def license_plate(self):
        """Get vehicle license_plate.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['license_plate']
        return value

    def enabled(self):
        """Get vehicle enabled.

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
        """Get all vehicle data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_vehicle_exists(idx_vehicle):
    """Determine whether the idx_vehicle exists.

    Args:
        idx_vehicle: idx_vehicle value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_vehicle, int) is False:
        idx_vehicle = None

    # Get information on vehicle from database
    data = GetIDXVehicle(idx_vehicle)
    if data.exists() is True:
        exists = True

    # Return
    return exists
