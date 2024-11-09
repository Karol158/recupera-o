from Geral import Geral

class Moto(Geral):
      def __init__(self,marca,modelo,numero_chassi,ano,cor,preco,cilindrada,quilometragem):
            super().__init__(marca,modelo,numero_chassi,ano,cor,preco)    
            self.___cilindrada=cilindrada
            self.__quilometragem=quilometragem

      def getCilindrada(self):
          return self.___cilindrada
      def setCilindrada(self,cilindrada):
            self.___cilindrada=cilindrada
    
      def getQuilometragem(self):
          return self.__quilometragem
      def setQuilometragem(self,quilometragem):
            self.__quilometragem=quilometragem
            