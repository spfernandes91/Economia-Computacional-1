#Definição: Este programa recebe o grau e os coeficientes e calcula o polinomio de um valor pré determinado
#Autor: Sérgio Fernandes
#Data: 13/10/26
#Versão:0.0.1
'''
a.append(5)
a.append(6)
print(*a)
'''

#Alocação de memória
n= 0
i=0 
a = [] 
aux=0
x=2 
result=0


#Entrada de dados
n=int(input("Digite o grau do polinômio:"))
while(i<=n ):
    aux=int(input("Digite os n coeficientes:"))
    a.append(aux)
    i=i +1
 
#print(* a)


#Procesamento de dados
i=0 
while(i<=n):
    result =result + a[i]* (x **n)
    #print(f'{a[i]}')
   # print(f'{n}')
    i=i+1
    n= n-1
    

result= result + a[i]

print(f'{result}')                       
    
    
    


