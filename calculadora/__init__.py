from functions import *

def funcao1():
    return 1
funcao1()

def funcao2():
    return 10-8
funcao2()

def soma(a,b,c):
    resultado = a+b+c
    return resultado
soma(1,2,3)

def maior(x,y):
    return x>y
maior(1,2) # -> False

def menorOuIgual(a,b):
    return a<=b
menorOuIgual(1,1) # -> True

def diferente(a,b):
    return a!=b
diferente(1,"1") # -> True (Tipagem Forte)
# 1+"1" # -> Erro
# 1+1.0 # -> 2.0
# print(1+1j + 1.0) # -> 2+1j

def igual(a,b):
    return a==b
igual(1,1.0) # -> True (int e float eles compatíveis entre si)
# print(igual(0,False))
# print(igual(1,True))

def igualEDiferente(a,b):
    return a==b and a!=b
igualEDiferente(1,2) # -> False

def maiorEMenor(a,b):
    return a>b and a<b
maiorEMenor(1,2) # -> False

def maiorOuMenor(a,b):
    return a>b or a<b
maiorOuMenor(1,2) # -> True
maiorOuMenor(2,1) # -> True
maiorOuMenor(1,1) # -> False
maiorOuMenor(2,2) # -> False