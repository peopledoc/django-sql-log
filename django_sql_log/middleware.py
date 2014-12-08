"""

This logging middleware classes have to be added to the
settings.MIDDLEWARE_CLASSES list in order to log START and STOP in the SQL
logs. Example::

    MIDDLEWARE_CLASSES = (
        'django_sql_log.middleware.RequestLoggingMiddleware',
        # Your other middlewares...
        'django_sql_log.middleware.ResponseLoggingMiddleware',
    )


"""
from django.core.urlresolvers import resolve
from django.db import connection
from django.conf import settings


def get_log_string(request, phase):
    DJANGO_SQL_LOG_FORMAT = getattr(
        settings, 'DJANGO_SQL_LOG_FORMAT', '{full_name}_{phase}')
    func, args, kwargs = resolve(request.path)
    func_name = func.__name__
    module_name = func.__module__
    full_name = '.'.join([func.__module__, func.__name__])

    return DJANGO_SQL_LOG_FORMAT.format(**{
        'module_name': module_name,
        'func_name': func_name,
        'full_name': full_name,
        'phase': phase,
    })


class LoggingMiddleware(object):

    @property
    def phase(self):
        raise NotImplementedError('You need to set the phase. START or STOP')

    def sql_log(self, request):
        cursor = connection.cursor()
        msg = get_log_string(request, self.phase)
        cursor.execute("SELECT %s", [msg])


class RequestLoggingMiddleware(LoggingMiddleware):
    """
    This class must be added to the settings.MIDDLEWARE_CLASSES list to log
    incoming requests in the database log
    """
    phase = "START"

    def process_request(self, request):
        self.sql_log(request)


class ResponseLoggingMiddleware(LoggingMiddleware):
    """
    This class must be added to the settings.MIDDLEWARE_CLASSES list to log
    the processed response to the database log
    """
    phase = "STOP"

    def process_response(self, request, response):
        self.sql_log(request)
        return response
