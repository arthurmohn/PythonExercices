valor = float(input("Quanto voce ganha por hora?: "))
horas = float(input("Quantas horas voce trabalha por mes?: "))

bruto = valor*horas
ir = bruto*0.11
inss = bruto*0.08
sind = bruto*0.05
liquido = bruto - ir - inss - sind
 
print("+ Salario bruto = R$%.2f" %bruto)
print("- IR (11%) = R$%.2f" %ir)
print("- INSS (8%) = R$%.2f" %inss)
print("- Sindicato (5%) = R$%.2f" %sind)
print("= Salario liquido = R$%.2f" %liquido)