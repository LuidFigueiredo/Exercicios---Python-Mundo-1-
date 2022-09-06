a = int(input('PRIMEIRO VALOR: '))
b = int(input("SEGUNDO VALOR: "))
c = int(input("TERCEIRO VALOR: "))

#VERIFICANDO QUEM É O MENOR
menor = a
if b < a and b < c:
    menor = b
if c < a and c < b :
    menor = c

#VERIFICANDO QUEM É O MENOR
maior = a
if b > a and b > c:
    maior = b
if c > a and c > b :
    maior = c
print('\n=====================================')
print(f'O MENOR VALOR É {menor}')
print(f'O MAIOR VALOR É {maior}')
print('=====================================')