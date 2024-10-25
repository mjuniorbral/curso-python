import math
def f(x):
    return math.sin(x*math.pi/4)

def integral(funcao,x0,x1,n):
    dx = (x1-x0)/n
    somaArea = 0
    for passo in range(n):
        x = x0 + passo*dx
        prox_x = x0 + (passo+1)*dx
        somaArea += dx*(funcao(x)+funcao(prox_x))/2
    return somaArea