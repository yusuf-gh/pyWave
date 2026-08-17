
def build_response(body: str, status_code: int = 200, status_text: str = "OK") -> bytes:
    response = f"HTTP/1.1 {status_code} {status_text}\r\n\r\n{body}"
    return response.encode()