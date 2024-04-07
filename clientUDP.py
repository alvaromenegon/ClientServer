import socket
#"tchau" encerra

host = input('Digite o IP do servidor, ou pressione enter para usar o localhost: ') or '127.0.0.1'
port = int(input('Digite a porta do servidor, ou pressione enter para usar a porta padrão 5000: ') or 5000)
serverAddressPort   = (host, port)
#input('Digite o IP do servidor, ou pressione enter para usar o localhost: ') or (socket.gethostbyname(socket.gethostname()), 20000)
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
    
    



