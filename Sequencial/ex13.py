h = float(input("Entre com a altura: "))
sexo = input("Ser for homem, digite h e se for mulher, digite m: ")

if sexo == 'h':
    peso_ideal = (72.7*h) - 58

if sexo == 'm':
    peso_ideal = (62.1*h) - 44.7

else:
    print("Entrada inválida.")

print("O seu peso ideal eh: ", peso_ideal)