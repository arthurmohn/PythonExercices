from cmath import pi
from re import A


r = float(input("Entre com o raio do circulo: "))

def area(r):
    a = pi*(r**2)
    return a

print("O raio do circulo eh: ", area(r))