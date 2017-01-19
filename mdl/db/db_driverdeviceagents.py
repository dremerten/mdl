"""Module of mdl database functions. DriverDeviceAgents table."""

# Python standard libraries
from collections import defaultdict

# Python libraries
from sqlalchemy import and_

# Infoset libraries
from mdl.db import db
from mdl.db.db_orm import DriverDeviceAgents


class GetIDXDriverDeviceAgents(object):
    """Class to return driverdeviceagent data.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_driverdeviceagent):
        """Function for intializing the class.

        Args:
            idx_driverdeviceagent: DriverDeviceAgents idx_driverdeviceagent

        Returns:
            None

        """
        # Initialize important variables
        self.data_dict = defaultdict(dict)
        keys = [
            'idx_driverdeviceagent', 'idx_agent',
            'enabled', 'idx_driverdevice']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_driverdeviceagent, int) is False:
            idx_driverdeviceagent = None

        # Only work if the value is an integer
        if isinstance(idx_driverdeviceagent, int) is True and (
                idx_driverdeviceagent is not None):
            # Get the result
            database = db.Database()
            session = database.session()
            result = session.query(DriverDeviceAgents).filter(
                DriverDeviceAgents.idx_driverdeviceagent == idx_driverdeviceagent)

            # Massage data
            if result.count() == 1:
                for instance in result:
                    self.data_dict[
                        'idx_driverdeviceagent'] = idx_driverdeviceagent
                    self.data_dict['idx_agent'] = instance.idx_agent
                    self.data_dict['enabled'] = bool(instance.enabled)
                    self.data_dict[
                        'idx_driverdevice'] = instance.idx_driverdevice
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

    def idx_driverdeviceagent(self):
        """Get idx_driverdeviceagent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_driverdeviceagent']
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

    def idx_driverdevice(self):
        """Get agent idx_driverdevice.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_driverdevice']
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


class GetDriverDeviceAgents(object):
    """Class to return DriverDeviceAgents data by device and agent idx.

    Args:
        None

    Returns:
        None

    Methods:

    """

    def __init__(self, idx_driverdevice, idx_agent):
        """Method initializing the class.

        Args:
            idx_driverdevice: Device idx
            idx_agent: Agent idx

        Returns:
            None

        """
        # Initialize key variables
        self.data_dict = defaultdict(dict)
        keys = ['last_timestamp', 'idx_driverdeviceagent', 'enabled']
        for key in keys:
            self.data_dict[key] = None
        self.data_dict['exists'] = False

        # Fix values passed
        if isinstance(idx_driverdevice, int) is False:
            idx_driverdevice = None
        if isinstance(idx_agent, int) is False:
            idx_agent = None

        # Establish a database session
        database = db.Database()
        session = database.session()
        result = session.query(DriverDeviceAgents).filter(and_(
            DriverDeviceAgents.idx_driverdevice == idx_driverdevice,
            DriverDeviceAgents.idx_agent == idx_agent))

        # Massage data
        if result.count() == 1:
            for instance in result:
                self.data_dict['last_timestamp'] = instance.last_timestamp
                self.data_dict[
                    'idx_driverdeviceagent'] = instance.idx_driverdeviceagent
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

    def idx_driverdeviceagent(self):
        """Get idx_driverdeviceagent value.

        Args:
            None

        Returns:
            value: Value to return

        """
        # Initialize key variables
        value = self.data_dict['idx_driverdeviceagent']
        return value


def idx_driverdeviceagent_exists(idx_driverdeviceagent):
    """Determine whether the idx_driverdeviceagent exists.

    Args:
        idx_driverdeviceagent: idx_driverdeviceagent value for datapoint

    Returns:
        exists: True if exists

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_driverdeviceagent, int) is False:
        idx_driverdeviceagent = None

    # Get information on driverdeviceagent from database
    data = GetIDXDriverDeviceAgents(idx_driverdeviceagent)
    if data.exists() is True:
        exists = True

    # Return
    return exists


def device_agent_exists(idx_driverdevice, idx_agent):
    """Determine whether a entry exists in the DriverDeviceAgents table.

    Args:
        idx_driverdevice: Device idx
        idx_agent: Agent idx

    Returns:
        found: True if found

    """
    # Initialize key variables
    exists = False

    # Fix values passed
    if isinstance(idx_driverdevice, int) is False:
        idx_driverdevice = None
    if isinstance(idx_agent, int) is False:
        idx_agent = None

    # Get information on agent from database
    data = GetDriverDeviceAgents(idx_driverdevice, idx_agent)
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
    result = session.query(DriverDeviceAgents.idx_driverdevice)

    # Add to the list of device idx values
    for instance in result:
        idx_list.append(instance.idx_driverdevice)

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
    result = session.query(DriverDeviceAgents.idx_driverdevice).filter(
        DriverDeviceAgents.idx_agent == idx_agent)

    # Add to the list of device idx values
    for instance in result:
        idx_list.append(instance.idx_driverdevice)

    # Return the session to the pool after processing
    database.close()

    # Return
    return list(set(idx_list))


def agent_indices(idx_driverdevice):
    """Get list of all agent indexes for a specific device_idx.

    Args:
        None

    Returns:
        listing: List of indexes

    """
    idx_list = []

    # Fix values passed
    if isinstance(idx_driverdevice, int) is False:
        idx_driverdevice = None

    # Establish a database session
    database = db.Database()
    session = database.session()
    result = session.query(DriverDeviceAgents.idx_agent).filter(
        DriverDeviceAgents.idx_driverdevice == idx_driverdevice)

    # Add to the list of device idx values
    for instance in result:
        idx_list.append(instance.idx_agent)

    # Return the session to the pool after processing
    database.close()

    # Return
    return idx_list


def get_all_device_agents():
    """Get list of all DriverDeviceAgents indexes.

    Args:
        None

    Returns:
        listing: List of indexes

    """
    data = []

    # Establish a database session
    database = db.Database()
    session = database.session()
    result = session.query(DriverDeviceAgents)

    # Add to the list of device idx values
    for instance in result:
        data_dict = {}
        data_dict['idx_driverdeviceagent'] = instance.idx_driverdeviceagent
        data_dict['idx_agent'] = instance.idx_agent
        data_dict['idx_driverdevice'] = instance.idx_driverdevice
        data.append(data_dict)

    # Return the session to the pool after processing
    database.close()

    # Return
    return data
