import socket

host = 'localhost'
port = 52878

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((host, port))
transfered_data = socket_client.recv(1024).decode()
if transfered_data :
    print(transfered_data)
socket_client.close()