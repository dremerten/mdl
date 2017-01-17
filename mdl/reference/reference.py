#!/usr/bin/env python3
"""mdl Agent class.

Description:

    This script:
        1) Processes a variety of information from agents
        2) Posts the data using HTTP to a server listed
           in the configuration file

"""
# Standard libraries
import os
import tempfile
from collections import defaultdict
from copy import deepcopy
import json

# pip3 libraries
import requests

# mdl libraries
from mdl.utils import log
from mdl.utils import general
from mdl.utils.configuration import Config


class ReferenceSampleConfig(Config):
    """Class gathers all configuration information."""

    def __init__(self, agent_name='_MDL_TEST_'):
        """Function for intializing the class.

        Args:
            agent_name: Name of agent

        Returns:
            None

        """
        # Initialize key variables
        Config.__init__(self)
        self.prefix = agent_name

    def agent_cache_directory(self):
        """Determine the agent_cache_directory.

        This is where the agent will temporarily store its data in the
        event it cannot contact the API. When contact returns all data
        cached in this directory will be posted to the API and deleted.

        Args:
            None

        Returns:
            result: configured agent_cache_directory

        """
        # Initialize key variables
        result = tempfile.mkdtemp(prefix=self.prefix)

        # Return
        return result

    def agent_name(self):
        """Get agent_name.

        The name of the agent that will be included in the JSON data posted
        to the API.

        Args:
            None

        Returns:
            result: result

        """
        # Get result
        result = self.prefix
        return result


class ReferenceSampleAPI(object):
    """Class used to GET and POST data to the mdl API."""

    def __init__(self, config):
        """Function for intializing the class.

        Args:
            config: ConfigAgent object

        Returns:
            None

        """
        # Initialize key variables
        self.config = config
        self.url_prefix = infoset_api_url_prefix(config)

    def _url(self, uri):
        """Create API URL.

        Args:
            uri: URI to append to prefix

        Returns:
            result: Full URL to process

        """
        # Fix URI string
        fixed_uri = uri.lstrip('/').rstrip('/')

        # Create API URL
        result = ('%s/%s') % (self.url_prefix, fixed_uri)
        return result

    def get(self, uri):
        """Get API data.

        Args:
            uri: URI to retrieve excluding the API prefix.

        Returns:
            data: Result of query

        """
        # Initialize key variables
        data = None

        # Create API URL
        url = self._url(uri)

        # Return data
        try:
            result = requests.get(url)
            data = result.json()
        except:
            data = None

        # Return
        return data

    def post(self, uri, data):
        """Post API data.

        Args:
            uri: URI to retrieve excluding the API prefix.

        Returns:
            _data: Result of query

        """
        # Initialize key variables
        success = False

        # Create API URL
        url = self._url(uri)
        try:
            result = requests.post(url, json=data)
            response = True
        except:
            response = False

        # Define success
        if response is True:
            if result.status_code == 200:
                success = True

        # Retun
        return success


class ReferenceSampleAgent(object):
    """mdl reference agent class for retreiving and posting data."""

    def __init__(self, config, devicename, id_agent, timestamp=None):
        """Method initializing the class.

        Args:
            config: ConfigAgent configuration object
            agent_name: Name of agent
            devicename: Devicename that the agent applies to
            id_agent: ID of the agent running on the device
            timestamp: The timestamp that should be used

        Returns:
            None

        """
        # Initialize key variables
        self.data = defaultdict(lambda: defaultdict(dict))
        agent_name = config.agent_name()

        # Add timestamp
        if timestamp is None:
            self.data['timestamp'] = general.normalized_timestamp()
        else:
            self.data['timestamp'] = int(timestamp)
        self.data['id_agent'] = id_agent
        self.data['agent'] = agent_name
        self.data['devicename'] = devicename

        # Create an object for API interaction
        self._api = ReferenceSampleAPI(config)

        # Create the cache directory
        self.cache_dir = config.agent_cache_directory()
        if os.path.exists(self.cache_dir) is False:
            os.mkdir(self.cache_dir)

        # All cache files created by this agent will end with this suffix.
        devicehash = general.hashstring(self.data['devicename'], sha=1)
        self.cache_suffix = ('%s_%s.json') % (id_agent, devicehash)

    def name(self):
        """Return the name of the agent.

        Args:
            None

        Returns:
            value: Name of agent

        """
        # Return
        value = self.data['agent']
        return value

    def populate(self, data_in):
        """Populate data for agent to eventually send to server.

        Args:
            data_in: dict of datapoint values from agent
            timeseries: TimeSeries data if True

        Returns:
            None

        """
        # Initialize data
        data = deepcopy(data_in)

        # Validate base_type
        if len(data) != 1 or isinstance(data, defaultdict) is False:
            log_message = ('Agent data "%s" is invalid') % (data)
            log.log2die(1005, log_message)

        ######################################################################
        # Get a description to use for label value. You could do a lookup in
        # a table based on the spoken language of the environment based on the
        # label and assign the translated result to data[label]['description']
        ######################################################################
        for label in data.keys():
            data[label]['description'] = label
            break

        # Add data to appropriate self.data key
        if data[label]['base_type'] is not None:
            self.data['timeseries'].update(data)
        else:
            self.data['timefixed'].update(data)

    def populate_single(self, label, value, base_type=None, source=None):
        """Add a single value to the data to be posted by the agent.

        Args:
            label: Agent label for data. A unique descriptive label for
                    the datapoint. This could be a string like
                    "Percent memory used" or a coded value like
                    "pct_mem_used" that could be used as a key in a
                    lookup table for multilanguage support.
            value: Value of data
            base_type: Base type of data. Modeled on SNMP style base_type
                (integer, counter32, etc.) Valid values include:
                None: String data
                1: Gauge or point in time data like "Percentage memory used"
                32: 32 bit counter data "Packets seen since booting"
                64: 63 bit counter data "Packets seen since booting"
            source: Source of the data as a string. This helps to identify
                where the data was found. For example "Interface eth0"

        Returns:
            None

        """
        # Initialize key variables
        data = defaultdict(lambda: defaultdict(dict))
        data[label]['base_type'] = base_type
        data[label]['data'] = [[0, value, source]]

        # Update
        self.populate(data)

    def populate_named_tuple(self, named_tuple, prefix='', base_type=1):
        """Post system data to the central server.

        Args:
            named_tuple: Named tuple with data values. Format of the tuple
                should be:
                (key1=value1, key2=value2, key3=value3, ...)
                An example of this would be the results of "psutil.cpu_times()"
            prefix: Prefix to append to data keys when populating the agent
            base_type: Base type of data. Modeled on SNMP style base_type
                (integer, counter32, etc.) Valid values include:
                None: String data
                1: Gauge or point in time data like "Percentage memory used"
                32: 32 bit counter data "Packets seen since booting"
                64: 63 bit counter data "Packets seen since booting"

        Returns:
            None

        """
        # Get data
        system_dict = named_tuple._asdict()
        for label, value in system_dict.items():
            # Convert the dict to two dimensional dict keyed by [label][source]
            # for use by self.populate_dict
            if (bool(prefix)) is True:
                new_label = ('%s_%s') % (prefix, label)
            else:
                new_label = label

            # Initialize data
            data = defaultdict(lambda: defaultdict(dict))

            # Add data
            data[new_label]['data'] = [[0, value, None]]
            data[new_label]['base_type'] = base_type

            # Update
            self.populate(data)

    def populate_dict(self, data_in, prefix='', base_type=1):
        """Populate agent with data that's a dict keyed by [label][source].

        Args:
            data_in: Dict of data to post "X[label][source] = value"
                where:
                    label = A unique descriptive label for the datapoint.
                        This could be a string like "Percent memory used" or
                        a coded value like "pct_mem_used" that could be used
                        as a key in a lookup table for multilanguage support.
                    source = Source of the data as a string. This helps to
                        identify where the data was found. For example
                        "Interface eth0"
            prefix: Prefix to append to data keys when populating the agent
            base_type: Base type of data. Modeled on SNMP style base_type
                (integer, counter32, etc.) Valid values include:
                None: String data
                1: Gauge or point in time data like "Percentage memory used"
                32: 32 bit counter data "Packets seen since booting"
                64: 63 bit counter data "Packets seen since booting"

        Returns:
            None

        """
        # Initialize data
        data_input = deepcopy(data_in)

        # Iterate over labels
        for label in data_input.keys():
            # Initialize tuple list to use by agent.populate
            value_sources = []
            if (bool(prefix)) is True:
                new_label = ('%s_%s') % (prefix, label)
            else:
                new_label = label

            # Initialize data
            data = defaultdict(lambda: defaultdict(dict))
            data[new_label]['base_type'] = base_type

            # Append to tuple list
            # (Sorting is important to keep consistent ordering)
            for source, value in sorted(data_input[label].items()):
                value_sources.append(
                    [source, value, source]
                )
            data[new_label]['data'] = value_sources

            # Update
            self.populate(data)

    def polled_data(self):
        """Return data that should be posted.

        Args:
            None

        Returns:
            None

        """
        # Return
        return self.data

    def post(self, save=True, data=None):
        """Post data to central server.

        Args:
            save: When True, save data to cache directory if postinf fails
            data: Data to post. If None, then uses self.data

        Returns:
            success: "True: if successful

        """
        # Initialize key variables
        success = False
        timestamp = self.data['timestamp']
        id_agent = self.data['id_agent']

        # Create data to post
        if data is None:
            data = self.data

        # Post data save to cache if this fails
        uri = ('/receive/%s') % (id_agent)
        success = self._api.post(uri, data)

        # Log message
        if success is True:
            log_message = (
                'Agent "%s" successfully contacted server'
                '') % (self.name())
            log.log2info(1012, log_message)
        else:
            # Save data if requested
            if save is True:
                # Create a unique very long filename to reduce risk of
                filename = ('%s/%s_%s.json') % (
                    self.cache_dir, timestamp, self.cache_suffix)

                # Save data
                with open(filename, 'w') as f_handle:
                    json.dump(data, f_handle)

            # Log message
            log_message = (
                'Agent "%s" failed to contact server'
                '') % (self.name())
            log.log2warning(1013, log_message)

        # Return
        return success

    def purge(self):
        """Purge data from cache by posting to central server.

        Args:
            None

        Returns:
            success: "True: if successful

        """
        # Initialize key variables
        id_agent = self.data['id_agent']

        # Add files in cache directory to list only if they match the
        # cache suffix
        all_filenames = [filename for filename in os.listdir(
            self.cache_dir) if os.path.isfile(
                os.path.join(self.cache_dir, filename))]
        filenames = [
            filename for filename in all_filenames if filename.endswith(
                self.cache_suffix)]

        # Read cache file in sorted order.
        # NOTE: We must post data in timestamp sorted order.
        for filename in filenames.sorted():
            # Only post files for our own UID value
            if id_agent not in filename:
                continue

            # Get the full filepath for the cache file and post
            filepath = os.path.join(self.cache_dir, filename)
            with open(filepath, 'r') as f_handle:
                try:
                    data = json.load(f_handle)
                except:
                    # Log removal
                    log_message = (
                        'Error reading previously cached agent data file %s '
                        'for agent %s. May be corrupted.'
                        '') % (filepath, self.name())
                    log.log2die(1058, log_message)

            # Post file
            success = self.post(save=False, data=data)

            # Delete file if successful
            if success is True:
                os.remove(filepath)

                # Log removal
                log_message = (
                    'Purging cache file %s after successfully '
                    'contacting server'
                    '') % (filepath)
                log.log2info(1014, log_message)


def infoset_api_url_prefix(config):
    """Create the URL prefix to communicate with the Infoset server.

    Args:
        config: Config configuration object

    Returns:
        url_prefix: The URL prefix

    """
    # Create API URL
    fixed_uri = config.infoset_server_uri().lstrip('/').rstrip('/')
    if config.infoset_server_https() is True:
        prefix = 'https'
    else:
        prefix = 'http'

    # Return
    url_prefix = (
        '%s://%s:%s/%s'
        '') % (
            prefix, config.infoset_server_name(),
            config.infoset_server_port(), fixed_uri)
    return url_prefix
