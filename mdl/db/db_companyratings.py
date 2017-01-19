"""Module of mdl database functions.

Classes for companyrating data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.db import db
from mdl.db.db_orm import CompanyRatingss


class GetIDXCompanyRatings(object):
    """Class to return companyrating data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_companyrating):
        """Function for intializing the class.

        Args:
            idx_companyrating: CompanyRatings idx_companyrating

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_companyrating', 'rating_value', 'rating_timestamp',
            'idx_company', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_companyrating, int) is False:
            idx_companyrating = None

        # Only work if the value is an integer
        if (isinstance(idx_companyrating, int) is True) and (
                idx_companyrating is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(CompanyRatingss).filter(
                CompanyRatingss.idx_companyrating == idx_companyrating)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_companyrating'] = idx_companyrating
                    self.data_dict['rating_value'] = instance.rating_value
                    self.data_dict['idx_company'] = instance.idx_company
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

    def idx_companyrating(self):
        """Get idx_companyrating value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_companyrating']
        return value

    def idx_company(self):
        """Get idx_company value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_company']
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
        """Get companyrating rating_value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['rating_value']
        return value

    def enabled(self):
        """Get companyrating enabled.

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
        """Get all companyrating data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_companyrating_exists(idx_companyrating):
    """Determine whether the idx_companyrating exists.

    Args:
        idx_companyrating: idx_companyrating value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_companyrating, int) is False:
        idx_companyrating = None

    # Get information on companyrating from database
    data = GetIDXCompanyRatings(idx_companyrating)
    if data.exists() is True:
        exists = True

    # Return
    return exists
