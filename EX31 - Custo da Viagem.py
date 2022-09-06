distancia = float(input("QUAL A DISTANCIA DA SUA VIAGEM ? :"))
print(f'\nVOCE ESTAR PRESTES A COMEÇAR UMA VIAGEM DE {distancia} KM...')

if distancia <= 200:
    preco = distancia * 0.50
else:
    preco =distancia * 0.45
print(f'O PREÇO DA SUA VIAGEM SERA DE R$ {preco:.2f}')