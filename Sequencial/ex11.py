
try:
    n1 = int(input("Entre com um numero inteiro: "))
    n2 = int(input("Entre com outro numero inteiro: "))
except:
    print("Nao eh um numero inteiro.")
try:
    r1 = float(input("Entre com um numero real: "))
except:
    print("Nao eh um numero real.")


c1 = (2*n1) * (n2/2)
c2 = (3*n1) + r1
c3 = r1**3

print(c1)
print(c2)
print(c3)

