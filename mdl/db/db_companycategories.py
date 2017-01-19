"""Module of mdl database functions.

Classes for companycategory data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import CompanyCategories


class GetIDXCompanyCategory(object):
    """Class to return companycategory data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_companycategory):
        """Function for intializing the class.

        Args:
            idx_companycategory: CompanyCategory idx_companycategory

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_companycategory', 'companycategory_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_companycategory, int) is False:
            idx_companycategory = None

        # Only work if the value is an integer
        if isinstance(idx_companycategory, int) is (
                True and idx_companycategory is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(CompanyCategories).filter(
                CompanyCategories.idx_companycategory == idx_companycategory)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_companycategory'] = idx_companycategory
                    self.data_dict[
                        'companycategory_name'] = general.decode(
                            instance.companycategory_name)
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

    def idx_companycategory(self):
        """Get idx_companycategory value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_companycategory']
        return value

    def companycategory_name(self):
        """Get companycategory companycategory_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['companycategory_name']
        return value

    def enabled(self):
        """Get companycategory enabled.

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
        """Get all companycategory data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_companycategory_exists(idx_companycategory):
    """Determine whether the idx_companycategory exists.

    Args:
        idx_companycategory: idx_companycategory value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_companycategory, int) is False:
        idx_companycategory = None

    # Get information on companycategory from database
    data = GetIDXCompanyCategory(idx_companycategory)
    if data.exists() is True:
        exists = True

    # Return
    return exists
