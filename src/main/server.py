import socket
from response import build_response

connection = socket.socket()
host = "0.0.0.0"
port = 8000

connection.bind((host, port))
connection.listen(5)


print(f"Listening on {host}:{port}")

while True:
    try:
        client_socket, client_address = connection.accept()
        print(f"\n!!! NEW CONNECTION FROM !!!\n {client_address}\n\n")


        with client_socket:
            request = client_socket.recv(1024)
            print(request)

            response = build_response("Hello World!")
            client_socket.send(response)

    except KeyboardInterrupt as e:
        print(f"\n!!! Server shutting down !!!\n Factor: KeyboardInterrupt\n")
        break
    except Exception as e:
        print(f"\n!!! Client request error !!!\n Factor: {e}\n")
        continue





