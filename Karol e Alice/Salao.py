from Geral1 import Geral1
class Salao(Geral1):
    def __init__(self, id, id_vendedor, preco_pagar, pagamento, total_venda, data_entrega, data_inicio, hora, lista_veicomprado,nome_cliente,cpf_cliente,venda_concluida,):
        super().__init__(id, id_vendedor, preco_pagar, pagamento, total_venda, data_entrega, data_inicio, hora, lista_veicomprado)
        self.__nome_cliente=nome_cliente
        self.__cpf_cliente=cpf_cliente
        self.__venda_concluida=venda_concluida

    def getNomecliente(self):
        return self.__nome_cliente
    def setNomeclientesel(self,nome_cliente):
        self.__nome_cliente=nome_cliente
    
    def getCpfcliente(self):
        return self.__cpf_cliente
    def setCpfcliente(self,cpf_cliente):
        self.__cpf_cliente=cpf_cliente

    def getVendacon(self):
        return self.__venda_concluida
    def setVendacon(self,venda_concluida):
        self.__venda_concluida=venda_concluida
        

