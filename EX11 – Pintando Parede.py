print('Faça um programa que leia a largura e a altura de uma parede em metros,\n'
' calcule a sua área e a quantidade de tinta necessária para pintá-la,\n '
 'sabendo que cada litro de tinta pinta uma área de 2 metros quadrados.\n')

print('---------------------------------')
largura = float(input('1. DIGITE A LARGURA DA PAREDE: '))
altura = float(input('2. DIGITE A ALTURA DA PAREDE: '))
area = largura * altura
print('-------------------------------------------\n')

print(f'>> Sua parede tem {largura} e {altura} e sua area e de {area}.\n')
tinta = area / 2
print(f'>> pintar essa area voce precisara de {tinta} litros de tintas.')