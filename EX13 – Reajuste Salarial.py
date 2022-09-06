print("1. Faça um algoritmo que leia o salário de um funcionário e mostre seu novo salário, com 15% de aumento.\n")

salario = float(input('QUAL É O SALÁRIO DO FUNCIONARIO R$ :'))
novosalario = salario+(salario * 15/100)
print('UM FUNCIONARIO QUE GANAHAVA R$ {:.2f}, COM 15% DE AUMENTO , PASSA A RECEBER R$ {:.2f}'.format(salario, novosalario))