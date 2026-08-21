from ..main import HTTPRequest, build_response
import unittest

class HttpComponentsTest(unittest.TestCase):

    def test_request_parsing(self):
        raw_bytes = b"GET /about HTTP/1.1\r\nHost: localhost\r\n\r\n"
        request = HTTPRequest(raw_bytes)

        print(request.headers)
        self.assertEqual(request.method, "GET")
        self.assertEqual(request.path, "/about")

    def test_request_empty_bytes(self):
        request = HTTPRequest(b"")

        self.assertEqual(request.method, "")
        self.assertEqual(request.path, "")

    def test_response_builder(self):
        body = "Test"
        response_bytes = build_response(body, status_code=200, status_text="OK")

        response_text = response_bytes.decode('utf-8')

        self.assertTrue(response_text.startswith("HTTP/1.1 200 OK"))
        self.assertIn('Content-Length: 4', response_text)
        self.assertIn('Content-Type: text/html', response_text)
        self.assertTrue(response_text.endswith("Test"))

if __name__ == "__main__":
    unittest.main()