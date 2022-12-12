#----- A simple TCP client program in Python using send() function -----

import socket

# Create a client socket

clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

# Connect to the server

clientSocket.connect((socket.gethostname(), 1234));

# Send data to server

data = "Hello Server!";

clientSocket.send(data.encode());


# Receive data from server

dataFromServer = clientSocket.recv(1024);

# Print to the console

print(dataFromServer.decode());













numero_sala = 0
lampada_01 = False
lampada_02 = False
ar_condicionado = False
projetor = False
alarme_buzzer = False
sensor_presenca = False
sensor_fumaca = False
sensor_janela_01 = False
sensor_janela_02 = False
sensor_contagem_pessoas_entrada = False
sensor_contagem_pessoas_saida = False
sensor_temperatura_humidade = False


def apresentar_relatorio_sala(self):

    print(".")
    print(f"Relatorio da Sala {numero_sala}")
    printar_status("Lampada 01             | ", lampada_01)
    printar_status("Lampada 02             | ", lampada_02)
    printar_status("Ar condicionado        | ", ar_condicionado)
    printar_status("Projetor               | ", projetor)
    printar_status("Alarme                 | ", alarme_buzzer)
    printar_status("Sensor presenca        | ", sensor_presenca)
    printar_status("Sensor fumaca          | ", sensor_fumaca)
    printar_status("Sensor janela 01       | ", sensor_janela_01)
    printar_status("Sensor janela 02       | ", sensor_janela_02)
    printar_status("Sensor entrada pessoas | ", sensor_contagem_pessoas_entrada)
    printar_status("Sensor saida pessoas   | ", sensor_contagem_pessoas_saida)
    printar_status("Sensor temperatura     | ", sensor_temperatura_humidade)
    print(".")

def printar_status(self, aparelho: str, estado: bool):
    if estado:
        print(f"{aparelho} ligado")
    else:
        print(f"{aparelho} desligado")

def interruptor_aparelhos(self, aparelho: int, estado: bool):
    if aparelho == '0':
        lampada_01 = estado
    if aparelho == '1':
        lampada_02 = estado
    if aparelho == '2':
        ar_condicionado = estado
    if aparelho == '3':
        projetor = estado
    if aparelho == '4':
        alarme_buzzer = estado
    if aparelho == '5':
        sensor_presenca = estado
    if aparelho == '6':
        sensor_fumaca = estado
    if aparelho == '7':
        sensor_janela_01 = estado
    if aparelho == '8':
        sensor_janela_02 = estado
    if aparelho == '9':
        sensor_contagem_pessoas_entrada = estado
    if aparelho == '10':
        sensor_contagem_pessoas_saida = estado
    if aparelho == '11':
        sensor_temperatura_humidade = estado

