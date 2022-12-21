class Sala:
  def __init__(self):
    
    self.numero_pessoas = 0
    self.temperatura_umidade = ""

    #false para desligado, true para ligado
    
    self.sistema_alarme = False
    
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

      print("\n")
      print( " ___________________ Status Sala ___________________")
      print( "|")
      print(f"|Sistema Alarme   ON") if self.lampada_1 else print(      f"|Sistema Alarme   OFF")
      print( "|                                              ")
      print(f"|Ocupantes: {self.numero_pessoas}")
      print(f"|-{self.temperatura_umidade}-")
      print(f"|")
      print(f"|Lampada 1        ON") if self.lampada_1 else print(      f"|Lampada 1        OFF")
      print(f"|Lampada 2        ON") if self.lampada_2 else print(      f"|Lampada 2        OFF")
      print(f"|Ar condicionado  ON") if self.ar_condicionado else print(f"|Ar condicionado  OFF")
      print(f"|Projetor         ON") if self.projetor else print(       f"|Projetor         OFF")
      print( "|                                              ")
      print( "|==============================================|\n")


  def atualiza_ocupantes(self, ocupantes):
    self.numero_pessoas = ocupantes


  def interruptor_aparelhos(self, aparelho: int, estado: bool):

    if aparelho == 0:
      self.lampada_1 = estado
        
    if aparelho == 1:
      self.lampada_2 = estado

    if aparelho == 2:
      self.ar_condicionado = estado

    if aparelho == 3:
      self.projetor = estado
