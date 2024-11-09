from Geral1 import Geral1
class Pessoafisica(Geral1):
    def __init__(self, id, id_vendedor, preco_pagar, pagamento, total_venda, data_entrega, data_inicio, hora, lista_veicomprado,links,data_reserva,prazo_reserva,nome_cliente,cpf_cliente,venda_concluida):
        super().__init__(id, id_vendedor, preco_pagar, pagamento, total_venda, data_entrega, data_inicio, hora, lista_veicomprado)
        self.__links=links
        self.__data_reserva=data_reserva
        self.__prazo_reserva=prazo_reserva
        self.__nome_cliente=nome_cliente
        self.__cpf_cliente=cpf_cliente
        self.__venda_concluida=venda_concluida
    def getLinks(self):
        return self.__links
    def setLinks(self,links):
        self.__links=links
    
    def getDatareserva(self):
        return self.__data_reserva
    def setDatareserva(self,data_reserva):
        self.__data_reserva=data_reserva
    
    def getPrazoreserva(self):
        return self.__prazo_reserva
    def setPrazoreserva(self,prazo_reserva):
        self.__prazo_reserva=prazo_reserva
    
    def getNomecliente(self):
        return self.__nome_cliente
    def setNomecliente(self,nome_cliente):
        self.__nome_cliente=nome_cliente

    def getCpfcliente(self):
        return self.__cpf_cliente
    def setCpfcliente(self,cpf_cliente):
        self.__cpf_cliente=cpf_cliente

    def getVendacon(self):
        return self.__venda_concluida
    def setVendacon(self,venda_concluida):
        self.__venda_concluida=venda_concluida
        
