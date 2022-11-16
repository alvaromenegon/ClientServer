import socket

#TCP
#tchau encerra

def client_program():
    host = socket.gethostname() 
    port = 5000 
    client_socket = socket.socket() 
    client_socket.connect((host, port)) 
    serverName = client_socket.recv(1024).decode()
    print('Conectado ao Servidor ' + serverName)
    client_socket.send(clientName.encode()) 
    message = input(clientName + ": ")  #Mensagem

    while message.lower().strip() != 'tchau':
        client_socket.send(message.encode())  
        data = client_socket.recv(1024).decode()  
        print('Recebido do servidor '+serverName+': ' + data)  
        message = input(clientName+": ")  
    client_socket.close()

clientName = input('Nome: ')
client_program()
