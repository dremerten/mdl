"""Module of mdl database functions.

Classes for creditcard data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.db import db
from mdl.db.db_orm import CreditCards


class GetIDXCreditCard(object):
    """Class to return creditcard data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_creditcard):
        """Function for intializing the class.

        Args:
            idx_creditcard: CreditCard idx_creditcard

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_creditcard', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_creditcard, int) is False:
            idx_creditcard = None

        # Only work if the value is an integer
        if isinstance(idx_creditcard, int) is True and (
                idx_creditcard is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(CreditCards).filter(
                CreditCards.idx_creditcard == idx_creditcard)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_creditcard'] = idx_creditcard
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

    def idx_creditcard(self):
        """Get idx_creditcard value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_creditcard']
        return value

    def enabled(self):
        """Get creditcard enabled.

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
        """Get all creditcard data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_creditcard_exists(idx_creditcard):
    """Determine whether the idx_creditcard exists.

    Args:
        idx_creditcard: idx_creditcard value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_creditcard, int) is False:
        idx_creditcard = None

    # Get information on creditcard from database
    data = GetIDXCreditCard(idx_creditcard)
    if data.exists() is True:
        exists = True

    # Return
    return exists
