class RequestLoggingMiddleware(object):
    """
    This class must be added to the settings.MIDDLEWARE_CLASSES list to log
    incoming requests in the database log
    """
    def process_request(self, request):
        pass


class ResponseLoggingMiddleware(object):
    """
    This class must be added to the settings.MIDDLEWARE_CLASSES list to log
    the processed response to the database log
    """
    def process_response(self, request, response):
        return response
