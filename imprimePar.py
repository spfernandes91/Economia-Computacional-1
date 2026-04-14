#Descrição:O programa imprime todos numeros pares entre 0 e 20
#Autor:Sérgio Fernandes
#Versão:0.0.1 


#Alocação de memoria
num=[ ]
lista_par=[]
#Entrada de dados
for i in range(21):
    num.append(i)
    
#print(*num)
#processamento de dados
for i in range(21):
    if( num[i]%2 ==0):
        lista_par.append(num[i])
        
print(lista_par)   
