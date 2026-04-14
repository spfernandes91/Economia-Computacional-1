#Descrição: Este programa recebe dois numeros e calcula a exponecial
#Autor:Sérgio Fernandes
#Versão:0.0.1 

#Alocação de memoria
a=0
b=0
result=0
aux=0
#Entrada de Dados
a=int(input("Entre com o valor base:"))
b=int(input("Entre com a exponecial:"))
#Processamento de dados
result=a
for i in range(b-1):
    aux=a
    result= result*aux

print(f'{result}')
