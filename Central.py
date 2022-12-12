import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), 1234))
s.listen(5)

while True:
    clientsocket, address = s.accept()
    print(f"connection from {address} has been established")
    clientsocket.send(bytes("welcome to the server", "utf-8"))

# sala_01 = ServidorDistribuido(1)
# sala_02 = ServidorDistribuido(2)
# sala_03 = ServidorDistribuido(3)
# sala_04 = ServidorDistribuido(4)


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


def ligar_desligar_aparelhos():
    pass
    # sala = input("Qual sala voce deseja ligar-desligar aparelhos? \n[1,2,3,4]\n")
    # aparelho = input("Qual aparelho voce deseja ligar-desligar? \n"
    #                     "0 = lampada_01\n"
    #                     "1 = lampada_02\n"
    #                     "2 = ar_condicionado\n"
    #                     "3 = projetor\n"
    #                     "4 = alarme_buzzer\n"
    #                     "5 = sensor_presenca\n"
    #                     "6 = sensor_fumaca\n"
    #                     "7 = sensor_janela_01\n"
    #                     "8 = sensor_janela_02\n"
    #                     "9 = sensor_contagem_pessoas_entrada\n"
    #                     "10 = sensor_contagem_pessoas_saida\n"
    #                     "11 = sensor_temperatura_humidade\n")
    #
    # estado = input("O que voce deseja fazer \n 0 = desligar\n1 = ligar")
    #
    # operacao = True
    # if estado == '0':
    #     operacao = False
    #
    # if sala == '1':
    #     sala_01.interruptor_aparelhos(aparelho, operacao)
    #
    # if sala == '2':
    #     sala_02.interruptor_aparelhos(aparelho, operacao)
    #
    # if sala == '3':
    #     sala_03.interruptor_aparelhos(aparelho, operacao)
    #
    # if sala == '4':
    #     sala_04.interruptor_aparelhos(aparelho, operacao)



controle = '1'

while controle != '0':
    print("Menu")
    print("1 - Ligar ou Desligar Aparelhos")
    print("2 - relatorio de sala")
    print("3 - relatorio de todas as salas")
    print("0 - Encerrar")

    controle = input()

    if controle == '1':
        ligar_desligar_aparelhos()

    if controle == '2':
        relatorio_sala()

    if controle == '3':
        relatorio_todas_salas()
