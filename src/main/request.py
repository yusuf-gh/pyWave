
class HTTPRequest:
    def __init__(self, raw_request_bytes: bytes):
        self.method = ""
        self.path = ""
        self.headers = {}
        self.body = ""

        if not raw_request_bytes:
            return

        request_text = raw_request_bytes.decode("utf-8", errors="ignore")

        lines = request_text.split("\r\n")

        start_line = lines[0]
        start_line_parts = start_line.split(" ")

        if len(start_line_parts) >= 2:
            self.method = start_line_parts[0]
            self.path = start_line_parts[1]