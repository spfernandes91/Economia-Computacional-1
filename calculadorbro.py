
#Descrição: O programa lê 5 numeros do usuário e imprime na tela todos os numeros ao quadrado
#Autor:Sérgio Fernandes
#Versão:0.0.1 
#Alocação de memoria
num=[]
dobro=[]
aux=0.0
#Entrada de dados
#utilizando a funão for aqui
for i in range (5):
    aux=float(input("Entre com os 5 numeros:"))
    num.append(aux)
    
#processamento de dados
for i in range(5):
    dobro.append(num[i]**2)
  
#Saida de dados    
print(*dobro)
