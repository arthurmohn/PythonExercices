peso = float(input("Entre com o peso obtido: "))

if peso <50:
    print("Quantidade abaixo do limite.")

else:
    excesso = peso - 50
    multa = excesso*4

    print("Excesso = %.2f kg" %excesso)
    print("Multa = R$%.2f" %multa)

