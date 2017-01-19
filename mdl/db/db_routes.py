"""Module of mdl database functions.

Classes for route data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import Routes


class GetIDXRoute(object):
    """Class to return route data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_route):
        """Function for intializing the class.

        Args:
            idx_route: Route idx_route

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_route', 'route_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_route, int) is False:
            idx_route = None

        # Only work if the value is an integer
        if isinstance(idx_route, int) is True and idx_route is not None:
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(Routes).filter(
                Routes.idx_route == idx_route)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_route'] = idx_route
                    self.data_dict[
                        'route_name'] = general.decode(instance.route_name)
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

    def idx_route(self):
        """Get idx_route value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_route']
        return value

    def route_name(self):
        """Get route route_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['route_name']
        return value

    def enabled(self):
        """Get route enabled.

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
        """Get all route data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_route_exists(idx_route):
    """Determine whether the idx_route exists.

    Args:
        idx_route: idx_route value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_route, int) is False:
        idx_route = None

    # Get information on route from database
    data = GetIDXRoute(idx_route)
    if data.exists() is True:
        exists = True

    # Return
    return exists
