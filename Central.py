import threading
import socket
from csv import writer
from time import sleep
from datetime import datetime
from os.path import exists


# reponsabilidades:
#
# 1 - Manter conexao com distribuido
#
# 2 - Prover uma interface que mantenham atualizadas as seguintes informações:
#   2.1 Estado das entradas (Sensores)
#   2.2 Estado das Saídas (lâmpadas, aparelhos de ar, etc.)
#   2.3 Valor da temperatura e umidade de cada sala a cada 2 segundos
#   2.4 Contador de Ocupação (Número de Pessoas) presentes no prédio como um todo e a ocupação individual de cada sala
#
# 3 - Prover mecanismo de interface para:
#   3.1 - Acionar manualmente lâmpadas, aparelhos de ar-condicionado e projetores das salas;
#   3.2 - Acionamento do sistema de alarme que, quando estiver ligado, deve tocar um som de alerta (acionar a sirene/buzzer) ao detectar presenças ou abertura de portas/janelas;
#   3.3 - Acionamento de alarme de incêncio que, ao detectar presença de fumaça a qualquer momento deve soar o alarme;
#
# 4 - Manter log (em arqvuio CSV) dos comandos acionados pelos usuários e do acionamento dos alarmes com data e hora e cada evento;
#



def relatorio_sala():
    pass
    # print("Salas disponiveis: 1,2,3,4")
    # sala_escolhida = input("Qual sala voce desejar ver o relatorio?\n")
    # if sala_escolhida == '1':
    #     sala_01.apresentar_relatorio_sala()
    #
    # if sala_escolhida == '2':
    #     sala_02.apresentar_relatorio_sala()
    #
    # if sala_escolhida == '3':
    #     sala_03.apresentar_relatorio_sala()
    #
    # if sala_escolhida == '4':
    #     sala_04.apresentar_relatorio_sala()


def relatorio_todas_salas():
    pass
    # print("relatorio de todas as salas")
    # sala_01.apresentar_relatorio_sala()
    # sala_02.apresentar_relatorio_sala()
    # sala_03.apresentar_relatorio_sala()
    # sala_04.apresentar_relatorio_sala()


# funcionando direitinho
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

    sala = input("Qual sala voce deseja ligar-desligar aparelhos? \n[1,2,3,4]\n")

    aparelho = input("Qual aparelho voce deseja ligar-desligar? \n"
                        "0 = lampada_01\n"
                        "1 = lampada_02\n"
                        "2 = ar_condicionado\n"
                        "3 = projetor\n")
    
    estado = input("O que voce deseja fazer \n1 = ligar\n0 = desligar\n")
    
    operacao = True
    
    if estado == '0':
        operacao = False
    
    if sala == '1':
        print("Chamar funcao de ligar aparelho")
        #sala_01.interruptor_aparelhos(aparelho, operacao)
    
    if sala == '2':
        print("Chamar funcao de ligar aparelho")
         #sala_02.interruptor_aparelhos(aparelho, operacao)
    
    if sala == '3':
        print("Chamar funcao de ligar aparelho")
        #sala_03.interruptor_aparelhos(aparelho, operacao)
    
    if sala == '4':
        print("Chamar funcao de ligar aparelho")
        #sala_04.interruptor_aparelhos(aparelho, operacao)


controle = '1'

while controle != '0':

    print("Menu")
    print("1 - Ligar ou Desligar Aparelhos")
    print("2 - relatorio de sala")
    print("3 - relatorio de todas as salas")
    print("4 - enviar mensagem para cliente")
    print("5 - Registrar log")
    print("0 - Encerrar")

    controle = input()

    if controle == '1':
        ligar_desligar_aparelhos()

    if controle == '2':
        relatorio_sala()

    if controle == '3':
        relatorio_todas_salas()

    if controle == '4':
        enviar_mensagem_cliente()
    
    if controle == '5':
        mensagem = input("o que deseja registrar no log?")
        registrar_log(mensagem)
