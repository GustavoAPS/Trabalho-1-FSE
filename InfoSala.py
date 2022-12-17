class InfoSala:
  def __init__(self, name, age):
    
    self.numero_sala = 0

    self.numero_pessoas = 0

    self.temperatura = 0.00

    #false para desligado, true para ligado
    self.lampada_1 = False
    self.lampada_02 = False
    self.ar_condicionado = False
    self.projetor = False

    self.alarme_buzzer = False
    self.sensor_presenca = False
    self.sensor_fumaca = False
    self.sensor_janela_01 = False
    self.sensor_janela_02 = False

    def atualiza_dados():
        print("atualiza dados chamado")