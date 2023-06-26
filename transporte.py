# Clases abstractas

from abc import ABC, abstractmethod

class Transporte(ABC):
  @abstractmethod
  def acelerar():
    pass
  @abstractmethod
  def calular_ruta():
    pass
  @abstractmethod
  def calcular_paradas():
    pass
  @abstractmethod
  def frenar():
    pass


class Mexibus(Transporte):
  
    def acelerar(self):
        print("Estoy acelerando")

    def calular_ruta(self):
        print("Estoy calculando la rua del Mexibus")

g = Mexibus() 
g.acelerar()
g.calular_ruta()