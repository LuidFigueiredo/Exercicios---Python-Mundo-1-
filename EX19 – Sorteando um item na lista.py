import random
n1 = str(input('PRIMEIRO ALUNO : '))
n2 = str(input('SEGUNDO ALUNO: '))
n3 = str(input('TERCEIRO ALUNO: '))
n4 = str(input('QUARTO ALUNO:'))
n5 = str(input('QUINTO ALUNO: '))
n6 = str(input('SEXTO ALUNO :'))
n7 = str(input('SÉTIMO ALUNO: '))
lista = [n1, n2, n3, n4, n5, n6, n7]
escolhido = random.choice(lista)
print(f'O ALUNO ESCOLHIDO PARA LIMPA O QUADRO FOI {escolhido}')
