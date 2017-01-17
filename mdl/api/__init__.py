"""Initialize the API module."""

# Import PIP3 libraries
from flask import Flask

# Import configuration. This has to be done before all other infoset imports.
from mdl.utils import configuration
CONFIG = configuration.Config()

# Setup memcache. Required for all API imports
from mdl.api import cache
CACHE = cache.Cache(CONFIG)

# Do remaining mdl importations
from mdl.api.post import POST
from mdl.api.version import VERSION
from mdl.api.get.coordinates import COORDINATES

# Define the global URL prefix
API_PREFIX = '/{}/mobile'.format(CONFIG.mdl_server_uri())

API = Flask(__name__)
API.register_blueprint(POST, url_prefix=API_PREFIX)
API.register_blueprint(VERSION, url_prefix=API_PREFIX)
API.register_blueprint(COORDINATES, url_prefix=API_PREFIX)
