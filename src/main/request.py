import socket


class HTTPRequest:
    def __init__(self, raw_request_bytes: bytes):
        self.method = ""
        self.path = ""
        self.headers = {}
        self.body = ""

        if not raw_request_bytes:
            return

        if b"\r\n\r\n" in raw_request_bytes:
            header_part, self.body_bytes = raw_request_bytes.split(b"\r\n\r\n", 1)
        else:
            header_part = raw_request_bytes

        request_text = header_part.decode("utf-8", errors="ignore")
        lines = request_text.split("\r\n")

        start_line = lines[0]
        start_line_parts = start_line.split(" ")

        if len(start_line_parts) >= 2:
            self.method = start_line_parts[0]
            self.path = start_line_parts[1]

        for line in lines[1:]:
            if ":" in line:
                key, value = line.split(":", 1)
                self.headers[key.strip().lower()] = value.strip()

    # фигня короче для того что бы байтам письку не отрезало, и с помощью цикла
    # парсятся методы put и patch, post содержащие большие файлы
    @classmethod
    def read_from_socket(cls, client_socket: socket.socket):
        chunks = []
        raw_request = b""

        while True:
            chunk = client_socket.recv(4096)
            if not chunk:
                break

            chunks.append(chunk)
            raw_request = b"".join(chunks)

            if b"\r\b\r\b" in raw_request:
                break

        if not raw_request:
            return cls(b"")

        header_part, body_part = raw_request.split(b'\r\n\r\n', 1)

        header_text = header_part.decode("utf-8", errors='ignore')
        content_length = 0
        for line in header_text.split("\r\n"):
            if ":" in line:
                key, val = line.split(":", 1)
                if key.strip().lower() == "content-length":
                    content_length = int(val.strip())
                    break
        bytes_already_read = len(body_part)
        bytes_left_to_read = content_length - bytes_already_read

        while bytes_left_to_read > 0:
            chunk = client_socket.recv(min(4096, bytes_left_to_read))
            if not chunk:
                break
            chunks.append(chunk)
            bytes_left_to_read -= len(chunk)

        full_raw_data = b"".join(chunks)
        return cls(full_raw_data)




