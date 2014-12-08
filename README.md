# Django simple SQL log

Goal: provide a middleware that inserts start/stop annotations that would
land on the SQL logs.

The middlewares available have been tested only with Postgresql databases, but
it should work with other SQL-based RDBMs.

## Usage

Add this package to your requirements, and install it the usual way. You don't
have to add the application to the ``INSTALLED_APPS``, there's no model to sync.

Add the middlewares like this:

```python
MIDDLEWARE_CLASSES = (
    'django_sql_log.middleware.RequestLoggingMiddleware',
    # ...
    'django_sql_log.middleware.ResponseLoggingMiddleware',
)
```

Although the order of the middlewares is not crucial, it is better to make sure
that the RequestLoggingMiddleware is near the first place in the list, and the
ResponseLoggingMiddleware near the end.

## Hacking

If you want to run the test-suite, you **must** have a ``settings_pg.py`` file
in your ``demo/django_sql_log_demo`` directory.

You can find an example file that you may copy, and amend with correct
credentials to your Postgresql server. Please bear in mind that the database
you'll have to connect to must exist on this server, and that your PG user
should be able to create / delete databases.

With `tox` installed, simply run the command `tox`. This should run the tests
for Sqlite and postgresql environments, if ready.
