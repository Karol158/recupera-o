from Geral import Geral

class Caminhao(Geral):
       def __init__(self, marca, modelo, numero_chassi, ano, cor, preco,qtd_eixos,quilometragem):
              super().__init__(marca, modelo, numero_chassi, ano, cor, preco)
              self.__qtd_eixos=qtd_eixos
              self.__quilometragem=quilometragem
       def getQtdeixos(self):
              return self.__qtd_eixos
       def setQtdeixos(self,qtd_eixos):
              self.__qtd_eixos=qtd_eixos

       def getQuilometragem(self):
          return self.__quilometragem
       def setMarca(self,quilometragem):
             self.__quilometragem=quilometragem
        