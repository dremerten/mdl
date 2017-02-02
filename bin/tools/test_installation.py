#!/usr/bin/env python3

"""mdl ingest cache daemon.

Extracts agent data from cache directory files.

"""

# Standard libraries
import sys
import os
import random
from collections import defaultdict
from datetime import datetime
from pprint import pprint
import argparse
import requests

# Try to create a working PYTHONPATH
script_directory = os.path.dirname(os.path.realpath(__file__))
bin_directory = os.path.abspath(os.path.join(script_directory, os.pardir))
root_directory = os.path.abspath(os.path.join(bin_directory, os.pardir))
if script_directory.endswith('/mdl/bin/tools') is True:
    sys.path.append(root_directory)
else:
    print(
        'This script is not installed in the "mdl/bin/tools" '
        'directory. Please fix.')
    sys.exit(2)

# mdl libraries
try:
    from mdl.reference import reference
except:
    print('You need to set your PYTHONPATH to include the mdl library')
    sys.exit(2)
from mdl.utils import log
from mdl.utils import general


class _APItest(object):
    """Class to test basic functionality of APIs."""

    def __init__(self,):
        """Function for intializing the class."""
        # Initialize key variables
        self. agent_name = 'DoRoad'
        self.devicenames = ['+1 876-927-1680', '+1 876-927-1660']
        self.config = reference.ReferenceSampleConfig(self.agent_name)

    def mdl_get(self,):
        """Get posted data from mdl."""
        # Intialize key variables

        # Get infoset URI to process
        uri = 'mobile/get/coordinates/lastcontactdrivers'
        url = '{}/{}'.format(_mdl_api_url_prefix(self.config), uri)
        print(url)

        try:
            result = requests.get(url)
            data = result.json()
        except:
            data = None

        # Report posting success
        if data is not None:
            # Print data posted to screen
            print('')
            pprint(data)
            print('')

    def mdl_post(self,):
        """Post to mdl directly."""
        # Initialize key variables
        success = False

        # Timestamps sent to infoset must be normalized integers. Ie. rounded
        # to the nearest Config.interval() value
        utc_timestamp = general.normalized_timestamp(
            int(datetime.utcnow().timestamp()))

        # Post data for each devicename
        for devicename in self.devicenames:
            # Create an id for the agent running on the device
            id_agent = self._id_agent(devicename)

            # Create dict to post
            data_dict = {}
            data_dict['utc_timestamp'] = utc_timestamp
            data_dict['latitude'] = round(random.uniform(1.5, 1.9), 7)
            data_dict['longitude'] = round(random.uniform(1.5, 1.9), 7)
            data_dict['devicename'] = devicename
            data_dict['name'] = self.agent_name
            data_dict['id_agent'] = id_agent

            # Create API URL
            uri = 'mobile/post/drivercoordinates'
            url = '{}/{}'.format(_mdl_api_url_prefix(self.config), uri)
            print(url)
            try:
                result = requests.post(url, json=data_dict)
                response = True
            except:
                response = False

            # Define success
            if response is True:
                if result.status_code == 200:
                    success = True

            # Report posting success
            if success is True:
                # Print data posted to screen
                print('')
                pprint(data_dict)
                print('')

                # Log success
                log_message = (
                    'Successfully posted test data for {}'
                    ''.format(devicename))
                log.log2see(1055, log_message)

            else:
                # Log success
                log_message = (
                    'Failed to post data for {}. '
                    'Make sure the mdl API is running.'
                    ''.format(devicename))
                log.log2see(1056, log_message)

    def infoset_get(self,):
        """Get posted data from infoset."""
        # Initialize key variables
        lookuptable = defaultdict(lambda: defaultdict(dict))
        report = []

        # Get the most recent values from infoset database
        api = reference.ReferenceSampleAPI(self.config)
        uri = ('/lastcontacts')
        lastcontacts = api.get(uri)

        # Get the datapoint summary
        uri = ('/datapoints/all/summary')
        datapointsummary = api.get(uri)

        # Create a lookup table for datapoints
        if bool(datapointsummary) is True:
            for item in datapointsummary:
                idx_datapoint = item['idx_datapoint']
                for key, value in item.items():
                    if key != 'idx_datapoint':
                        lookuptable[idx_datapoint][key] = value

            # Create report
            for item in lastcontacts:
                # Assign values
                idx_datapoint = item['idx_datapoint']
                data_dict = {}
                data_dict['idx_datapoint'] = idx_datapoint
                data_dict['value'] = item['value']
                data_dict['timestamp'] = item['timestamp']
                for key, value in lookuptable[idx_datapoint].items():
                    data_dict[key] = value

                # Append to report
                report.append(data_dict)

            # Create report
            print('')
            pprint(report)
            print('')

    def infoset_post(self,):
        """Post to infoset directly."""
        # Post data for each devicename
        for devicename in self.devicenames:
            # Create an id for the agent running on the device
            id_agent = self._id_agent(devicename)

            # Instantiate object to post data
            report = reference.ReferenceSampleAgent(
                self.config, devicename, id_agent)

            # Populate data and post
            report.populate_single(
                'latitude',
                round(random.uniform(1.5, 1.9), 7),
                base_type=1, source='GPS')
            report.populate_single(
                'longitude',
                round(random.uniform(1.5, 1.9), 7),
                base_type=1, source='GPS')
            success = report.post()

            # Report posting success
            if success is True:
                # Print data posted to screen
                print('')
                pprint(report.polled_data())
                print('')

                # Log success
                log_message = (
                    'Successfully posted test data for {}. '
                    ''.format(devicename))
                log.log2see(1057, log_message)

            else:
                # Log success
                log_message = (
                    'Failed to post data for {}. '
                    'Make sure the infoset-ng API is running.'
                    ''.format(devicename))
                log.log2see(1059, log_message)

    def _id_agent(self, devicename):
        """Generate an id_agent for a device.

        Args:
            devicename: Name of device

        Returns:
            id_agent: ID agent to use

        """
        # Get ID agent to use
        id_agent = general.hashstring('{}_SIM_CARD_ID'.format(devicename))
        return id_agent


def _mdl_api_url_prefix(config):
    """Create the URL prefix to communicate with the Infoset server.

    Args:
        config: Config configuration object

    Returns:
        url_prefix: The URL prefix

    """
    # Create API URL
    if config.mdl_server_https() is True:
        prefix = 'https'
    else:
        prefix = 'http'

    # Return
    url_prefix = (
        '%s://%s:%s/%s'
        '') % (
            prefix, config.mdl_server_name(),
            config.bind_port(), config.mdl_server_uri())
    return url_prefix


def cli():
    """Class gathers all CLI information.

    Args:
        None

    Returns:
        args: Namespace() containing all of our CLI arguments as objects

    """
    # Initialize key variables
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest='action')

    # Parse infoset parameters
    api_infoset = subparsers.add_parser(
        'infoset', help='Interactions with Infoset')
    api_infoset.add_argument(
        '--post', action='store_true', help='Post test data.')
    api_infoset.add_argument(
        '--get', action='store_true', help='Get test data.')

    # Parse MDL parameters
    api_mdl = subparsers.add_parser(
        'mdl', help='Interactions with Infoset')
    api_mdl.add_argument('--post', action='store_true', help='Post test data.')
    api_mdl.add_argument('--get', action='store_true', help='Get test data.')

    # Return
    args = parser.parse_args()
    if args.action is None:
        parser.print_help()
        sys.exit(1)
    return args


def main():
    """Process agent data.

    Args:
        None

    Returns:
        None

    """
    # Get CLI arguments
    args = cli()

    # Instantiate class to communicate with the various APIs
    api_test = _APItest()

    # Process each option
    if args.action == 'infoset':
        if args.post is True:
            api_test.infoset_post()
            sys.exit(0)
        if args.get is True:
            api_test.infoset_get()
            sys.exit(0)
    else:
        if args.post is True:
            api_test.mdl_post()
            sys.exit(0)
        if args.get is True:
            api_test.mdl_get()
            sys.exit(0)


if __name__ == "__main__":
    main()
