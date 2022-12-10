from Distribuido import ServidorDistribuido

sala_01 = ServidorDistribuido(1)
sala_02 = ServidorDistribuido(2)
sala_03 = ServidorDistribuido(3)
sala_04 = ServidorDistribuido(4)


def relatorio_sala():
    print("Salas disponiveis: 1,2,3,4")
    sala_escolhida = input("Qual sala voce desejar ver o relatorio?")
    if sala_escolhida == '1':
        sala_01.apresentar_relatorio_sala()

    if sala_escolhida == '2':
        sala_02.apresentar_relatorio_sala()

    if sala_escolhida == '3':
        sala_03.apresentar_relatorio_sala()

    if sala_escolhida == '4':
        sala_04.apresentar_relatorio_sala()


def relatorio_todas_salas():
    print("relatorio de todas as salas")
    sala_01.apresentar_relatorio_sala()
    sala_02.apresentar_relatorio_sala()
    sala_03.apresentar_relatorio_sala()
    sala_04.apresentar_relatorio_sala()


controle = '1'

while controle != '0':
    print("Menu")
    print("1 - Ligar ou Desligar Aparelhos")
    print("2 - relatorio de sala")
    print("3 - relatorio de todas as salas")
    print("0 - Encerrar")

    controle = input()

    if controle == '1':
        relatorio_sala()

    if controle == '2':
        relatorio_sala()

    if controle == '3':
        relatorio_todas_salas()

sala_01.apresentar_relatorio_sala()
sala_01.liga_primeira_lampada()
sala_01.apresentar_relatorio_sala()

