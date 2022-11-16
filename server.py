import socket
#from ServerGUI import Application

def server_program():
    # get the hostname
    host = socket.gethostname()
    print(socket.gethostbyname(host))
    print(host)
    port = 5000  # initiate port no above 1024

    server_socket = socket.socket()  # get instance
        # look closely. The bind() function takes tuple as argument
    server_socket.bind((host, port))  # bind host address and port together

        # configure how many client the server can listen simultaneously
    server_socket.listen(1)
    conn, address = server_socket.accept()  # accept new connection
    print("Conectado a: " + str(address))
    conn.send(serverName.encode()) 
    clientName = conn.recv(1024).decode()
    while True:
            # receive data stream. it won't accept data packet greater than 1024 bytes
            data = conn.recv(1024).decode()
            if not data:
                # if data is not received break
                break
            print("De " + clientName +": "+ str(data))
            data = input(serverName + ': ')
            if data == 'force-exit': 
                break
            conn.send(data.encode())  # send data to the client

    conn.close()  # close the connection

#Application()
print('Envie force-exit para encerrar')
serverName = input('Nome do servidor: ')
server_program()