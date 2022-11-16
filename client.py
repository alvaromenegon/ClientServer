import socket

#TCP

def client_program():
    host = socket.gethostname()  # as both code is running on same pc
    port = 5000 
    client_socket = socket.socket()  # instantiate
    client_socket.connect((host, port))  # connect to the server
    serverName = client_socket.recv(1024).decode()
    print('Conectado ao Servidor ' + serverName)
    client_socket.send(clientName.encode()) 

    message = input(clientName + ": ")  # take input

    while message.lower().strip() != 'tchau':
        client_socket.send(message.encode())  # send message
        data = client_socket.recv(1024).decode()  # receive response
        print('Recebido do servidor '+serverName+': ' + data)  # show in terminal
        message = input(clientName+": ")  # again take input
    client_socket.close()  # close the connection


clientName = input('Nome: ')
client_program()
