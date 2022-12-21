from threading import Thread, Event
from csv import writer
from time import sleep
from datetime import datetime
from os.path import exists

import socket
import Sala as info
import json



sala_01 = info.Sala()
fila_instrucoes = []
fila_respostas = []
event = Event()

ip_servidor = '164.41.98.26'
porta = 10091

serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serverSocket.bind((ip_servidor, porta))

serverSocket.listen(5)

# Programa só vai prosseguir se tiver uma conexão
(clientConnected, clientAddress) = serverSocket.accept()


# THREAD MANDAR MENSAGEM
def send_messages(message:list):
    while True:
        if len(message) != 0:
            clientConnected.send(bytes(message[len(message) - 1], "utf-8"))
            message.pop()
            sleep(0.1)


# THREAD RECEBER MENSAGEM
def receive_messages(fila_respostas):
    while True:
        dataFromClient = clientConnected.recv(1024)
        print("Data received = " + dataFromClient.decode())
        fila_respostas.append(json.loads(dataFromClient.decode()))
        sleep(0.1)

t = Thread(target=send_messages, args=(fila_instrucoes, ))
t.start()

t2 = Thread(target=receive_messages, args=(fila_respostas, ))
t2.start()


# Função de registrar os logs do projeto
def registrar_log(mensagem_registro):

    if exists('log.csv') == False:
        with open('log.csv','w', encoding='UTF8') as log_file:
            writter = writer(log_file)
            data = ["mensagem", "data do registro", "hora do registro"]
            writter.writerow(data)

    now = datetime.now()
    
    # dd/mm/YY H:M:S
    data_do_registro = now.strftime("%d/%m/%Y")
    hora_do_registro = now.strftime("%H:%M:%S")

    List = [mensagem_registro, data_do_registro, hora_do_registro]
    
    with open('log.csv', 'a') as f_object:
    
        writer_object = writer(f_object)    
        writer_object.writerow(List)
        f_object.close()



def ligar_desligar_aparelhos():

    print("\n")
    print(" _____________ Ligar | Desligar _____________")
    print("|                                            |\n")
    print("| Qual aparelho voce deseja ligar-desligar?  |")
    print("| 1 - Ligar ou Desligar Aparelhos            |")
    print("| 2 - relatorio de sala                      |")
    print("| 0 = lampada_01                             |")
    print("| 1 = lampada_02                             |")
    print("| 2 = projetor                               |")
    print("| 3 = ar condicionado                        |")
    print("| 4 = Alarme                                 |")
    print("|============================================|\n")


    aparelho = input()

    estado = input("O que voce deseja fazer \n1 = ligar\n0 = desligar\n")

    valor_em_bool = True

    if estado == '0':
        valor_em_bool = False

    # mensagem que vai para o distribuido
    dict_relatorio = {'ligar_desligar_aparelho':[int(aparelho),valor_em_bool]}

    #registro no log do comando
    json_object = json.dumps(dict_relatorio)

    #envio da instrução para o distribuido
    fila_instrucoes.append(json_object)

    #atualiza dados locais da sala
    sala_01.interruptor_aparelhos(int(aparelho),valor_em_bool)


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
def AtualizaTemperatura(sala : info.Sala):

    while True:
        sleep(1)

        #print("Pedindo temperatura")

        dict_relatorio = {'Temperatura':''}
        json_object = json.dumps(dict_relatorio)
        fila_instrucoes.append(json_object)

        sleep(1)

        #print(f"Respostas = {fila_respostas}")

        for resposta in fila_respostas:
            for i in resposta:
                if i == "Temperatura":
                    sala.atualiza_temperatura(resposta[i])
                    fila_respostas.remove(resposta)


thread_atualizar_temperatura = Thread(target=AtualizaTemperatura, args=(sala_01, ))
thread_atualizar_temperatura.start()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def vigia_alarmes(fila_respostas):
    while True:
        sleep(1)
        for resposta in fila_respostas:
            for i in resposta:
                if i == "Sensor presenca disparado":
                    print("Sensor presenca disparado")
                    registrar_log("Sensor presenca disparado")
                    fila_respostas.remove(resposta)

                if i == "Sensor fumaca disparado":
                    print("Sensor fumaca disparado")
                    registrar_log("Sensor fumaca disparado")
                    fila_respostas.remove(resposta)

                if i == "Sensor janela disparado":
                    print("Sensor Janela disparado")
                    registrar_log("Sensor janela disparado")
                    fila_respostas.remove(resposta)

thread_vigiar_alarme = Thread(target=vigia_alarmes, args=(fila_respostas, ))
thread_vigiar_alarme.start()


while True:

    try:
        print("\n")
        print(" _______________ Menu_______________")
        print("|                                   |")
        print("| 1 - Ligar ou Desligar Aparelhos   |")
        print("| 2 - relatorio de sala             |")
        print("|===================================|\n")


        controle = input()

        if controle == '1':
            ligar_desligar_aparelhos()
            registrar_log("Aparelho ligado")

        if controle == '2':
            sala_01.relatorio_sala()
            registrar_log("Relatorio pedido")

    except KeyboardInterrupt:
        event.set()
        break


t.join()
t2.join()
thread_atualizar_temperatura.join()
