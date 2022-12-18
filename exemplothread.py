from threading import Thread, Event
from time import sleep
import socket


my_var = []
event = Event()


serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((socket.gethostname(), 1234))
serverSocket.listen(5)

(clientConnected, clientAddress) = serverSocket.accept()

def send_messages(message:list):
    while True:
        if len(message) != 0:
            clientConnected.send(bytes(message[len(message) - 1], "utf-8"))
            message.pop()

def receive_messages():
    while True:
        dataFromClient = clientConnected.recv(1024)
        print(dataFromClient.decode())
         

t = Thread(target=send_messages, args=(my_var, ))
t.start()

t2 = Thread(target=receive_messages)
t2.start()



while True:
    try:
        my_var.append(input("What is the message "))
    except KeyboardInterrupt:
        event.set()
        break
t.join()
t2.join()
print(my_var)