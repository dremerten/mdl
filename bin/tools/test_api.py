#! /usr/bin/env python3
"""mdl api tester."""

# Standard imports
import sys

# mdl imports
try:
    from mdl.utils import configuration
except:
    print('You need to set your PYTHONPATH to include the mdl library')
    sys.exit(2)
from mdl.api import API


def main():
    """Get Flask server running.

    Args:
        None

    Returns:
        None

    """
    # Start
    config = configuration.Config()
    bind_port = config.bind_port()
    listen_address = config.listen_address()
    API.run(debug=True, host=listen_address, threaded=True, port=bind_port)


if __name__ == '__main__':
    main()
