salario = float(input('QUAL É O SALARIO DO FUNCIONARIO: '))
if salario <= 1250:
    novo = salario + ( salario *15 / 100)
else:
    novo = salario + (salario * 10 / 100)

print(f"PARA QUEM GANHAVA {salario:.2f} PASSA A GANHAR {novo:.2f}")

