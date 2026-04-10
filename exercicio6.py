
# Online Python - IDE, Editor, Compiler, Interpreter
#Descrição: Esse programa calcula o n-ésimo termo de uma pass
#Autor: Sérgio Fernandes
#Data: 10/04/2026
#Versão:0.0.1

#Alocação de memória:
prim_term=0.0
termos=0.0
razao=0.0
n_esimo=0.0
# Armazenamento de dados
prim_term=float(input("Digite o primeiro termo:\n"))
termos=float(input("Digite o a quantidade de termos:\n"))
razao=float(input("Digite a razão a ser utilizada:"))
#Processamento de dados
n_esimo=prim_term + (termos-1)*razao
#Saida de dados
print(f"O soma dos {termos} termos é:{n_esimo}")


