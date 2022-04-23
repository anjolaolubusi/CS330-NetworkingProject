from socket import *
serverSocket = socket(AF_INET, SOCK_STREAM)
#Prepare a sever socket
serverPort = 6789
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
while True:
    #Establish the connection
    print('Ready to serve...')
    connectionSocket, addr = serverSocket.accept()
    print(f'Running at {addr}')
    try:
        message = connectionSocket.recv(1024)
        print(message)
        print(type(message))
        filename = message.split()[1].decode("utf-8")[1:]
        f = open(filename, 'rb')
        outputdata = f.readlines()
        f.close()
        connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i])
        connectionSocket.close()
    except IOError:
        f = open("NotFound.html",)
        outputdata = ["<html>", "<body>", "<h1>", "404 Not Found", "</h1>", "</body>", "</html>"]
        f.close()
        #Send response message for file not found
        connectionSocket.send(str.encode("HTTP/1.1 404 NOT FOUND\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            connectionSocket.send(str.encode(outputdata[i]))
        connectionSocket.close()
    except KeyboardInterrupt:
        serverSocket.close()


serverSocket.close()