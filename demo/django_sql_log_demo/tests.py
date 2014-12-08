from django.test import TestCase
from mock import Mock, patch, MagicMock

from django_sql_log.middleware import RequestLoggingMiddleware
from django_sql_log.middleware import ResponseLoggingMiddleware
RequestLoggingMiddleware = Mock(RequestLoggingMiddleware)
ResponseLoggingMiddleware = Mock(ResponseLoggingMiddleware)

REQUEST_MODULE = 'django_sql_log.middleware.RequestLoggingMiddleware' \
                 '.process_request'

RESPONSE_MODULE = 'django_sql_log.middleware.ResponseLoggingMiddleware' \
                  '.process_response'


class LoggingTestCase(TestCase):
    "Test if the demo settings are correctly done"

    def test_request(self):
        with patch(REQUEST_MODULE) as mocked_request:
            self.client.get('/')
            self.assertTrue(mocked_request.called)

    def test_response(self):
        with patch(RESPONSE_MODULE) as mocked_response:
            self.client.get('/')
            self.assertTrue(mocked_response.called)

    def test_order(self):
        manager = MagicMock()
        with patch(REQUEST_MODULE) as Request:
            with patch(RESPONSE_MODULE) as Response:
                manager.attach_mock(Request, 'Request')
                manager.attach_mock(Response, 'Response')
                self.client.get('/')
                # Ugly method, but couldn't find a better one
                first = manager.mock_calls[0].__str__()
                last = manager.mock_calls[-1].__str__()
                self.assertTrue(first.startswith('call.Request'))
                self.assertTrue(last.startswith('call.Response'))

    def test_zzz_all(self):
        # This test is only here to track the true system log, where the
        # queries should appear. It's more a "smoke test" than a unittest.
        # Its name is test_zzz_all just to make sure it's the last test of the
        # TestSuite.
        response = self.client.get('/')
        self.assertEquals(response.status_code, 200)
