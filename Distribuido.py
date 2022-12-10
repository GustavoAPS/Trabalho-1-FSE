

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

        print(".")
        print(f"Relatorio da Sala {self.numero_sala}")
        self.printar_status("Lampada 01 - ", self.lampada_01)
        self.printar_status("Lampada 02 - ", self.lampada_02)
        self.printar_status("Ar condicionado - ", self.ar_condicionado)
        self.printar_status("Projetor - ", self.projetor)
        self.printar_status("Alarme - ", self.alarme_buzzer)
        self.printar_status("Sensor presenca - ", self.sensor_presenca)
        self.printar_status("Sensor fumaca - ", self.sensor_fumaca)
        self.printar_status("Sensor janela 01 - ", self.sensor_janela_01)
        self.printar_status("Sensor janela 02 - ", self.sensor_janela_02)
        self.printar_status("Sensor entrada pessoas - ", self.sensor_contagem_pessoas_entrada)
        self.printar_status("Sensor saida pessoas - ", self.sensor_contagem_pessoas_saida)
        self.printar_status("Sensor temperatura - ", self.sensor_temperatura_humidade)
        print(".")

    def printar_status(self, aparelho: str, estado: bool):
        if estado:
            print(f"{aparelho} ligado")
        else:
            print(f"{aparelho} desligado")

    def interruptor_aparelhos(self, aparelho: str, estado: bool):
      return True

    def liga_primeira_lampada(self):
        self.lampada_01 = True

    def desliga_primeira_lampada(self):
        self.lampada_01 = False

    def liga_segunda_lampada(self):
        self.lampada_02 = True

    def desliga_segunda_lampada(self):
        self.lampada_02 = False

    def liga_ar_condicionado(self):
        self.ar_condicionado = True

    def desliga_ar_condicionado(self):
        self.ar_condicionado = False

