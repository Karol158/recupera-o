from Salao import Salao

salao1=Salao(1,2,600.000,"pix",50.0000,"25/12/2024","08/11/24","15:30hrs",["moto","carro"],"José Marcos","40028922","True")
salao2=Salao(2,4,700.000,"em espécie",100.0000,"30/12/2024","08/11/24","16:30hrs",["lancha","carro"],"Marcos","81812222","True")

print("Identificador"+ str (salao1. getId()))
print("Identificador do vendedor:"+ str (salao1.getIdvende()))
print("Preço a pagar:"+str (salao1.getPrecopagar()))
print("Forma de pagamento"+salao1.getPagamento())
print("Total da venda:"+ str (salao1.getTotalvenda()))
print("Data de entrega:"+salao1.getDataentrega())
print("Data de inicio da compra:"+salao1.getDatainicio())
print("Hora da compra:"+salao1.getHora())
print("Veículos comprados:"+str (salao1.getListacomprado()))
print("Nome do cliente:"+salao1.getNomecliente())
print("CPF do cliente"+salao1.getCpfcliente())
print("Confirmamento da venda:"+salao1.getVendacon())
print("")
print("Identificador:" +str (salao2.getId()))
print("Identificador do vendedor: " + str(salao2.getIdvende()))
print("Preço a pagar:" +str (salao2.getPrecopagar()))
print("Forma de pagamento:"+salao2.getPagamento())
print("Total da venda:"+str (salao2.getTotalvenda()))
print("Data de entrega:"+salao2.getDataentrega())
print("Data de inicio da compra:"+salao2.getDatainicio())
print("Hora da compra:"+salao2.getHora())
print("Veículos comprados:"+ str (salao2.getListacomprado()))
print("Nome do cliente:"+salao2.getNomecliente())
print("CPF do cliente:"+salao2.getCpfcliente())
print("Confirmamento da venda:"+salao2.getVendacon())




