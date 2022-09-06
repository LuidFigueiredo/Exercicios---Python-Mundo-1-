print('1.Crie um programa que leia quanto dinheiro uma pessoa tem na carteira e mostre quantos dólares ela pode comprar.\n')

real = float(input('>>QUANTO DINHEIRO VOCÊ TEM NA CARTEIRA R$:'))

# quanto eu tenho na carteira dividido pela cotação do dolar
dolar = real / 3.27
print(f'>>COM TANTOS {real:.2f} VOCE PODE COMPRAR {dolar:.2f} DOLARES.')