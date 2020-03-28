from socket import *

serverPort = 6789
# creo un socket
welcomeSocket = socket(AF_INET,SOCK_STREAM)

# assegna un IP e una porta al socket
# (l'ip deve corrispondere ad un ip dei NIC presenti sulla macchina)
# se non specifico niente sto in ascolto su tutte le interfacce
# con '' sto dicendo 0.0.0.0, cioe' *, tutte le interfacce
welcomeSocket.bind(('',serverPort))

# mi metto in ascolto, ovvero accetto connessioni in entrata
# il numero tra parentesi e' il numero di connessioni che possono accodare
# al momento e' un server mono thread
welcomeSocket.listen(5) 

# ciclo principale di vita del server
# in un vero programma non posso usare un while true 
# ma devo prevedere condizioni di uscita
while 1:  
    # mi prendo la prima telefonata nel buffer "listen"
    # e' bloccante, se e' vuoto il server sta in attesa
    # restituisce due cose: 
    #   un oggetto Socket
    #   l'indirizzo del chiamante
    # l'oggetto socket ricevuto e' gia connesso all'altra estremita', 
    # e' diverso dal socket creato prima che e' un socket di ascolto, serve ad aspettare le chiamate.
    # Nel connectionSocket, lato server, e' gia stato allocato un buffer di invio euno di ricezione
    # e il nostro client ha un buffer di ricezione euno di trasmissione.
    connectionSocket, addr = welcomeSocket.accept()

    # Con makefile() su connectionSocket ottengo un oggetto File sul quale posso invocare i tipici metodi dei file
    # anche readline(), legge riga per riga fino a \n (escluso). Attenzione "r", lettura, e' un parametro inmplicito.
    clientSentence = connectionSocket.makefile("r").readline() 

    # Elaborazione del dato...
    capitalizedSentence = clientSentence.upper() 

    # Scrivo il risultato dell'elaborazione sul buffer di scrittura del socket
    # writelines si aspetta che ci sia '\n' alla fine della riga, altrimenti si blocca
    connectionSocket.makefile("w").writelines(capitalizedSentence+"\n")

    # Chiudo la connessione con il client (connectionSocket)
    # non il socket creato all'inizio
    connectionSocket.close()