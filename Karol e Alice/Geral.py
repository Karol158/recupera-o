class Geral:
    def __init__(self,marca,modelo,numero_chassi,ano,cor,preco):
          self.__marca=marca
          self.__modelo=modelo
          self.__numero_chassi=numero_chassi
          self.__ano=ano
          self.__cor=cor
          self.__preco=preco

    def getMarca(self):
          return self.__marca
    def setMarca(self,marca):
         self.__marca=marca
    
    def getModelo(self):
         return self.__modelo
    def setModelo(self,modelo):
         self.__modelo=modelo

    def getNumerocha(self):
         return self.__numero_chassi
    def setNumerocha(self,numero_chassi):
         self.__numero_chassi=numero_chassi

    def getAno(self):
         return self.__ano
    def setAno(self,ano):
         self.__ano=ano
    
    def getCor(self):
         return self.__cor
    def setCor(self,cor):
         self.__cor=cor

    def getPreco(self):
         return self.__preco
    def setPreco(self,preco):
         self.__preco=preco
                  
         
    