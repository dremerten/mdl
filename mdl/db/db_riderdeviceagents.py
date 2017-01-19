"""Module of mdl database functions. RiderDeviceAgents table."""

# Python standard libraries
from collections import defaultdict

# Python libraries
from sqlalchemy import and_

# Infoset libraries
from mdl.db import db
from mdl.db.db_orm import RiderDeviceAgents


class GetIDXRiderDeviceAgents(object):
    """Class to return riderdeviceagent data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_riderdeviceagent):
        """Function for intializing the class.

        Args:
            idx_riderdeviceagent: RiderDeviceAgents idx_riderdeviceagent

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_riderdeviceagent', 'idx_agent', 'enabled', 'idx_riderdevice']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_riderdeviceagent, int) is False:
            idx_riderdeviceagent = None

        # Only work if the value is an integer
        if isinstance(idx_riderdeviceagent, int) is True and (
                idx_riderdeviceagent is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(RiderDeviceAgents).filter(
                RiderDeviceAgents.idx_riderdeviceagent == idx_riderdeviceagent)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict[
                        'idx_riderdeviceagent'] = idx_riderdeviceagent
                    self.data_dict['idx_agent'] = instance.idx_agent
                    self.data_dict['enabled'] = bool(instance.enabled)
                    self.data_dict[
                        'idx_riderdevice'] = instance.idx_riderdevice
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

    def idx_riderdeviceagent(self):
        """Get idx_riderdeviceagent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_riderdeviceagent']
        return value

    def idx_agent(self):
        """Get idx_agent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_agent']
        return value

    def enabled(self):
        """Get agent enabled.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['enabled']

        # Return
        return value

    def idx_riderdevice(self):
        """Get agent idx_riderdevice.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_riderdevice']
        return value

    def everything(self):
        """Get all agent data.

        Args:
            None

        Returns:
            value: Data as a dict

        """
        # Initialize key variables
        value = self.data_dict
        return value


class GetRiderDeviceAgents(object):
    """Class to return RiderDeviceAgents data by device and agent idx.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_riderdevice, idx_agent):
        """Method initializing the class.

        Args:
            idx_riderdevice: Device idx
            idx_agent: Agent idx

        Returns:
            None

        """
        # Initialize key variables
        self.data_dict = defaultdict(dict)
        keys = ['last_timestamp', 'idx_riderdeviceagent', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_riderdevice, int) is False:
            idx_riderdevice = None
        if isinstance(idx_agent, int) is False:
            idx_agent = None

        # Establish a database session
        database = db.Database()
        session = database.session()
        result = session.query(RiderDeviceAgents).filter(and_(
            RiderDeviceAgents.idx_riderdevice == idx_riderdevice,
            RiderDeviceAgents.idx_agent == idx_agent))

        # Massage data
        if result.count() == 1:
            for instance in result:
                self.data_dict['last_timestamp'] = instance.last_timestamp
                self.data_dict[
                    'idx_riderdeviceagent'] = instance.idx_riderdeviceagent
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

    def enabled(self):
        """Get enabled value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['enabled']
        return value

    def last_timestamp(self):
        """Get last_timestamp value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['last_timestamp']
        return value

    def idx_riderdeviceagent(self):
        """Get idx_riderdeviceagent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_riderdeviceagent']
        return value


def idx_riderdeviceagent_exists(idx_riderdeviceagent):
    """Determine whether the idx_riderdeviceagent exists.

    Args:
        idx_riderdeviceagent: idx_riderdeviceagent value for datapoint

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_riderdeviceagent, int) is False:
        idx_riderdeviceagent = None

    # Get information on riderdeviceagent from database
    data = GetIDXRiderDeviceAgents(idx_riderdeviceagent)
    if data.exists() is True:
        exists = True

    # Return
    return exists


def device_agent_exists(idx_riderdevice, idx_agent):
    """Determine whether a entry exists in the RiderDeviceAgents table.

    Args:
        idx_riderdevice: Device idx
        idx_agent: Agent idx

    Returns:
        found: True if found

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_riderdevice, int) is False:
        idx_riderdevice = None
    if isinstance(idx_agent, int) is False:
        idx_agent = None

    # Get information on agent from database
    data = GetRiderDeviceAgents(idx_riderdevice, idx_agent)
    if data.exists() is True:
        exists = True

    # Return
    return exists


def all_device_indices():
    """Get list of all device indexes in database.

    Args:
        None

    Returns:
        listing: List of indexes

    """
    idx_list = []

    # Establish a database session
    database = db.Database()
    session = database.session()
    result = session.query(RiderDeviceAgents.idx_riderdevice)

    # Add to the list of device idx values
    for instance in result:
        idx_list.append(instance.idx_riderdevice)

    # Return the session to the pool after processing
    database.close()

    # Return
    return list(set(idx_list))


def device_indices(idx_agent):
    """Get list of all device indexes for a specific agent_idx.

    Args:
        None

    Returns:
        listing: List of indexes

    """
    idx_list = []

    # Fix values passed
    if isinstance(idx_agent, int) is False:
        idx_agent = None

    # Establish a database session
    database = db.Database()
    session = database.session()
    result = session.query(RiderDeviceAgents.idx_riderdevice).filter(
        RiderDeviceAgents.idx_agent == idx_agent)

    # Add to the list of device idx values
    for instance in result:
        idx_list.append(instance.idx_riderdevice)

    # Return the session to the pool after processing
    database.close()

    # Return
    return list(set(idx_list))


def agent_indices(idx_riderdevice):
    """Get list of all agent indexes for a specific device_idx.

    Args:
        None

    Returns:
        listing: List of indexes

    """
    idx_list = []

    # Fix values passed
    if isinstance(idx_riderdevice, int) is False:
        idx_riderdevice = None

    # Establish a database session
    database = db.Database()
    session = database.session()
    result = session.query(RiderDeviceAgents.idx_agent).filter(
        RiderDeviceAgents.idx_riderdevice == idx_riderdevice)

    # Add to the list of device idx values
    for instance in result:
        idx_list.append(instance.idx_agent)

    # Return the session to the pool after processing
    database.close()

    # Return
    return idx_list


def get_all_device_agents():
    """Get list of all RiderDeviceAgents indexes.

    Args:
        None

    Returns:
        listing: List of indexes

    """
    data = []

    # Establish a database session
    database = db.Database()
    session = database.session()
    result = session.query(RiderDeviceAgents)

    # Add to the list of device idx values
    for instance in result:
        data_dict = {}
        data_dict['idx_riderdeviceagent'] = instance.idx_riderdeviceagent
        data_dict['idx_agent'] = instance.idx_agent
        data_dict['idx_riderdevice'] = instance.idx_riderdevice
        data.append(data_dict)

    # Return the session to the pool after processing
    database.close()

    # Return
    return data
