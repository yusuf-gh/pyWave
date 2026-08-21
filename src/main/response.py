
def build_response(body_bytes: bytes, status_code: int = 200, status_text: str = "OK",
                   content_type: str = "text/html") -> bytes:
    content_length = len(body_bytes)

    headers = (
        f"HTTP/1.1 {status_code} {status_text}\r\n"
        f"Content-Type: {content_type}\r\n"
        f"Content-Length: {content_length}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    return headers.encode("utf-8") + body_bytes
