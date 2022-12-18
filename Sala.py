class Sala:
  def __init__(self):
    
    self.numero_sala = 0

    self.numero_pessoas = 0

    self.temperatura = 0.00

    #false para desligado, true para ligado
    self.lampada_1 = False
    self.lampada_2 = False
    self.ar_condicionado = False
    self.projetor = False

    self.alarme_buzzer = False
    self.sensor_presenca = False
    self.sensor_fumaca = False
    self.sensor_janela_1 = False
    self.sensor_janela_2 = False


  def relatorio_sala(self):
      print(f"------------------------------------------")
      print(f"Dados da Sala {self.numero_sala}")
      print(f"")
      print(f"Ocupantes: {self.numero_pessoas}")
      print(f"temperatura: {self.temperatura}")
      print(f"")
      print(f"Lampada 1        ON") if self.lampada_1 else print(      f"Lampada 1        OFF")
      print(f"Lampada 2        ON") if self.lampada_2 else print(      f"Lampada 2        OFF")
      print(f"Ar condicionado  ON") if self.ar_condicionado else print(f"Ar condicionado  OFF")
      print(f"Projetor         ON") if self.projetor else print(      f"Projetor         OFF")
      print(f"------------------------------------------")


  def atualiza_temperatura(self, temperatura):
    self.temperatura = temperatura


  def interruptor_aparelhos(self, aparelho: int, estado: bool):

    if aparelho == 0:
      self.lampada_1 = estado
        
    if aparelho == 1:
      self.lampada_2 = estado

    if aparelho == 2:
      self.ar_condicionado = estado

    if aparelho == 3:
      self.projetor = estado


  def atualiza_dados(self):
      print("atualiza dados chamado")