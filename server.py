from socket import *
import re

class WebServer:
    def __init__(self, portNumber=6789):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverPort = portNumber
        self.serverSocket.bind(('', self.serverPort))
        self.serverSocket.listen(1)
        self.rePatternForFiles = re.compile("\w+[.]{1}\w+")
    
    def HttpGet(self, message):
        filename = message.split()[1].decode("utf-8")[1:]
        if(self.rePatternForFiles.match(filename)):
            self.SendHTMLFile(filename)
        else:
            raise IOError
    
    def SendHTMLFile(self, filename):
        print('Sending {0}'.format(filename))
        f = open(filename, 'rb')
        outputdata = f.readlines()
        f.close()
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            self.connectionSocket.send(outputdata[i])
        self.connectionSocket.close()

    def NotFound(self):
        notFound = open("NotFound.html",)
        outputdata = ["<html>", "<body>", "<h1>", "404 Not Found", "</h1>", "</body>", "</html>"]
        notFound.close()
        #Send response message for file not found
        self.connectionSocket.send(str.encode("HTTP/1.1 404 NOT FOUND\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            self.connectionSocket.send(str.encode(outputdata[i]))
        self.connectionSocket.close()

    def run(self):
        print('Ready to serve...')
        self.connectionSocket, addr = self.serverSocket.accept()
        print(f'Running at {addr}')
        try:
            message = self.connectionSocket.recv(1024)
            print(message.split())
            if(message.split()[0].decode("utf-8") == 'GET'):
                self.HttpGet(message)
        except KeyboardInterrupt:
            self.serverSocket.close()
        except IOError:
            self.NotFound()

if __name__ == '__main__':
    server = WebServer()
    while True:
        server.run()
    server.serverSocket.close()
