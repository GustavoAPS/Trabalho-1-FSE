import sys
import json
import socket
import threading
import board
import adafruit_dht

from time import sleep
from gpiozero import LED, Button, Buzzer


print("Config:")
print(sys.argv[1])

dicionario_configuracao = []

with open(sys.argv[1]) as arquivo_entrada:
    dicionario_configuracao = json.load(arquivo_entrada)


#mensagens no formato json
fila_mensagens_para_envio = []

servidor = '164.41.98.26'
port = 10091

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);
clientSocket.connect((servidor, port));


def metodo_recebimento_mensagens(fila_mensagens):
    while True:
        sleep(0.1)
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
        sleep(0.15)
        if len(fila_mensagens) != 0:
            print(fila_mensagens)
            for mensagem in fila_mensagens:
                clientSocket.sendto((json.dumps(mensagem)).encode(), (servidor, port))
            fila_mensagens.clear()



thread_envio_mensagem = threading.Thread(target=metodo_recebimento_mensagens, args=(fila_mensagens_para_envio, ))
thread_envio_mensagem.start()

thread_recebimento_mensagem = threading.Thread(target=metodo_envio_mensagens, args=(fila_mensagens_para_envio, ))
thread_recebimento_mensagem.start()

#-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------#

def leitor_temperatura():

    dict_relatorio = {'Temperatura':""}
    dhtDevice = adafruit_dht.DHT22(board.D4, use_pulseio=False)
    complemento = "Temperatura: "

    try:
        temperature_c = dhtDevice.temperature
        temperature_f = temperature_c * (9 / 5) + 32
        humidity = dhtDevice.humidity
        complemento += str(dhtDevice.temperature)
        complemento += " Umidade: "
        complemento += str(dhtDevice.humidity)
        dict_relatorio = {'Temperatura':complemento}
        #dict_relatorio = {"temperatura":str("Temperatura: {:.1f} F / {:.1f} C    Umidade: {}% ".format(temperature_f, temperature_c, humidity))}

    except RuntimeError as error:
        print(error.args[0])

    except Exception as error:
        dhtDevice.exit()
        raise error

    return dict_relatorio


def interruptor_aparelhos( aparelho: int, estado: bool):

    #lampada 1
    led_1 = LED(dicionario_configuracao["outputs"][0]["gpio"])

    #lampada 2
    led_2 = LED(dicionario_configuracao["outputs"][1]["gpio"])

    #projetor
    led_3 = LED(dicionario_configuracao["outputs"][2]["gpio"])

    #ar-condicionado
    led_4 = LED(dicionario_configuracao["outputs"][3]["gpio"])

    #alarme
    alarme_buzzer = Buzzer(dicionario_configuracao["outputs"][4]["gpio"])

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
            print("Ligando projetor")
            led_3.on()
        else:
            print("Desligando projetor")
            led_3.off()

    if aparelho == 3:
        if estado:
            print("Ligando ar-condicionado")
            led_4.on()
        else:
            print("Desligando ar-condicionado")
            led_4.off()

    if aparelho == 4:
        if estado:
            print("Ligando Alarme")
            alarme_buzzer.on()
        else:
            print("Desligando Alarme")
            alarme_buzzer.off()

    sleep(3)

sensor_presenca = Button(dicionario_configuracao["inputs"][0]["gpio"])
sensor_fumaca =   Button(dicionario_configuracao["inputs"][1]["gpio"])
sensor_janela =   Button(dicionario_configuracao["inputs"][2]["gpio"])
sensor_porta  =   Button(dicionario_configuracao["inputs"][3]["gpio"])
sensor_entrada =  Button(dicionario_configuracao["inputs"][4]["gpio"])
sensor_saida =    Button(dicionario_configuracao["inputs"][5]["gpio"])


while True:

    if sensor_entrada.is_pressed == False:
        print("Entrada Detectada")
        sleep(0.31)

    if sensor_saida.is_pressed == False:
        print("Saida Detectada")
        sleep(0.31)

    if sensor_presenca.is_pressed == False:
        #print("presenca detectada")
        fila_mensagens_para_envio.append({"Sensor presenca disparado":""})
        sleep(0.5)

    if sensor_fumaca.is_pressed == False:
        #print("fumaca detectada")
        fila_mensagens_para_envio.append({"Sensor fumaca disparado":""})
        sleep(0.5)

    if sensor_janela.is_pressed == False:
        #print("Janela detectada")
        fila_mensagens_para_envio.append({"Sensor janela disparado":""})
        sleep(0.5)

    if sensor_porta.is_pressed == False:
        #print("Janela detectada")
        fila_mensagens_para_envio.append({"Sensor porta disparado":""})
        sleep(0.5)

