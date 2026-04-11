#Descrição: Este programa recebe 3 numero do teclado e escreve na tela em ordem decrescente
#Autor: Sérgio Fernandes 
#Data:10/04/26
#Versão:0.0.1

#Alocação de memória
num_1=0.0
num_2=0.0
num_3=0.0
aux=0.0
#Armazenamento dos Dados:
num_1=float(input("Digite o primeiro numero:\n"))
num_2=float(input("Digite o segundo numero:\n"))
num_3=float(input("Digite o primeiro numero:\n"))
#Processamento de dados
#caso 1:
if (num_1 > num_2) and (num_1> num_3):
    if(num_2>num_3):
        print(f"{num_1},{num_2},{num_3}")
    elif(num_3 > num_2):
           print(f"{num_1},{num_3},{num_2}")
#caso2
if(num_2> num_1) and (num_2>num_3):
    if(num_1>num_3):
        print(f"{num_2},{num_1},{num_3}")
    elif(num_3> num_1):
        print(f"{num_2},{num_3},{num_1}")
            
#caso 3 
if(num_3 > num_1) and (num_3> num_2):
    if(num_2> num_1):
        print(f"{num_3},{num_2},{num_1}")
    elif(num_1> num_2):
        print(f"{num_3},{num_1},{num_2}")
