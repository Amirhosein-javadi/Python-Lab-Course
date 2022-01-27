import socket
import time

host = 'localhost'
port = 52878

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.listen()
connection, address = socket_server.accept()
connection.send("Welcome".encode('UTF-8'))
time.sleep(0.2)
socket_server.close()