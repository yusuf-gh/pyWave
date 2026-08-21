from request import HTTPRequest
from router import handle_static_routing
from logger import log_connection, log_error

def handle_client(client_socket, client_address):
    try:
        req_object = HTTPRequest.read_from_socket(client_socket)

        if not req_object.method:
            return

        log_connection(
            client_address=client_address,
            method=req_object.method,
            path=req_object.path,
            user_agent=req_object.headers.get('user-agent', 'Unknown')
        )

        response = handle_static_routing(req_object)
        client_socket.sendall(response)

    except Exception as e:
        log_error("Client request error", factor=str(e))