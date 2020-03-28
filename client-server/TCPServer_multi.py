from socket import *
from threading import Thread
from time import sleep

class Server(Thread):
    def __init__(self, socket):
        super().__init__()
        self.socket = socket

    def run(self):
        clientSentence = self.socket.makefile("r").readline()
        clientSentence = clientSentence[:-1]
        capitalizedSentence = clientSentence.upper() + " elaborato da " + self.name
        print(capitalizedSentence)
        sleep(10)
        self.socket.makefile("w").writelines(capitalizedSentence+"\n")
        self.socket.close()

serverPort = 5555
welcomeSocket = socket(AF_INET,SOCK_STREAM)
welcomeSocket.bind(('',serverPort))
welcomeSocket.listen(10) 

while 1:
    connectionSocket, addr = welcomeSocket.accept()
    server = Server(connectionSocket)
    server.start()