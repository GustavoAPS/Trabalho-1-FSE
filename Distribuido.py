import threading
import socket
import json
import random
from time import sleep
#import board
#import adafruit_dht


from gpiozero import LED, Button, Buzzer


numero_sala = 0
lampada_1 = False
lampada_2 = False
ar_condicionado = False
projetor = False
alarme_buzzer = False
sensor_presenca = False
sensor_fumaca = False
sensor_janela_1 = False
sensor_janela_2 = False
sensor_contagem_pessoas_entrada = False
sensor_contagem_pessoas_saida = False
sensor_temperatura_humidade = False

#mensagens no formato json
fila_mensagens_para_envio = []



clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect((socket.gethostname(), 10091));


def metodo_recebimento_mensagens(fila_mensagens):
    while True:

        dataFromServer = clientSocket.recv(1024)
        dicionario_resposta = json.loads(dataFromServer.decode())


        # Direcionamento para cada função dependendo do requerimento

        if "ligar_desligar_aparelho" in dicionario_resposta.keys():
            print("Key ligar_desligar_aparelho encontrada")
            interruptor_aparelhos(dicionario_resposta["ligar_desligar_aparelho"][0],dicionario_resposta["ligar_desligar_aparelho"][1])
            fila_mensagens.append({"Aparelho ligado/desligado":""})
            
        if "Temperatura" in dicionario_resposta.keys():       
            fila_mensagens.append(leitor_temperatura())




def metodo_envio_mensagens(fila_mensagens:dict):
    while True:
        
        if len(fila_mensagens) != 0:
            print(fila_mensagens)
            for mensagem in fila_mensagens:
                clientSocket.send((json.dumps(mensagem)).encode())
            fila_mensagens.clear()



thread_envio_mensagem = threading.Thread(target=metodo_recebimento_mensagens, args=(fila_mensagens_para_envio, ))
thread_envio_mensagem.start()

thread_recebimento_mensagem = threading.Thread(target=metodo_envio_mensagens, args=(fila_mensagens_para_envio, ))
thread_recebimento_mensagem.start()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DEPRECATED - tenho que atualizar
def apresentar_relatorio_sala():

    print(".")
    print(f"Relatorio da Sala {numero_sala}")
    print("Lampada 01             | ", lampada_1)
    print("Lampada 02             | ", lampada_2)
    print("Ar condicionado        | ", ar_condicionado)
    print("Projetor               | ", projetor)
    print("Alarme                 | ", alarme_buzzer)
    print("Sensor presenca        | ", sensor_presenca)
    print("Sensor fumaca          | ", sensor_fumaca)
    print("Sensor janela 01       | ", sensor_janela_1)
    print("Sensor janela 02       | ", sensor_janela_2)
    print("Sensor entrada pessoas | ", sensor_contagem_pessoas_entrada)
    print("Sensor saida pessoas   | ", sensor_contagem_pessoas_saida)
    print("Sensor temperatura     | ", sensor_temperatura_humidade)
    print(".")

    dict_relatorio = {
    'Lampada01':lampada_1,
    'Lampada02':lampada_2,
    'Arcondicionado':ar_condicionado,
    'Projetor':projetor,
    'Alarme':alarme_buzzer,
    'Sensorpresenca':sensor_presenca,
    'Sensorfumaca':sensor_fumaca,
    'Sensorjanela01':sensor_janela_1,
    'Sensorjanela02':sensor_janela_2,
    'Sensorentradapessoas':sensor_contagem_pessoas_entrada,
    'Sensorsaidapessoas':sensor_contagem_pessoas_saida,
    'Sensortemperatura':sensor_temperatura_humidade}

    json_object = json.dumps(dict_relatorio)
    
    return json_object
#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def leitor_temperatura():
    dict_relatorio = {'Temperatura':random.uniform(-10,40)}
    return dict_relatorio

def interruptor_aparelhos( aparelho: int, estado: bool):

    #lampada 1
    led_1 = LED(18)
    #lampada 2
    led_2 = LED(23)
    #ar condicionado
    led_3 = LED(25)
    #projetor
    led_4 = LED(24)
    #alarme 
    alarme_buzzer = Buzzer(8)

    print(f"Interruptor chamado, aparelho {aparelho} estado {estado}")

    if aparelho == 0:
        if estado:
            print("Ligando lampada 1")
            led_1.on()
        else:
            print("Desligando lampada 1")
            led_1.off()

    if aparelho == 1:
        if estado:
            print("Ligando lampada 2")
            led_2.on()
        else:
            print("Desligando lampada 2")
            led_2.off()

    if aparelho == 2:
        if estado:
            print("Ligando ar condicionado")
            led_3.on()
        else:
            print("Desligando ar condicionado")
            led_3.off()

    if aparelho == 3:
        if estado:
            print("Ligando Projetor")
            led_4.on()
        else:
            print("Desligando Projetor")
            led_4.off()

    if aparelho == 4:
        if estado:
            print("Ligando Alarme")
            alarme_buzzer.on()
        else:
            print("Desligando Projetor")
            alarme_buzzer.off()
   
    sleep(3)

sensor_presenca = Button(7)
sensor_fumaca = Button(1)
sensor_janela = Button(12)
#sensor_porta  = Button(16)
#sensor_entrada = Button(20)
#sensor_saida = Button(21)


while True:

    #entrada = input("1 entrada, 2 presenca")

    #if entrada == '1':
    if sensor_presenca.is_pressed == False:
        #print("presenca detectada")
        fila_mensagens_para_envio.append({"Sensor presenca disparado":""})
    
    
    #if entrada == '2':
    if sensor_fumaca.is_pressed == False:
        #print("fumaca detectada")
        fila_mensagens_para_envio.append({"Sensor fumaca disparado":""})

    #if entrada == '3':
    if sensor_janela.is_pressed == False:
        #print("Janela detectada")
        fila_mensagens_para_envio.append({"Sensor janela disparado":""})
        
    #if sensor_fumaca.is_pressed():
    #    print("fumaca detectada")
    sleep(1)
