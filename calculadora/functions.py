# 1. Receber valores do usuário
# 2. Calcular
# 3. Exibir resultado

def receberValor():
    a = input("digite a: ")
    b = input("digite b: ")
    return float(a),float(b)

def soma(a,b):
    return a+b

def sub(a,b):
    return a-b

def mult(a,b):
    return a*b

def div(a,b):
    return a/b

def mostrarResultado(resultado):
    print(resultado)