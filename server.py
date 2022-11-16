import socket
def server_program():
    host = socket.gethostname()
    print(socket.gethostbyname(host))
    port = 5000 

    server_socket = socket.socket()  
    server_socket.bind((host, port))  
    server_socket.listen(1)
    conn, address = server_socket.accept()  
    print("Conectado a: " + str(address))
    conn.send(host.encode()) 
    clientName = conn.recv(1024).decode()
    while True:
            data = conn.recv(1024).decode()
            if not data:
                break
            print("De " + clientName +": "+ str(data))
            data = input(host + ': ')
            if data == 'force-exit': 
                break
            conn.send(data.encode())  
    conn.close() 

print('Envie force-exit para encerrar')
server_program()