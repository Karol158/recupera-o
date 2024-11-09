from Geral1 import Geral1
class Pessoajuridica(Geral1):
    def __init__(self, id, id_vendedor, preco_pagar, pagamento, total_venda, data_entrega, data_inicio, hora, lista_veicomprado,links,data_reserva,prazo_reserva,nome_empresa,cnpj_cliente,nome_respon):
        super().__init__(id, id_vendedor, preco_pagar, pagamento, total_venda, data_entrega, data_inicio, hora, lista_veicomprado)
        self.__links=links
        self.__data_reserva=data_reserva
        self.__prazo_reserva=prazo_reserva
        self.__nome_empresa=nome_empresa
        self.__cnpj_cliente=cnpj_cliente
        self.__nome_respon=nome_respon
    
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

    def getNomeempresa(self):
        return self.__nome_empresa
    def setNomeempresa(self,nome_empresa):
        self.__nome_empresa=nome_empresa
    
    def getCnpjcliente(self):
        return self.__cnpj_cliente
    def setCnpjcliente(self,cnpj_cliente):
        self.__cnpj_cliente=cnpj_cliente
    
    def getNomerespon(self):
        return self.__nome_respon
    def setNomerespon(self,nome_respon):
        self.__nome_respon=nome_respon
        
        
    