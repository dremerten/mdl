"""Module of mdl database functions.

Classes for agentname data

"""
# Python standard libraries
from collections import defaultdict

# mdl libraries
from mdl.utils import general
from mdl.db import db
from mdl.db.db_orm import AgentNames


class GetIDXAgentName(object):
    """Class to return agentname data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_agentname):
        """Function for intializing the class.

        Args:
            idx_agentname: AgentName idx_agentname

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_agentname', 'agent_name', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_agentname, int) is False:
            idx_agentname = None

        # Only work if the value is an integer
        if (isinstance(idx_agentname, int) is True) and (
                idx_agentname is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(AgentNames).filter(
                AgentNames.idx_agentname == idx_agentname)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict['idx_agentname'] = idx_agentname
                    self.data_dict[
                        'agent_name'] = general.decode(instance.agent_name)
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

    def idx_agentname(self):
        """Get idx_agentname value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_agentname']
        return value

    def agent_name(self):
        """Get agentname agent_name.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['agent_name']
        return value

    def enabled(self):
        """Get agentname enabled.

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
        """Get all agentname data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


def idx_agentname_exists(idx_agentname):
    """Determine whether the idx_agentname exists.

    Args:
        idx_agentname: idx_agentname value

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_agentname, int) is False:
        idx_agentname = None

    # Get information on agentname from database
    data = GetIDXAgentName(idx_agentname)
    if data.exists() is True:
        exists = True

    # Return
    return exists
