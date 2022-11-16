import socket

localIP = socket.gethostbyname(socket.gethostname())
localPort   = 20000
bufferSize  = 1024

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))

print("Servidor UDP iniciado")

while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    address = bytesAddressPair[1]
    message = message.decode()
    if message == 'tchau':
        break

    clientIP  = "IP do Cliente: {}".format(address)
    print("Mensagem do cliente: " + message)
    print(clientIP)
    print("Mensagem: ")
    msgFromServer       = input()
    bytesToSend         = str.encode(msgFromServer)
    UDPServerSocket.sendto(bytesToSend, address)
    
    