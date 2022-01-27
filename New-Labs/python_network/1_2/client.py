import socket

host = 'localhost'
port = 52878

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((host, port))
data_file = open('data_client.txt', 'w')
while True:
    transfered_data = socket_client.recv(1024).decode()
    if transfered_data:
        data_file.write(transfered_data)
        data_file.flush()
    else:
        break
data_file.close()
socket_client.close()