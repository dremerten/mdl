"""mdl-ng database API. Datapoint table."""

# Standard imports
from collections import defaultdict

# PIP3 imports
import requests

# Flask imports
from flask import Blueprint, jsonify

# Infoset-ng imports
from mdl.api import CACHE, CONFIG
from mdl.reference import reference

# Define the AGENT global variable
COORDINATES = Blueprint('COORDINATES', __name__)


@COORDINATES.route('/get/coordinates/lastcontactdrivers')
def get_lastgps_drivers():
    """Get last GPS coordinates for drivers.

    Args:
        None

    Returns:
        results: A list of dicts of results

    """
    # Initialize key variables
    data = _lastcontact('DoRoad')

    # Return
    return jsonify(data)


@COORDINATES.route('/get/coordinates/lastcontactriders')
def get_lastgps_riders():
    """Get last GPS coordinates for riders.

    Args:
        None

    Returns:
        results: A list of dicts of results

    """
    # Initialize key variables
    data = _lastcontact('OneStop')

    # Return
    return jsonify(data)


def _lastcontact(agent_name):
    """Get last GPS coordinates for drivers.

    Args:
        None

    Returns:
        results: A list of dicts of results

    """
    # Initialize key variables
    lookuptable = defaultdict(lambda: defaultdict(dict))
    lastcontacts = None
    data = []

    # Get data from cache
    key = ('mdl.api:get/coordinates/lastcontactsdrivers')
    cache_value = CACHE.get(key)

    # Process cache miss
    if cache_value is None:
        # Get lookup table of datapoints
        lookuptable = _lastcontact_lookup(agent_name)

        # Get infoset last contact information
        uri = 'lastcontacts'
        url = '{}/{}'.format(reference.infoset_api_url_prefix(CONFIG), uri)
        try:
            result = requests.get(url)
            lastcontacts = result.json()
        except:
            lastcontacts = None

        if bool(lastcontacts) is True:
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
                data.append(data_dict)

        # Add data to cache
        CACHE.set(key, data)
    else:
        data = cache_value

    # Return
    return data


def _lastcontact_lookup(agent_name):
    """Get last contact data from all agents of specific name.

    Args:
        agent_name: Name of agent

    Returns:
        lookuptable: Dict of agent and datapoint information keyed by
            idx_datapoint

    """
    # Initialize key variables
    lookuptable = defaultdict(lambda: defaultdict(dict))
    datapointsummary = None

    # Get infoset datapoint information
    uri = 'datapoints/all/summary'
    url = '{}/{}'.format(reference.infoset_api_url_prefix(CONFIG), uri)
    try:
        result = requests.get(url)
        datapointsummary = result.json()
    except:
        datapointsummary = None

    # Create a lookup table for datapoints
    if bool(datapointsummary) is True:
        for item in datapointsummary:
            # Only process the desired agent
            if item['name'] != agent_name:
                continue

            # Append data
            idx_datapoint = item['idx_datapoint']
            for key, value in item.items():
                if key != 'idx_datapoint':
                    lookuptable[idx_datapoint][key] = value

    # Abort if nothing found
    return lookuptable
