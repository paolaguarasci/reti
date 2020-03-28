from socket import *
from time import time

serverName = '127.0.0.1'
serverPort = 5555

# creo il socket
clientSocket = socket(AF_INET, SOCK_STREAM)

# qui invece di bindare, come ho fatto sul server, dico 
# "mi voglio connettere". Mi servono sia IP che PORTA.
clientSocket.connect((serverName,serverPort))

# prendo da input la frase
sentence = input('Frase in minuscolo:')
start = time()
### operazioni simmetriche rispetto al server
# inizio scrivendo sul buffer
clientSocket.makefile("w").writelines(sentence+"\n") 

# continuo leggendo dal buffer la frase elaborata dal server
modifiedSentence = clientSocket.makefile().readline() 
stop = time()
# stampo il risultato dell'elaborazione 
print("FROM SERVER: ", modifiedSentence) 
print("--- %s seconds ---" % (stop-start))

# chiudo la connessione
clientSocket.close()