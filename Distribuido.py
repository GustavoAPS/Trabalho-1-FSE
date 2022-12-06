

class ServidorDistribuido:
    def __init__(self, numero):
        self.numero_sala = numero
        self.lampada_01 = False
        self.lampada_02 = False
        self.ar_condicionado = False
        self.projetor = False
        self.alarme_buzzer = False
        self.sensor_presenca = False
        self.sensor_fumaca = False
        self.sensor_janela_01 = False
        self.sensor_janela_02 = False
        self.sensor_contagem_pessoas_entrada = False
        self.sensor_contagem_pessoas_saida = False
        self.sensor_temperatura_humidade = False

    def apresentar_relatorio_sala(self):
        print("\n----------------------------------------------")

        print(f"Relatorio da Sala {self.numero_sala}")

        if self.lampada_01:
            print("Lampada 1 ligada")
        else:
            print("Lampada 1 desligada")
        print("----------------------------------------------")


    def liga_primeira_lampada(self):
        self.lampada_01 = True

    def desliga_primeira_lampada(self):
        self.lampada_01 = False



