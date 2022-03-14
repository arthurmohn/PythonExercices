altura = float(input("Entre com a altura: "))

def peso_ideal(altura):
    return (72.7*altura) - 58
    
print("O seu peso ideal eh: ", peso_ideal(altura))