'''
Name of team members: Anjola, Brandon, Craig
Project Description: A web anonymous voting application built using the client-server archiceture.
Anjola's Contribution: Transformed the code from Homework 3 into the WebServer class. Added functions so that the WebServer class can process HTTP POST requests with JSON data embedded.
Brandon's Contribution:
Craig's Contribution: Managed refreshing HTML elements using JQuerry functions and sending data to and receiving data from the server. Defined the HTML structure.
'''


from socket import *
import re
import json

class WebServer:
    """
    A class used to represent a Web Server

    Attributes
    ----------
    serverSocket: socket
        socket used to establish a tcp connection with the client
    serverPort: int
        Port of the server
    rePatternForFiles: re object
        Regular Expression used to determine if a url in a socket is referencing a file
    totalNumOfPartcipants: int
        Stores number of quiz particpants
    questions: Array
        Array of objects representing the questions of the quiz
    quizResponses: Array
        Array of objects represent all the answers of each client
    questionTally: Dict
        Stores tally of the submitted answers    

    Methods
    -------
    HttpGet(message)
        Handler for any HTTP GET requets that arrive
    HttpPost(message)
        Handler for any HTTP POST requets that arrive
    RegisterUser()
        Sends a new user id to the client
    echo(message)
        Sends the client any data stored in the Body of the HTTP POST request
    getTally()
        Sends the client a tally of answers
    getQuestionsById(id)
        Sends the client a JSON string containing: a path to the question image and the options for the questions
    acceptAnswer(answer)
        Updates the tally and records the answer
    GetJsonBody(message)
        Converts the JSON string in the HTTP POST Request body into a python object
    SendHTMLFile(filename)
        Sends the client a file specified by filename
    NotFound()
        Sends the client a NOT FOUND html filename
    run()
        Opens the port and recieves packets on specificed ports
    """

    def __init__(self, portNumber=6789):
        """
        Parameters
        ----------
        portNumber: int
            Port Number that the web host will be hosted on. Defaulted to 6789
        """
        self.serverSocket = socket(AF_INET, SOCK_STREAM) #Borrowed from Homework 3
        self.serverSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1) #Borrowed from https://stackoverflow.com/questions/47958473/how-to-reuse-the-socket-address-python

        self.serverPort = portNumber
        self.serverSocket.bind(('', self.serverPort)) #Borrowed from Homework 3
        self.serverSocket.listen(1) #Borrowed from Homework 3
        self.rePatternForFiles = re.compile("(\w+[\/])?\w+[.]{1}\w+")
        self.totalNumOfPartcipants = 0
        with open("questions.json", "r") as f:
            self.questions = json.load(f)
        self.quizResponses = []
        self.questionTally = {}
        for i in range(len(self.questions)):
            self.questionTally[str(i+1)] = {}
            self.questionTally[str(i+1)][self.questions[str(i+1)]['option1']] = 0
            self.questionTally[str(i+1)][self.questions[str(i+1)]['option2']] = 0

    def HttpGet(self, message):
        """Handler for any HTTP GET requets that arrive

        Parameters
        ----------
        message : packet object
            Object that represents the socket message

        Raises
        ------
        IOError
            If file is not found
        """
        filename = message.split()[1].decode("utf-8")[1:]
        if(self.rePatternForFiles.match(filename)):
            self.SendHTMLFile(filename)
        elif(filename == ''):
            self.SendHTMLFile('index.html')
        elif(filename == 'GetTally'):
            self.getTally()
        elif(filename == 'GetTallyById'):
            with open("tallyTest.json", "r") as f:
                self.quizResponses = json.load(f)
            requestBody = self.GetJsonBody(message)
            self.getTallyById(requestBody['user_id'])
        elif(filename == "RegisterUser"):
            self.RegisterUser()
        else:
            raise IOError

    def HttpPost(self, message):
        """Handler for any HTTP POST requets that arrive

        Parameters
        ----------
        message : packet object
            Object that represents the socket message
        """
        endpoint = message.split()[1].decode("utf-8")[1:]
        if(endpoint == "echo"):
            self.echo(message)
        elif(endpoint == 'getQuestionsById'):
            question_id = self.GetJsonBody(message)['question_id']
            self.getQuestionsById(question_id)
        elif(endpoint == 'acceptAnswer'):
            answer = self.GetJsonBody(message)
            self.acceptAnswer(answer)
        else:
            self.connectionSocket.send(str.encode("HTTP/1.1 404 Not Found\nContent-Type: text/plain\n\n"))
            self.connectionSocket.send(str.encode("Can not find endpoint"))
            self.connectionSocket.close()

    def RegisterUser(self):
        """Sends a new user id to the client
        """
        self.totalNumOfPartcipants += 1
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n"))
        self.connectionSocket.send(str.encode(json.dumps({"user_id": self.totalNumOfPartcipants})))
        self.connectionSocket.close()

    def echo(self, message):
        """Sends the client any data stored in the Body of the HTTP POST request

        Parameters
        ----------
        message : packet object
            Object that represents the socket message
        """
        echo_message = self.GetJsonBody(message)
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n"))
        self.connectionSocket.send(str.encode("Hit Post. Endpoint: ") + message.split()[1] + str.encode("\n"))
        self.connectionSocket.send(str.encode("Body of POST call: " + json.dumps(echo_message)))
        self.connectionSocket.close()

    def getTally(self):
        """Sends the client a tally of answers
        """
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n"))
        self.connectionSocket.send(str.encode(json.dumps(self.questionTally)))
        self.connectionSocket.close()

    def getQuestionsById(self, id):
        """
        Sends the client a JSON string containing: a path to the question image and the options for the questions

        Parameter
        ---------
        id : int
            Id of question
        """
        question = self.questions[str(id)]
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n"))
        self.connectionSocket.send(str.encode(json.dumps(question)))
        self.connectionSocket.close()
        
    def acceptAnswer(self, answer):
        """Updates the tally and records the answer

        Parameter
        ---------
        answer: Dictionary
            Contains question_id, answer and user_id variables
        """
        questionAnswered = False
        quizResponseIndex = -1
        curr_answer = ""
        for i in range(len(self.quizResponses)):
            if(self.quizResponses[i]['user_id'] == answer['user_id'] and self.quizResponses[i]['question_id'] == answer['question_id']):
                questionAnswered = True
                quizResponseIndex = i
                break
        if(questionAnswered):
            self.questionTally[str(answer['question_id'])][self.quizResponses[quizResponseIndex]['answer']] -= 1
            self.quizResponses[quizResponseIndex]['answer'] = answer['answer']
            self.questionTally[str(answer['question_id'])][answer['answer']] += 1
        else:
            self.quizResponses.append(answer)
            self.questionTally[str(answer['question_id'])][answer['answer']] += 1
        
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/plain\n\n"))
        self.connectionSocket.send(str.encode(json.dumps(self.quizResponses)))
        self.connectionSocket.close()

    def GetJsonBody(self, message):
        """Converts the JSON string in the HTTP POST Request body into a python object

        Parameter
        ---------
        message : packet object
            Object that represents the socket message
        """
        json_str = ""
        json_str = message.split(b'\r\n\r\n')[-1].decode()
        print("JSON_STR: {}".format(json_str))
        return json.loads(json_str)

    def SendHTMLFile(self, filename):
        #Borrowed from Homework 3
        """Sends HTML File
        
        Parameter
        ---------
        filename : string 
            Sends over file specified by filename
        """        
        print('Sending {0}'.format(filename))
        f = open(filename, 'rb')
        outputdata = f.readlines()
        f.close()
        self.connectionSocket.send(str.encode("HTTP/1.1 200 OK\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            self.connectionSocket.send(outputdata[i])
        self.connectionSocket.close()

    def NotFound(self):
        #Borrowed from Homework 3
        """
        Sends Not Found HTML file
        """
        notFound = open("NotFound.html",)
        outputdata = ["<html>", "<body>", "<h1>", "404 Not Found", "</h1>", "</body>", "</html>"]
        notFound.close()
        #Send response message for file not found
        self.connectionSocket.send(str.encode("HTTP/1.1 404 NOT FOUND\nContent-Type: text/html\n\n"))
        for i in range(0, len(outputdata)):
            self.connectionSocket.send(str.encode(outputdata[i]))
        self.connectionSocket.close()


    def run(self):
        """
        Opens the port and recieves packets on specificed ports
        """
        print('Ready to serve...')
        self.connectionSocket, addr = self.serverSocket.accept() #Borrowed from Homework 3
        print(f'Running at {addr}')
        try:
            message = self.connectionSocket.recv(4096) #Borrowed from Homework 3
            if(len(message.split()) > 0):
                if(message.split()[0].decode("utf-8") == 'GET'):
                    self.HttpGet(message)
                if(message.split()[0].decode("utf-8") == 'POST'):
                    self.HttpPost(message)
        except KeyboardInterrupt:
            self.serverSocket.close()
        except IOError:
            self.NotFound()
        except Exception as e:
            print(e)

if __name__ == '__main__':
    server = WebServer()
    while True:
        server.run()
    #server.serverSocket.close()
