from Geral import Geral

class Lancha(Geral):
       def __init__(self, marca, modelo, numero_chassi, ano, cor, preco,horas_util):
              super().__init__(marca, modelo, numero_chassi, ano, cor, preco)
              self.__horas_util=horas_util

       def getHoras(self):
              return self.__horas_util
       def setHoras(self,horas_util):
              self.__horas_util=horas_util
    