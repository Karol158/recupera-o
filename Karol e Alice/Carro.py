from Geral import Geral

class Carro(Geral):
        
        def __init__(self, marca, modelo, numero_chassi, ano, cor,preco,potencia,quilometragem):
                super().__init__(marca, modelo, numero_chassi, ano, cor,preco)

                self.__potencia=potencia
                self.__quilometragem=quilometragem

        def getPotencia(self):
          return self.__potencia
        def setPotencia(self,potencia):
            self.__potencia=potencia

        def getQuilometragem(self):
          return self.__quilometragem
        def setQuilometragem(self,quilometragem):
             self.__quilometragem=quilometragem
        