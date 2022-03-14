area = float(input("Entre com a area a ser pintada em metros quadrados: "))

litros = area/3
latas = litros//18

if latas == 0:
    print("É necessário 1 lata de tinta.")

else:
    print("É necessário", latas, "de tinta.")