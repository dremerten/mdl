Operation
=========

The core of ``mdl`` is its API which stores and retrieves data from either it's own database of from infoset using  REST API calls. 

Testing Operation After Installation
------------------------------------

There are a number of steps to take to make sure you have installed ``mdl`` correctly. This section explains how to do basic testing before putting ``mdl`` into production.

Start the API Interactively
~~~~~~~~~~~~~~~~~~~~~~~~~~~

Start the ``mdl`` API interactively.

::

    $ bin/mdl-api --start


Test API Functionality
~~~~~~~~~~~~~~~~~~~~~~

Now that both the API and ingester are running, it's time to test functionality by running the ``bin/tools/test_installation.py`` script.

You can test by either posting to the ``mdl`` API or directly to the ``infoset-ng`` API depending on your needs. Here are some command examples.

::

    $ bin/tools/test_installation.py mdl --post 
    $ bin/tools/test_installation.py mdl --get 
    $ bin/tools/test_installation.py infoset --post 
    $ bin/tools/test_installation.py infoset --get 

Here is an example of a successful ``post`` test:

::

    $ bin/tools/test_installation.py mdl --post 
    
    http://localhost:3000/mdl/api/v1/mobile/post/drivercoordinates
    
    {'devicename': '+1 876-927-1680',
     'id_agent': 'e33ce6311cf95c6264c6777323e9c717220b19ccad7b6da1877384e7fb3364e7',
     'latitude': 1.7070604,
     'longitude': 1.8220003,
     'name': 'DoRoad',
     'utc_timestamp': 1487763120}
    
    2017-02-21 19:32:30,471 - mdl_console - INFO - [peter] (1055S): Successfully posted test data for +1 876-927-1680
    
    $

Refer to the Troubleshooting section of this page to rectify any issues.

Stop After Successful Testing
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

Now that you have tested the functionality successsfully it is time to stop the interactive API session until you decide the best method to run ``mdl``, either interactively as you did during the testing or as system daemons. 

::

    $ bin/mdl-api --stop


The procedures to operate ``mdl`` using the various types of daemons will be covered next.



API Operation
-------------
The ``API`` can be operated in one of two modes:

#.  **System Daemon**: As a system daemon which will automatically restart after a reboot.
#.  **User Process**: Run by a user from the CLI. The ``API`` will not automatically restart after a reboot.

Usage of the ``API`` in each mode will be discussed next.


The API as a System Daemon
~~~~~~~~~~~~~~~~~~~~~~~~~~

This is the preferred mode of operation for production systems. This mode is automatically configured if you installed ``mdl`` using the ``root`` user.

The ``API`` can be started like this:

::

    $ sudo systemctl start mdl-api.service

The ``API`` can be stopped like this:

::

    $ sudo systemctl stop mdl-api.service

You can get the status of the ``API`` like this:

::

    $ sudo systemctl status mdl-api.service

You can get the ``API`` to automatically restart on boot like this:

::

    $ sudo systemctl enable mdl-api.service
    
A sample system startup script can be found in the
``examples/linux/systemd/mdl-api.service`` file. Follow the instructions in the file to make changes to the startup operation of the ``API`` daemon.

**Note:** There will be no visible output when the ``API`` is running. The ``API`` logs its status to the ``etc/api-web.log`` file by default. You will be able to see this interaction dynamically by running the following command:

::

    $ tail -f etc/api-web.log


The API as a User Process
~~~~~~~~~~~~~~~~~~~~~~~~~

You can run the API in standalone mode using the  ``bin/mdl-api`` script. The standalone ``API`` can be started like this:

::

    $ bin/mdl-api --start

The API can be stopped like this:

::

    $ bin/mdl-api --stop

You can get the status of the API like this:

::

    $ bin/mdl-api --status

**Note:** There will be no visible output when the API is running. Web traffic to the API is logged to the ``etc/api-web.log`` file by default. You will be able to see this interaction dynamically by running the following command:

::

    $ tail -f etc/api-web.log

