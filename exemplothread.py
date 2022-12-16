from threading import Thread, Event
from time import sleep
import socket


message_to_client = "adagio"
my_var = [1, 2, 3]
event = Event()


def NetworkServerServe(message):
    serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serverSocket.bind((socket.gethostname(), 1234))
    serverSocket.listen(5)

    while True:
        (clientConnected, clientAddress) = serverSocket.accept()

        print("Accepted a connection request from %s:%s"%(clientAddress[0], clientAddress[1]))
        
        clientConnected.send(bytes(message_to_client, "utf-8"))

        dataFromClient = clientConnected.recv(1024)

        print(dataFromClient.decode());
        
        print("Rodando")
        sleep(.5)


def Numbers(var):
    while True:
        for i in range(len(var)):
            var[i] += 1
        if event.is_set():
            break
        sleep(.5)
    print('Stop printing')        


t = Thread(target=NetworkServerServe, args=(message_to_client, ))
t.start()


while True:
    try:
        message_to_client = input("What is the message")
    except KeyboardInterrupt:
        event.set()
        break
t.join()
print(my_var)