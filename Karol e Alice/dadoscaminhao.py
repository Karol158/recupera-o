from Caminhao import Caminhao
 
caminhao1=Caminhao("Scania","Carreta","KKRHJHJH55454",2024,"Prata",500.000,4, "1.200 km",)
caminhao2=Caminhao("Volkswagen","Carreta","YYEEWWWW5656",2011,"Vermelha",200.000,4,"1.200 km")

print("Marca:"+caminhao1.getMarca())
print("Modelo:"+caminhao1.getModelo())
print("Numero de chassi:"+caminhao1.getNumerocha())
print(f"Cor:{caminhao1.getCor()}/Ano de fabricação:  {(caminhao1.getAno())}")
print("Preço:"+ str (caminhao1.getPreco()))
print("Quantidade de eixos:"+str (caminhao1.getQtdeixos()))
print("Quilometragem/Horas de uso:"+caminhao1.getQuilometragem())
print("")
print("Marca:"+caminhao2.getMarca())
print("Modelo:"+caminhao2.getModelo())
print("Numero de chassi:"+caminhao2.getNumerocha())
print(f"{caminhao2.getCor()} Ano de fabricação:{caminhao2.getAno()}")
print("Preç:o"+str (caminhao2.getPreco()))
print("Quantidade de eixos:"+ str (caminhao2.getQtdeixos()))
print("Quilometragem/Hora de uso:"+caminhao2.getQuilometragem())


