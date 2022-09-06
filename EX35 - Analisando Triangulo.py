print('=================================')
print('ANALISANDO TRIANGULO')
print('=================================\n')

r1 = float(input('PRIMEIRO VALOR: '))
r2 = float(input('SEGUNDO VALOR: '))
r3 = float(input('TERCEIRO VALOR: '))

if r1 < r2 + r3 and r2 < r1+ r3 and r3 < r1 + r2:
    print('OS VALORES ACIMA FORMA UM TRIANGULO (Y)')
else:
    print('NÃO PODEM FORMA UM TRIANGULO')