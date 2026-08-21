import os
from response import build_response

MIME_TYPES = {
    '.html': 'text/html; charset=utf-8',
    '.css': 'text/css',
    '.js': 'application/javascript',
    '.png': 'image/png',
    '.jpg': 'image/jpeg',
    '.gif': 'image/gif',
}

def handle_static_routing(req_object) -> bytes:
    requested_path = req_object.path

    if requested_path == "/intro":
        requested_path = "/index.html"

    BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
    file_path = os.path.join(BASE_DIR, 'public', requested_path.lstrip('/'))

    if os.path.exists(file_path) and os.path.isfile(file_path):
        with open(file_path, 'rb') as f:
            file_content = f.read()

        _, ext = os.path.splitext(file_path)
        content_type = MIME_TYPES.get(ext.lower(), 'application/octet-stream')
        return build_response(file_content, content_type=content_type)

    error_body = "<h1>404 Not Found</h1><p>File does not exist on server</p>".encode('utf-8')
    return build_response(error_body, status_code=404, status_text="Not Found", content_type="text/html; charset=utf-8")


