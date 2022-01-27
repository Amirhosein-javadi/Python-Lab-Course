import _thread
import socket
import time
import os.path

host = 'localhost'
port = 52878

def back_function(connection, address):
    connection.send('Hello :)'.encode('UTF-8'))
    while True:
        data = connection.recv(1024).decode()
        if data == 'finish':
            break
        if not os.path.exists(data):
            connection.send('I dont have this file!'.encode('UTF-8'))
        elif not data:
            break
        else:
            connection.send('I am sending your file...'.encode('UTF-8'))
            time.sleep(0.2)
            data_file = open(data, 'r')
            for line in data_file:
                connection.send(line.encode('UTF-8'))
                time.sleep(0.2)
            data_file.close()
            connection.send('It is done :)'.encode('UTF-8'))
    connection.close()

        
socket_server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_server.bind((host, port))
socket_server.listen()
while True:
    connection, address = socket_server.accept()
    _thread.start_new_thread(back_function, (connection, address))
            
