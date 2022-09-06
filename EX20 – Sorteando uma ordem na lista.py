from random import shuffle
n1 = str(input('1. PRIMEIRO ALUNO: '))
n2 = str(input('2. SEGUNDO ALUNO: '))
n3 = str(input('3. TERCEIRO ALUNO: '))
n4 = str(input('4. QUARTO ALUNO: '))
lista = [n1, n2,n3,n4]
shuffle(lista)
print('A ORDEM DE APRESENTAÇÃO DO TRABALHO SERÁ')
print(lista)