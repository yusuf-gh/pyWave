import socket

connection = socket.socket()
host = "0.0.0.0"
port = 8000

connection.bind((host, port))
connection.listen(5)

connection.settimeout(15)


print(f"Listening on {host}:{port}")

while True:
    try:
        client_socket, client_address = connection.accept()
        print(f"\n!!! NEW CONNECTION FROM !!!\n {client_address}\n\n")
        request = client_socket.recv(1024)
        print(request.decode())
        response = b"HTTP/1.1 200 OK\r\n\r\nHello, world!"
        client_socket.send(response)
    except socket.timeout:
        print(f"\n!!! TIMEOUT !!!\n")
        client_socket.close()
        break




