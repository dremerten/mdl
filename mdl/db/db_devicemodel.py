"""Module of mdl database functions.

Classes for model data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import DeviceModels


class GetIDXDeviceModel(object):
    """Class to return model data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_devicemodel):
        """Function for intializing the class.

        Args:
            idx_devicemodel: DeviceModel idx_devicemodel

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_devicemodel', 'idx_devicemake, ''model_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_devicemodel, int) is False:
            idx_devicemodel = None

        # Only work if the value is an integer
        if (isinstance(idx_devicemodel, int) is True) and (
                idx_devicemodel is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(DeviceModels).filter(
                DeviceModels.idx_devicemodel == idx_devicemodel)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_devicemodel'] = idx_devicemodel
                    self.data_dict[
                        'idx_devicemake'] = instance.idx_devicemake
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

    def idx_devicemake(self):
        """Get idx_devicemake value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_devicemake']
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


def idx_devicemodel_exists(idx_devicemodel):
    """Determine whether the idx_devicemodel exists.

    Args:
        idx_devicemodel: idx_devicemodel value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_devicemodel, int) is False:
        idx_devicemodel = None

    # Get information on model from database
    data = GetIDXDeviceModel(idx_devicemodel)
    if data.exists() is True:
        exists = True

    # Return
    return exists
