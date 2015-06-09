Django simple SQL log
=====================

.. image:: https://travis-ci.org/novafloss/django-sql-log.svg?branch=master


Goal: provide a middleware that inserts start/stop annotations that
would land on the SQL logs.

Like this:

::

    2014-12-08 09:33:58 CET LOG:  duration: 0.174 ms  statement: BEGIN
    2014-12-08 09:33:58 CET LOG:  duration: 0.502 ms  statement: SET TIME ZONE 'UTC'
    2014-12-08 09:33:58 CET LOG:  duration: 0.053 ms  statement: COMMIT
    2014-12-08 09:33:58 CET LOG:  duration: 0.228 ms  statement: SHOW default_transaction_isolation
    2014-12-08 09:33:58 CET LOG:  duration: 0.043 ms  statement: BEGIN
    2014-12-08 09:33:58 CET LOG:  duration: 0.354 ms  statement: SELECT 'django_sql_log_demo.views.Index_START'
    2014-12-08 09:33:58 CET LOG:  duration: 1.221 ms  statement: SELECT "dummy_article"."id", "dummy_article"."title", "dummy_article"."body" FROM "dummy_article"
    2014-12-08 09:33:58 CET LOG:  duration: 0.118 ms  statement: SELECT 'django_sql_log_demo.views.Index_STOP'
    2014-12-08 09:33:58 CET LOG:  duration: 0.067 ms  statement: ROLLBACK
    2014-12-08 09:33:59 CET LOG:  duration: 0.179 ms  statement: BEGIN
    2014-12-08 09:33:59 CET LOG:  duration: 0.513 ms  statement: SET TIME ZONE 'UTC'
    2014-12-08 09:33:59 CET LOG:  duration: 0.054 ms  statement: COMMIT
    2014-12-08 09:33:59 CET LOG:  duration: 0.231 ms  statement: SHOW default_transaction_isolation
    2014-12-08 09:34:00 CET LOG:  duration: 117.999 ms  statement: DROP DATABASE "test_hello_world"

The available middleware has been tested only with Postgresql databases,
but it should work with other SQL-based RDBMs.

Usage
-----

Add this package to your requirements, and install it the usual way. You
don't have to add the application to the ``INSTALLED_APPS``, there's no
model to sync.

Add the middleware like this:

.. code:: python

    MIDDLEWARE_CLASSES = (
        'django_sql_log.middleware.SQLLoggingMiddleware',
        # ...
    )

Although the order of the middlewares is not crucial, it is better to
make sure that the middleware is near the first place in the list.

Log format string
~~~~~~~~~~~~~~~~~

By default, the log format string is:

::

    {full_name}_{phase}

In the demo site, this would result in:

::

    django_sql_log_demo.views.Index_START

for the START event in the log.

You can customize this format by adding the ``DJANGO_SQL_LOG_FORMAT`` to
your settings. Available format variables are (with correspondance in
the demo tests):

-  ``module_name``: ``django_sql_log_demo.views``,
-  ``func_name``: ``Index``,
-  ``full_name``: ``django_sql_log_demo.views.Index``,
-  ``phase``: START or STOP,

Hacking
-------

If you want to run the test-suite, you **must** have a
``settings_pg.py`` file in your ``demo/django_sql_log_demo`` directory.

You can find an example file that you may copy, and amend with correct
credentials to your Postgresql server. Please bear in mind that the
database you'll have to connect to must exist on this server, and that
your PG user should be able to create / delete databases.

With ``tox`` installed, simply run the command ``tox``. This should run
the tests for Sqlite and postgresql environments, if ready.

Logging in Postgresql
~~~~~~~~~~~~~~~~~~~~~

For you information, logs are not activated by default in postgresql settings.
To make sure your log file will display the START/STOP events, go edit
your ``postgresql.conf`` file and set this variable::

    log_min_duration_statement = 0

For other database systems, please refer to the official documentation.


This software is published under the terms of the MIT License. Please
see the ``LICENSE`` file for more information.
