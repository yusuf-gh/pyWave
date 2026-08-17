import socket
from multiprocessing.connection import Client

connection = socket.socket()
host = "0.0.0.0"
port = 8000

connection.bind((host, port))
connection.listen(5)

print(f"Listening on {host}:{port}")

client_socket, client_address = connection.accept()
print(f"New connection from {client_address}")
