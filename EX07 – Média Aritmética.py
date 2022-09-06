print('1. Desenvolva um programa que leia as duas notas de um aluno, calcule e mostre a sua média.\n')

nota1 = float(input('DIGITE A PRIMEIRA NOTA :'))
nota2 = float(input('DIGITE A SEGUNDA NOTA:'))

# TEM QUE USAR A ORDEM DE PRESEDENCIA SE NAO VAI DAR ERRO NO CALCULO
media = (nota1 + nota2) / 2
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')
print(f'A MEDIA DO ALUNO É {media}')
print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>')

if media == 10:
    print('PARABENS !, VOCÊ É UM ALUNO EXEMPLAR.')
else:
    print('VOCÊ PRECISA ESTUDAR MAIS.')