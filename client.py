import socket

#TCP
#tchau encerra

def client_program():
    host = input('Digite o IP do servidor, ou pressione enter para usar o localhost: ') or '127.0.0.1'
    port = int(input('Digite a porta do servidor, ou pressione enter para usar a porta padrão 5000: ') or 5000)
    #host = socket.gethostname() 
    #port = 5000 
    print('Conectando ao servidor em ' + host + ' na porta ' + str(port))
    client_socket = socket.socket() 
    client_socket.connect((host, port)) 
    print('Conectado ao servidor ' + host + ' na porta ' + str(port))
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
