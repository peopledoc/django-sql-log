"""

This logging middleware classes have to be added to the
settings.MIDDLEWARE_CLASSES list in order to log START and STOP in the SQL
logs. Example::

    MIDDLEWARE_CLASSES = (
        'django_sql_log.middleware.SQLLoggingMiddleware',
        # Your other middlewares...
    )


"""
from django.core.urlresolvers import resolve, Resolver404
from django.db import connection
from django.conf import settings


def get_log_string(request, phase):
    DJANGO_SQL_LOG_FORMAT = getattr(
        settings, 'DJANGO_SQL_LOG_FORMAT', '{full_name}_{phase}')
    try:
        func, args, kwargs = resolve(request.path)
    except Resolver404:
        return ""
    func_name = func.__name__
    module_name = func.__module__
    full_name = '.'.join([func.__module__, func.__name__])

    return DJANGO_SQL_LOG_FORMAT.format(**{
        'module_name': module_name,
        'func_name': func_name,
        'full_name': full_name,
        'phase': phase,
    })


class SQLLoggingMiddleware(object):

    def sql_log(self, request, phase):
        cursor = connection.cursor()
        msg = get_log_string(request, phase)
        if msg:
            cursor.execute("SELECT %s", [msg])

    def process_request(self, request):
        self.sql_log(request, "START")

    def process_response(self, request, response):
        self.sql_log(request, "STOP")
        return response
