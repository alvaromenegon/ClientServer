import socket

localIP = socket.gethostbyname(socket.gethostname())
#localIP     = "127.0.0.1"
localPort   = 20000
bufferSize  = 1024

msgFromServer       = input() #"Hello UDP Client"
bytesToSend         = str.encode(msgFromServer)

UDPServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

UDPServerSocket.bind((localIP, localPort))

print("Servidor UDP")

while(True):

    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)

    message = bytesAddressPair[0]

    address = bytesAddressPair[1]

    clientMsg = "Message from Client: {}".format(message)
    clientIP  = "Client IP Address: {}".format(address)
    
    print(clientMsg)
    print(clientIP)

    UDPServerSocket.sendto(bytesToSend, address)
    if clientMsg == "b'close'":
        break