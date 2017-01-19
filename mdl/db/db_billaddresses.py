"""Module of mdl database functions.

Classes for geocity data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import BillAddresses


class GetIDXBillAddress(object):
    """Class to return geocity data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_billaddress):
        """Function for intializing the class.

        Args:
            idx_billaddress: BillAddress idx_billaddress

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_billaddress', 'idx_geocity', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_billaddress, int) is False:
            idx_billaddress = None

        # Only work if the value is an integer
        if isinstance(idx_billaddress, int) is True and idx_billaddress is not None:
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(BillAddresses).filter(
                BillAddresses.idx_billaddress == idx_billaddress)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_billaddress'] = idx_billaddress
                    self.data_dict['idx_geocity'] = instance.idx_geocity
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

    def idx_billaddress(self):
        """Get idx_billaddress value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_billaddress']
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


def idx_billaddress_exists(idx_billaddress):
    """Determine whether the idx_billaddress exists.

    Args:
        idx_billaddress: idx_billaddress value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_billaddress, int) is False:
        idx_billaddress = None

    # Get information on geocity from database
    data = GetIDXBillAddress(idx_billaddress)
    if data.exists() is True:
        exists = True

    # Return
    return exists
