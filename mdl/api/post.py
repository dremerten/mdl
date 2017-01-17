"""mdl database API. Posting Routes."""

# Flask imports
from flask import Blueprint, request, abort

# mdl imports
from mdl.reference import reference

# Define the POST global variable
POST = Blueprint('POST', __name__)


@POST.route('/post/drivercoordinates', methods=['POST'])
def receive_driver():
    """Function for handling /mdl/api/v1.0/mobile/post/drivercoordinates route.

    Args:
        None

    Returns:
        Text response if Received

    """
    # Initialize key variables
    found_count = 0

    # Get JSON from incoming agent POST
    data = request.json

    # Make sure all the important keys are available
    keys = [
        'utc_timestamp', 'id_agent', 'devicename',
        'latitude', 'longitude', 'name']
    for key in keys:
        if key in data:
            found_count += 1

    # Do processing
    if found_count == 6:
        # Extract key values from posting
        try:
            int(data['utc_timestamp'])
            float(data['latitude'])
            float(data['longitude'])
        except:
            abort(404)
        agent_name = data['name']

        # Fail if wrong agent
        if agent_name != 'DoRoad':
            abort(404)

        # Post data
        success = _post_coordinate_data(data)

        # Provide feedback
        if success is True:
            # Return
            return 'OK'
        else:
            abort(404)
    else:
        abort(404)


@POST.route('/post/ridercoordinates', methods=['POST'])
def receive_rider():
    """Function for handling /mdl/api/v1.0/mobile/post/ridercoordinates route.

    Args:
        None

    Returns:
        Text response if Received

    """
    # Initialize key variables
    found_count = 0

    # Get JSON from incoming agent POST
    data = request.json

    # Make sure all the important keys are available
    keys = [
        'utc_timestamp', 'id_agent', 'devicename',
        'latitude', 'longitude', 'name']
    for key in keys:
        if key in data:
            found_count += 1

    # Do processing
    if found_count == 6:
        # Extract key values from posting
        try:
            int(data['utc_timestamp'])
            float(data['latitude'])
            float(data['longitude'])
        except:
            abort(404)
        agent_name = data['name']

        # Fail if wrong agent
        if agent_name != 'OneStop':
            abort(404)

        # Post data
        success = _post_coordinate_data(data)

        # Provide feedback
        if success is True:
            # Return
            return 'OK'
        else:
            abort(404)
    else:
        abort(404)


def _post_coordinate_data(data):
    """Post coordinate data to infoset.

    Args:
        data: Data dictionary to post

    Returns:
        Text response if Received

    """
    # Instantiate object to post data
    agent_name = data['name']
    timestamp = data['utc_timestamp']
    latitude = data['latitude']
    longitude = data['longitude']
    id_agent = data['id_agent']
    devicename = data['devicename']

    # Setup the object to post data
    config = reference.ReferenceSampleConfig(agent_name=agent_name)
    report = reference.ReferenceSampleAgent(
        config, devicename, id_agent, timestamp=timestamp)

    # Populate data and post
    report.populate_single(
        'latitude',
        latitude,
        base_type=1, source='GPS')
    report.populate_single(
        'longitude',
        longitude,
        base_type=1, source='GPS')

    # Post data
    success = report.post()
    return success
