"""Module of mdl database functions.

Classes for model data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import VehicleModels


class GetIDXVehicleModel(object):
    """Class to return model data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_vehiclemodel):
        """Function for intializing the class.

        Args:
            idx_vehiclemodel: VehicleModel idx_vehiclemodel

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_vehiclemodel', 'idx_vehiclemake, ''model_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_vehiclemodel, int) is False:
            idx_vehiclemodel = None

        # Only work if the value is an integer
        if (isinstance(idx_vehiclemodel, int) is True) and (
                idx_vehiclemodel is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(VehicleModels).filter(
                VehicleModels.idx_vehiclemodel == idx_vehiclemodel)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_vehiclemodel'] = idx_vehiclemodel
                    self.data_dict[
                        'idx_vehiclemake'] = instance.idx_vehiclemake
                    self.data_dict[
                        'model_name'] = general.decode(instance.model_name)
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

    def idx_vehiclemake(self):
        """Get idx_vehiclemake value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_vehiclemake']
        return value

    def model_name(self):
        """Get model model_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['model_name']
        return value

    def enabled(self):
        """Get model enabled.

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
        """Get all model data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_vehiclemodel_exists(idx_vehiclemodel):
    """Determine whether the idx_vehiclemodel exists.

    Args:
        idx_vehiclemodel: idx_vehiclemodel value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_vehiclemodel, int) is False:
        idx_vehiclemodel = None

    # Get information on model from database
    data = GetIDXVehicleModel(idx_vehiclemodel)
    if data.exists() is True:
        exists = True

    # Return
    return exists
