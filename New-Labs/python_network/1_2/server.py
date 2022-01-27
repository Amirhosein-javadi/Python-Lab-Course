import socket
import time

host = 'localhost'
port = 52878

socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.listen()
connection, address = socket_server.accept()
data_file = open('data_server.txt', 'r')
for line in data_file:
    connection.send(line.encode('UTF-8'))
    time.sleep(0.2)
data_file.close()
time.sleep(0.2)
socket_server.close()