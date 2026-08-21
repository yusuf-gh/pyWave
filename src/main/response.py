
def build_response(body: str, status_code: int = 200, status_text: str = "OK") -> bytes:

    body_types = body.encode("utf-8")

    content_length = len(body_types)

    headers = (
        f"HTTP/1.1 {status_code} {status_text}\r\n"
        f"Content-Type: text/html; charset=utf-8\r\n"
        f"Content-Length: {content_length}\r\n"
        f"Connection: close\r\n"
        f"\r\n"
    )
    return headers.encode("utf-8") + body_types