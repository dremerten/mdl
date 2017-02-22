Configuration
=============

It is important to have a valid configuration file in the ``etc/``
directory before starting data collection. The installation automatically creates a default version that may need to be edited. This page explains the various configuration parameters.

The ``examples/etc`` directory includes a sample reference file.


mdl Configuration Example
--------------------------------

In this example we explain each parameter in the configuration file.

The ``main`` section governs the general operation of ``mdl``.

::

    main:
        log_directory: /home/mdl/log
        log_level: debug
        interval: 300
        listen_address: 0.0.0.0
        bind_port: 6000
        sqlalchemy_pool_size: 10
        sqlalchemy_max_overflow: 10
        memcached_hostname: localhost
        memcached_port: 11211
        db_hostname: localhost
        db_username: mdl
        db_password: PASSWORD
        db_name: mdl
        infoset_server_name: localhost
        infoset_server_port: 6000
        infoset_server_https: False
        infoset_server_uri: /infoset/api/v1



An explanation of these fields follows:


=================================== ========
Parameter                           Description
=================================== ========
``main:``                           YAML key describing the server configuration.
``log_directory:``                  The directory where ``mdl`` places its log files
``log_level:``                      Defines the logging level. ``debug`` level is the most verbose, followed by ``info``, ``warning`` and ``critical``
``interval:``                       The expected interval in seconds between updates to the database from systems posting to the mdl API. Data retieved from the API will be spaced ``interval`` seconds apart. **Note** it is important that the ``interval`` matches the interval of the ``infoset-ng`` backend server.
``listen_address:``                 IP address the API will be using. The default is ``0.0.0.0`` or all available IP addresses
``bind_port:``                      The TCP port the API will be listening on
``sqlalchemy_pool_size:``           The SQLAlchemy pool size. This is the largest number of connections that ``mdl`` will be keep persistently with the MySQL database
``sqlalchemy_max_overflow:``        The SQLAlchemy maximum overflow size. When the number of connections reaches the size set in ``sqlalchemy_pool_size``, additional connections will be returned up to this limit. This is the floating number of additional database connections to be made available.
``memcached_hostname: localhost``   The hostname of our ``memcached`` cache server
``memcached_port: 11211``           The port which ``memcached`` is running on
``db_hostname:``                    The devicename or IP address of the database server.
``db_username:``                    The database username
``db_password:``                    The database password
``db_name:``                        The name of the database
``infoset_server_name:``            The name of the ``infoset-ng`` server
``infoset_server_port:``            The TCP/IP port of the ``infoset-ng`` server
``infoset_server_https:``           ``True`` if the ``infoset-ng`` server is using HTTPS
``infoset_server_uri:``             The URI of the ``infoset-ng`` server's API
=================================== ========



Logrotate Configuration
-----------------------


The ``examples/linux/logrotate/mdl`` file is a working logrotate
configuration to rotate the log files that ``mdl`` generates. The ``mdl`` log file data can be extensive and adding the logrotate file to your system
is highly recommended.

::

    $ sudo cp examples/linux/logrotate/mdl /etc/logrotate.d

Next Steps
----------

It is time to test the operation of ``mdl``.
