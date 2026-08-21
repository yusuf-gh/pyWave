import socket
from response import build_response
from request import HTTPRequest
from logger import log_connection, log_error


connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
connection.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
host = "0.0.0.0"
port = 8000

connection.bind((host, port))
connection.listen(5)


print(f"Listening on {host}:{port}")

while True:
    try:
        client_socket, client_address = connection.accept()
        # print(f"\n!!! NEW CONNECTION FROM !!!\n {client_address}")


        with client_socket:
            raw_request = client_socket.recv(4096)
            if not raw_request:
                continue

            req_object = HTTPRequest(raw_request)

            log_connection(
                client_address=client_address,
                method=req_object.method,
                path=req_object.path,
                user_agent=req_object.headers.get('user-agent', 'Unknown')
            )

            # print(f"Path: {req_object.path}\r\n"
            #       f"Method: {req_object.method}\r\n"
            #       f"Browser (User Agent): {req_object.headers.get('user-agent', 'Unknown')}\n")

            if req_object.path == '/':
                body = "<h1>Main page</h1><p>Wellcome</p>"
                response = build_response(body)

            elif req_object.path == '/about':
                body = "<h1>About Us</h1><p>We are building our own server</p>"
                response = build_response(body)

            else :
                body = "<h1>404 Page not found</h1>"
                response = build_response(body, status_code=404, status_text="Not found")

            client_socket.sendall(response)

    except KeyboardInterrupt as e:
        log_error("Server shutting down")
        # print(f"\n!!! Server shutting down !!!\n Factor: KeyboardInterrupt\n")
        break
    except Exception as e:
        log_error("Client request error", factor=str(e))
        # print(f"\n!!! Client request error !!!\n Factor: {e}\n")
        continue





