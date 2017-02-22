Introduction
============

MDL is a middleware subsystem for mobile taxi applications.

There's a lot to know about ``mdl`` which we'll summarize here.

Features
--------

``mdl`` has the following features:

1.  Written in python, a modern language.
2.  Easy configuration.
3.  Uses the well known Flask webserver for accepting data and
    responding to requests.
4.  ``mdl`` has a number of fault tolerant features aimed at
    making it resilient in unstable computing environemnts.
5.  MariaDB / MySQL database backend
6.  Database connection pooling to reduce database load.
7. The ``mdl`` configuration is entirely stored in files. This
    allows it to collect data in the absense of a database, such as
    during maintenance or an outage.
8. Backups are simple. Just save the entire contents of the
    ``mdl`` directory tree including hidden files, and save a
    copy of the database for your performance data.

We are always looking for more contributors!

Oversight
---------

``mdl`` is a student collaboration between:

1. The University of the West Indies Computing Society. (Kingston,
   Jamaica)
2. The University of Techology, IEEE Student Branch. (Kingston, Jamaica)
3. The Palisadoes Foundation http://www.palisadoes.org

And many others.
