from django.test import TestCase
from mock import Mock, patch

from django_sql_log.middleware import RequestLoggingMiddleware
from django_sql_log.middleware import ResponseLoggingMiddleware
RequestLoggingMiddleware = Mock(RequestLoggingMiddleware)
ResponseLoggingMiddleware = Mock(ResponseLoggingMiddleware)


class TestSettings(TestCase):
    "Test if the demo settings are correctly done"

    def test_request(self):
        with patch('django_sql_log.middleware.RequestLoggingMiddleware.process_request') as mocked_request:
            self.client.get('/')
            self.assertTrue(mocked_request.called)

    def test_response(self):
        with patch('django_sql_log.middleware.ResponseLoggingMiddleware.process_response') as mocked_response:
            self.client.get('/')
            self.assertTrue(mocked_response.called)
