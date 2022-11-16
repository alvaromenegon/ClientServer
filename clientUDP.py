import socket

serverAddressPort   = (socket.gethostbyname(socket.gethostname()), 20000)
bufferSize          = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

while True:
    print("Mensagem: ")
    msgFromClient       = input()
    if msgFromClient == 'tchau': break
    bytesToSend         = str.encode(msgFromClient)
    UDPClientSocket.sendto(bytesToSend, serverAddressPort)
    try:
        msgFromServer = UDPClientSocket.recvfrom(bufferSize)
        msg = "Message from Server {}".format(msgFromServer[0])
    except:
        msg = "Nenhum dado recebido"
    print(msg)
    



