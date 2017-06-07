"""mdl database API. Posting Routes."""

# Flask imports
from flask import Blueprint, request, abort

# mdl imports
from mdl.reference import reference
from mdl.db.db_orm import Drivers, Riders
from mdl.db.db import Database

from mdl.utils import general

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


@POST.route('/post/register/driver', methods=['POST', 'GET'])
def register_driver():
    """Function for handling /mdl/api/v1/mobile/post/register/driver route.

    Args:
        None

    Returns:
        Text response if Received
    """
    # Initialize key variables
    found_count = 0

    # Get JSON from incoming agent POST
    data = request.json
    keys = [
        'firstName', 'lastName', 'password', 'email',
        'phone', 'utc_timestamp']
    for key in keys:
        if key in data:
            found_count += 1
        # Do processing
    if found_count == 6:
        agent_name = data['name']

        # Fail if wrong agent
        if agent_name != 'OneStop':
            abort(404)

        # Post data
        success = _register_driver_data(data)

        # Provide feedback
        if success is True:
            # Return
            return 'OK'
        else:
            abort(404)
    else:
        abort(404)


@POST.route('/post/login/driver', methods=['POST', 'GET'])
def login_driver():
    """Function for handling /mdl/api/v1/mobile/post/login/driver route.

    Args:
        None

    Returns:
        Text response if Received
    """
    # Initialize key variables
    found_count = 0

    # Get JSON from incoming agent POST
    data = request.json
    keys = ['email', 'password']
    for key in keys:
        if key in data:
            found_count += 1
        # Do processing
    if found_count == 2:
        agent_name = data['name']

        # Fail if wrong agent
        if agent_name != 'OneStop':
            abort(404)

        # Post data
        success = _login_driver_data(data)

        # Provide feedback
        if success is True:
            # Return
            return 'OK'
        else:
            abort(404)
    else:
        abort(404)


@POST.route('/post/register/rider', methods=['POST', 'GET'])
def register_rider():
    """Function for handling /mdl/api/v1/mobile/post/register/rider route.

    Args:
        None

    Returns:
        Text response if Received
    """

    # Initialize key variables
    found_count = 0

    # Get JSON from incoming agent POST
    data = request.json
    keys = [
        'firstName', 'lastName', 'password', 'email',
        'phone', 'utc_timestamp']
    for key in keys:
        if key in data:
            found_count += 1
        # Do processing
    if found_count == 6:
        agent_name = data['name']

        # Fail if wrong agent
        if agent_name != 'OneStop':
            abort(404)

        # Post data
        success = _register_rider_data(data)

        # Provide feedback
        if success is True:
            # Return
            return 'OK'
        else:
            abort(404)
    else:
        abort(404)


@POST.route('/post/login/rider', methods=['POST', 'GET'])
def login_rider():
    """Function for handling /mdl/api/v1/mobile/post/login/rider route.

    Args:
        None

    Returns:
        Text response if Received
    """
    # Initialize key variables
    found_count = 0

    # Get JSON from incoming agent POST
    data = request.json
    keys = ['email', 'password']
    for key in keys:
        if key in data:
            found_count += 1
        # Do processing
    if found_count == 2:
        agent_name = data['name']

        # Fail if wrong agent
        if agent_name != 'OneStop':
            abort(404)

        # Post data
        success = _login_rider_data(data)

        # Provide feedback
        if success is True:
            # Return
            return 'OK'
        else:
            abort(404)
    else:
        abort(404)


def _post_coordinate_data(data):
    """ Post coordinate data to infoset.

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


def _register_driver_data(data):
    """ Post driver data to mdl database.

    Args:
        data: Data dictionary to post

    Returns:
        Text response if Received
    """

    firstName = general.encode(data['firstName'])
    lastName = general.encode(data['lastName'])
    password = general.encode(data['password'])
    email = general.encode(data['email'])
    phone = general.encode(data['phone'])

    database = Database()
    session = database.session()

    # create Driver object
    record = Drivers(
        first_name=firstName,
        last_name=lastName,
        password=password,
        email=email,
        enabled=0
    )
    # check if email exists
    result = session.query(Drivers).filter(
        Drivers.email == email)

    if result.count() == 1:
        # User exists
        return False
    elif result.count() == 0:
        # User doesnt exist
        database.add(record, 1008)
        database.close()
        return True


def _login_driver_data(data):
    """ Check driver data against database.

    Args:
        data: Data dictionary to post

    Returns:
        Text response if Received
    """

    password = general.encode(data['password'])
    email = general.encode(data['email'])

    database = Database()
    session = database.session()

    # check if email exists
    result = session.query(Drivers).filter(
        Drivers.email == email)

    if result.count() == 1:
        # User exists
        return True
    elif result.count() == 0:
        # User doesnt exist
        return False


def _register_rider_data(data):
    """ Post rider data to mdl database.

    Args:
        data: Data dictionary to post

    Returns:
        Text response if Received
    """

    firstName = general.encode(data['firstName'])
    lastName = general.encode(data['lastName'])
    password = general.encode(data['password'])
    email = general.encode(data['email'])
    phone = general.encode(data['phone'])

    database = Database()
    session = database.session()

    # create Riders object
    record = Riders(
        first_name=firstName,
        last_name=lastName,
        password=password,
        email=email,
        enabled=0
    )
    # check if email exists
    result = session.query(Riders).filter(
        Riders.email == email)

    if result.count() == 1:
        # User exists
        return False
    elif result.count() == 0:
        # User doesnt exist
        database.add(record, 1008)
        database.close()
        return True


def _login_rider_data(data):
    """ Check rider data against database.

    Args:
        data: Data dictionary to post

    Returns:
        Text response if Received
    """

    password = general.encode(data['password'])
    email = general.encode(data['email'])

    database = Database()
    session = database.session()

    # check if email exists
    result = session.query(Riders).filter(
        Riders.email == email)

    if result.count() == 1:
        # User exists
        return True
    elif result.count() == 0:
        # User doesnt exist
        return False
