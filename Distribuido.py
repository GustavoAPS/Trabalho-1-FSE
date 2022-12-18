import threading
import socket
import json
import random
#from gpiozero import LED


numero_sala = 0

#led_1 = LED(18)
#led_2 = LED(23)
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


def serve(lampada_1):

    clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

    clientSocket.connect((socket.gethostname(), 1234));

    while True:

        response = ""

        dataFromServer = clientSocket.recv(1024)

        #print(dataFromServer.decode())

        function_dict = json.loads(dataFromServer.decode())
        print(type(function_dict))
        print(function_dict)

        if "ligar_desligar_aparelho" in function_dict.keys():
            print("Key ligar_desligar_aparelho encontrada")
            interruptor_aparelhos(function_dict["ligar_desligar_aparelho"][0],function_dict["ligar_desligar_aparelho"][1])
            response = {"Aparelho ligado/desligado":""}


        if "Temperatura" in function_dict.keys():
            response = leitor_temperatura()

        else:
            response = {"Default response":1}

        clientSocket.send((json.dumps(response)).encode())


t = threading.Thread(target=serve, args=(lampada_1, ))
t.start()


#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#
# DEPRECATED
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

    print(f"Interruptor chamado, aparelho {aparelho} estado {estado}")

    if aparelho == 0:
        if estado:
            print("Ligando lampada 1")
            #led_1.on()
        else:
            print("Desligando lampada 1")
            #led_1.off()

    if aparelho == 1:
        if estado:
            print("Ligando lampada 2")
            #led_2.on()
        else:
            print("Desligando lampada 2")
            #led_2.off()

    if aparelho == 2:
        if estado:
            print("Ligando ar condicionado")
            #led_3.on()
        else:
            print("Desligando ar condicionado")
            #led_3.off()

    if aparelho == 3:
        if estado:
            print("Ligando Projetor")
            #led_3.on()
        else:
            print("Desligando Projetor")
            #led_3.off()
   