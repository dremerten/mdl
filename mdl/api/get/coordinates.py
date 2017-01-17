"""mdl-ng database API. Datapoint table."""

# Standard imports
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
    data = []

    # Get data from cache
    key = ('mdl.api:get/coordinates/lastcontactsdrivers')
    cache_value = CACHE.get(key)

    # Get infoset URI to process
    uri = 'db/multitable/datapointsummary'
    url = '{}/{}'.format(reference.infoset_api_url_prefix(CONFIG), uri)

    # Process cache miss
    if cache_value is None:
        # Get data from infoset
        try:
            result = requests.get(url)
            received_data = result.json()
        except:
            received_data = None

        # Filter data
        if received_data is not None:
            for item in received_data:
                if item['name'] != 'DoRoad':
                    continue
                data.append(item)

        # Add data to cache
        CACHE.set(key, data)
    else:
        data = cache_value

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
    data = []

    # Get data from cache
    key = ('mdl.api:get/coordinates/lastcontactsriders')
    cache_value = CACHE.get(key)

    # Get infoset URI to process
    uri = 'db/multitable/datapointsummary'
    url = '{}/{}'.format(reference.infoset_api_url_prefix(CONFIG), uri)

    # Process cache miss
    if cache_value is None:
        # Get data from infoset
        try:
            result = requests.get(url)
            received_data = result.json()
        except:
            received_data = None

        # Filter data
        if received_data is not None:
            for item in received_data:
                if item['name'] != 'OneStop':
                    continue
                data.append(item)

        # Add data to cache
        CACHE.set(key, data)
    else:
        data = cache_value

    # Return
    return jsonify(data)
