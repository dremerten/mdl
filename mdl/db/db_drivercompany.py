"""Module of mdl database functions.

Classes for company data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import DriverCompany


class GetIDXDriverCompany(object):
    """Class to return company data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_drivercompany):
        """Function for intializing the class.

        Args:
            idx_drivercompany: DriverCompany idx_drivercompany

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_drivercompany', 'drivercompany_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_drivercompany, int) is False:
            idx_drivercompany = None

        # Only work if the value is an integer
        if (isinstance(idx_drivercompany, int)) is True and (
                idx_drivercompany is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(DriverCompany).filter(
                DriverCompany.idx_drivercompany == idx_drivercompany)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_drivercompany'] = idx_drivercompany
                    self.data_dict[
                        'drivercompany_name'] = general.decode(
                            instance.drivercompany_name)
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

    def idx_drivercompany(self):
        """Get idx_drivercompany value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_drivercompany']
        return value

    def drivercompany_name(self):
        """Get company drivercompany_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['drivercompany_name']
        return value

    def enabled(self):
        """Get company enabled.

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
        """Get all company data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_drivercompany_exists(idx_drivercompany):
    """Determine whether the idx_drivercompany exists.

    Args:
        idx_drivercompany: idx_drivercompany value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_drivercompany, int) is False:
        idx_drivercompany = None

    # Get information on company from database
    data = GetIDXDriverCompany(idx_drivercompany)
    if data.exists() is True:
        exists = True

    # Return
    return exists
