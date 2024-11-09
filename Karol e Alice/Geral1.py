class Geral1:
     def __init__(self,id,id_vendedor,preco_pagar,pagamento,total_venda,data_entrega,data_inicio,hora,lista_veicomprado):
          self.__id=id
          self.__id_vendedor=id_vendedor
          self.__preco_pagar=preco_pagar
          self.__pagamento=pagamento
          self.__total_venda=total_venda
          self.__data_entrega=data_entrega
          self.__data_inicio=data_inicio
          self.__hora=hora
          self.__lista_veicomprado=lista_veicomprado

     def getId(self):
          return self.__id
     def setId(self,id):
          self.__id=id
    
     def getIdvende(self):
          return self.__id_vendedor
     def setIdvende(self,id_vendedor):
          self.__id_vendedor=id_vendedor
    
     def getPrecopagar(self):
          return self.__preco_pagar
     def setPrecopagar(self,preco_pagar):
          self.__preco_pagar=preco_pagar
    
     def getPagamento(self):
          return self.__pagamento
     def setPagamento(self,pagamento):
          self.__pagamento=pagamento
    
     def getTotalvenda(self):
          return self.__total_venda
     def setTotalvenda(self,total_venda):
          self.__total_venda=total_venda

     def getDataentrega(self):
          return self.__data_entrega
     def setDataentrega(self,data_entrega):
          self.__data_entrega=data_entrega
        
     def getDatainicio(self):
          return self.__data_inicio
     def setDatainicio(self,data_inicio):
          self.__data_inicio=data_inicio

     def getHora(self):
          return self.__hora
     def setHora(self,hora):
          self.__hora=hora
    
     def getListacomprado(self):
          return self.__lista_veicomprado
     def setListacomprado(self,lista_veicomprado):
           self.__lista_veicomprado=lista_veicomprado
          
          
