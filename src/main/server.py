import socket
import threading
from response import build_response
from request import HTTPRequest
from logger import log_connection, log_error
import os

from src.main.handler import handle_client


def main ():
    host = "0.0.0.0"
    port = 8000

    connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    connection.bind((host, port))
    connection.listen(100)

    print(f"Listening on http://localhost:{port}")

    while True:
        try:
            client_socket, client_address = connection.accept()

            client_thread = threading.Thread(
                target=handle_client,
                args=(client_socket, client_address)
            )
            client_thread.daemon = True
            client_thread.start()

        except KeyboardInterrupt:
            log_error("Server shutting down")
        except Exception as e:
            log_error("Server loop error", factor=str(e))
            continue

    connection.close()

if __name__ == "__main__":
    main()



# connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# host = "0.0.0.0"
# port = 8000
#
# connection.bind((host, port))
# connection.listen(5)
#
#
#
# print(f"Listening on http://localhost:{port}")
#
# while True:
#     try:
#         client_socket, client_address = connection.accept()
#
#
#         with client_socket:
#
#             req_object = HTTPRequest.read_from_socket(client_socket)
#
#             if not req_object.method:
#                 continue
#
#             log_connection(
#                 client_address=client_address,
#                 method=req_object.method,
#                 path=req_object.path,
#                 user_agent=req_object.headers.get('user-agent', 'Unknown')
#             )
#
#             requested_path = req_object.path
#
#             if req_object.path == '/intro':
#                 requested_path = '/index.html'
#
#             BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
#             file_path = os.path.join(BASE_DIR, 'public', requested_path.lstrip('/'))
#
#             if os.path.exists(file_path) and os.path.isfile(file_path):
#
#                 with open(file_path, 'rb') as f:
#
#                     file_content = f.read()
#
#                 _, ext = os.path.splitext(file_path)
#
#                 content_type = MIME_TYPES.get(ext.lower(), 'application/octet-stream')
#                 response = build_response(file_content, content_type=content_type)
#
#             else:
#                 error_body = "<h1>404 Not Found</h1><p>File does not exists on server</p>".encode('utf-8')
#                 response = build_response(error_body, status_code=404, status_text="Not Found")
#
#             client_socket.sendall(response)
#
#     except KeyboardInterrupt as e:
#         log_error("Server shutting down")
#         break
#     except Exception as e:
#         log_error("Client request error", factor=str(e))
#         continue





