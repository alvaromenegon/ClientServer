import socket
#"tchau" encerra

serverAddressPort   = (socket.gethostbyname(socket.gethostname()), 20000)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    print("Mensagem: ")
    msgFromClient       = input()
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    if msgFromClient == 'tchau': break
    try:
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msgFromServer = msgFromServer[0].decode()
        msg = "Mensagem do servidor: {}".format(msgFromServer)
    except:
        msg = "Nenhum dado recebido"
    print(msg)
    
    



