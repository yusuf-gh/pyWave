from ..main import HTTPRequest, build_response
import unittest

class HttpComponentsTest(unittest.TestCase):

    def test_request_parsing(self):
        raw_bytes = b"GET /about HTTP/1.1\r\nHost: localhost\r\n\r\n"
        request = HTTPRequest(raw_bytes)

        print(request.headers)
        self.assertEqual(request.method, "GET")
        self.assertEqual(request.path, "/about")


