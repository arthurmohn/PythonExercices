print("Seguindo o modelo: ax^2 + bx + c")

a = float(input("Entre com o valor de a: "))
b = float(input("Entre com o valor de b: "))
c = float(input("Entre com o valor de c: "))

def raizes(a, b, c):
    delta =  b**2 - 4*a*c

    raiz1 = (- b + delta**(1/2))/2*a

    raiz2 = (- b - delta**(1/2))/2*a

    return raiz1, raiz2

raiz1, raiz2 = raizes(a,b,c)

print("raiz 1 = ", raiz1, "\nraiz 2 = ", raiz2)
