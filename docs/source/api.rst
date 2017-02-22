Using the API
=============

This section outlines how to use the API

Why Infoset-ng Expects UTC Timestamps
-------------------------------------

There is a good reason for this. According to the python datetime documentation page, `The rules for time adjustment across the world are more political than rational, change frequently, and there is no standard suitable for every application aside from UTC.`

We cannot guarantee the python timezone libraries will be always up to date, so we default to UTC as recommended.

Posting Data to the API
-----------------------

Posting data to the API is. Add the prefix ``http://SERVER_IP:3000`` to
all the examples below to update data in your instance of ``mdl``

Route /mdl/api/v1/mobile/post/drivercoordinates
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

JSON data needs to be posted to the ``http://SERVER_IP:3000/mdl/api/v1/mobile/post/drivercoordinates`` URL in the format below:

The example below explains the expected JSON format:

::

    {'devicename': '+1 876-927-1660',
     'id_agent': 'bec9ba91e14804001e037fa4f52c94fb1ef027d04e1b86f6a74ab36e3b073609',
     'latitude': 1.7518061,
     'longitude': 1.7115351,
     'name': 'DoRoad',
     'utc_timestamp': 1487763540}


Where feasible, we will use Linux and networking related examples to
make explanation easier.

===================================     ========
Field                                   Descripton
===================================     ========
``name``                                Agent or application name. If your agent script is designed to collect server performance data, you could name it 'server_performance'. Each server performance agent would therefore report the same agent value.
``id_agent``                            A unique, unchanging systemwide identifier for the **application** sending the data.

``latitude``                            Latitude value of the geocoordinates.
``longitude``                           Longitude value of the geocoordinates.
``devicename``                          A unique, unchanging systemwide identifier 
``utc_timestamp``                       Epoch **UTC** time when data was generated. This must be an integer.
===================================     ========


Retrieving Data from the API
----------------------------
This section covers how to retrieve data from the API. First we cover some of the basics.

Overview
~~~~~~~~
Retrieving data from mdl is easy. Add the prefix ``http://SERVER_IP:6000`` to all the examples below to get data from your instance of ``mdl``

You can test each route using the command:

::

    $ curl http://SERVER_IP:6000/route


Routes
~~~~~~

Data is retrieved by making HTTP requests to well known URIs or ``routes``. These are covered next.

Route /mdl/api/v1/mobile/get/coordinates/lastcontactdrivers
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

This route will retreive the most recent geo coordinate data posted by all drivers. It is returned in the form of a list of dicts.

=========================   ======
Field                       Description
=========================   ======
``id_agent``                The Agent ID
``agent_label``             The description of the data being stored
``devicename``              The name of the device
``idx_deviceagent``         The index value that ``infoset-ng`` uses to store the the device`s agent data.
``idx_datapoint``           The index value that ``infoset-ng`` uses to store the the geocordinate data.
``name``                    The agent name
``timestamp``               The **UTC** timestamp of the the contact
``value``                   The value of the geocoordinate
=========================   ======

Example:

::

    $ curl http://SERVER_IP:3000/mdl/api/v1/mobile/get/coordinates/lastcontactdrivers
    
    [{'agent_label': 'latitude',
      'agent_source': 'GPS',
      'devicename': '+1 876-927-1660',
      'id_agent': 'bec9ba91e14804001e037fa4f52c94fb1ef027d04e1b86f6a74ab36e3b073609',
      'idx_datapoint': 2,
      'idx_deviceagent': 2,
      'name': 'DoRoad',
      'timestamp': 1487763900,
      'value': 1.79943},
     {'agent_label': 'longitude',
      'agent_source': 'GPS',
      'devicename': '+1 876-927-1660',
      'id_agent': 'bec9ba91e14804001e037fa4f52c94fb1ef027d04e1b86f6a74ab36e3b073609',
      'idx_datapoint': 3,
      'idx_deviceagent': 2,
      'name': 'DoRoad',
      'timestamp': 1487763900,
      'value': 1.69493},
     {'agent_label': 'latitude',
      'agent_source': 'GPS',
      'devicename': '+1 876-927-1680',
      'id_agent': 'e33ce6311cf95c6264c6777323e9c717220b19ccad7b6da1877384e7fb3364e7',
      'idx_datapoint': 4,
      'idx_deviceagent': 3,
      'name': 'DoRoad',
      'timestamp': 1487763900,
      'value': 1.89642},
     {'agent_label': 'longitude',
      'agent_source': 'GPS',
      'devicename': '+1 876-927-1680',
      'id_agent': 'e33ce6311cf95c6264c6777323e9c717220b19ccad7b6da1877384e7fb3364e7',
      'idx_datapoint': 5,
      'idx_deviceagent': 3,
      'name': 'DoRoad',
      'timestamp': 1487763900,
      'value': 1.57342}]
    
