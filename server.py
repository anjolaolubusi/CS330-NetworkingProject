from socket import *
import re
import json

class WebServer:
    '''
    Class initaliztion
    portNumber - Port Number that the web host will be hosted on
    '''
    def __init__(self, portNumber=80):
        self.serverSocket = socket(AF_INET, SOCK_STREAM)
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
        self.serverPort = portNumber
        self.serverSocket.bind(('', self.serverPort))
        self.serverSocket.listen(1)
        self.rePatternForFiles = re.compile("(\w+[\/])?\w+[.]{1}\w+")
    
    '''
    Function that process the HTTP GET Call
    message - Object that represents the socket message
    '''
    def HttpGet(self, message):
        filename = message.split()[1].decode("utf-8")[1:]
        if(self.rePatternForFiles.match(filename)):
            self.SendHTMLFile(filename)
        elif(filename == ''):
            self.SendHTMLFile('HelloWorld.html')
        else:
            raise IOError
    
    '''
    Function that process the HTTP POST Call
    message - Object that represents the socket message
    '''
    def HttpPost(self, message):
        endpoint = message.split()[1].decode("utf-8")[1:]
        if(endpoint == "echo"):
            self.echo(message)
        else:
            self.connectionSocket.send(str.encode("HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n"))
            self.connectionSocket.send(str.encode("Can not find endpoint"))
            self.connectionSocket.close()        

    '''
    Python Function For Echo Endpoint
    message - Object that represents the socket message
    '''
    def echo(self, message):
        echo_message = self.GetJsonBody(message)
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n"))
        self.connectionSocket.send(str.encode("Hit Post. Endpoint: ") + message.split()[1] + str.encode("\n"))
        self.connectionSocket.send(str.encode("Body of POST call: " + json.dumps(echo_message)))
        self.connectionSocket.close()       

    '''
    Process HTTP POST call to return python object of Request Object
    message - Object that represents the socket message
    '''
    def GetJsonBody(self, message):
        json_str = ""
        json_index = 0
        for i in range(len(message.split())):
            if (message.split()[i].decode() == 'same-origin'):
                json_index = i + 1
                break
        for i in range(json_index, len(message.split())):
            json_str += message.split()[i].decode()
        print("JSON_STR: {}".format(json_str))
        return json.loads(json_str)

    '''
    Sends HTML File
    filename - string for HTML filename
    '''
    def SendHTMLFile(self, filename):
        print('Sending {0}'.format(filename))
        f = open(filename, 'rb')
        outputdata = f.readlines()
        f.close()
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            self.connectionSocket.send(outputdata[i])
        self.connectionSocket.close()

    '''
    Sends Not Found HTML file
    '''
    def NotFound(self):
        notFound = open("NotFound.html",)
        outputdata = ["<html>", "<body>", "<h1>", "404 Not Found", "</h1>", "</body>", "</html>"]
        notFound.close()
        #Send response message for file not found
        self.connectionSocket.send(str.encode("HTTP/1.1 404 NOT FOUND\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            self.connectionSocket.send(str.encode(outputdata[i]))
        self.connectionSocket.close()

    '''
    Server Loop
    '''
    def run(self):
        print('Ready to serve...')
        self.connectionSocket, addr = self.serverSocket.accept()
        print(f'Running at {addr}')
        try:
            message = self.connectionSocket.recv(1024)
            print(message)
            print(message.split())
            if(len(message.split()) > 0):
                if(message.split()[0].decode("utf-8") == 'GET'):
                    self.HttpGet(message)
                if(message.split()[0].decode("utf-8") == 'POST'):
                    self.HttpPost(message)
        except KeyboardInterrupt:
            self.serverSocket.close()
        except IOError:
            self.NotFound()

if __name__ == '__main__':
    server = WebServer()
    while True:
        server.run()
    server.serverSocket.close()
