import socket

host = 'localhost'
port = 52878

socket_client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
socket_client.connect((host, port))
transfered_data = socket_client.recv(1024).decode()
if not transfered_data:
    socket_client.close()
    exit()
elif transfered_data == 'Hello :)':
    while True:
        file = input('Type the name of your file:')
        socket_client.send(file.encode('UTF-8'))
        transfered_data = socket_client.recv(1024).decode()
        print(transfered_data)
        if not transfered_data:
            socket_client.close()
            exit()
        elif transfered_data == 'I am sending your file...':
            while True:
                transfered_data = socket_client.recv(1024).decode()
                if not transfered_data:
                    socket_client.close()
                    exit()
                elif transfered_data == 'It is done :)':
                    print(transfered_data)
                    break
                else:
                    print(transfered_data)
        else:
            print(transfered_data)
