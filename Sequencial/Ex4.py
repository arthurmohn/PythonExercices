import random as rd

lista = []

for i in range(3):
    lista.append(rd.randint(0,100))

print("lista = " + str(lista))

lista.sort()

print("lista ordenada = " + str(lista))




