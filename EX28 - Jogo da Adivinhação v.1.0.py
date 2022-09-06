from random import randint
from time import sleep

computador = randint(0,5) # faz o computador sortear um numero
print('-=-' * 20)
print('Vou pensar entre um número entre 0 e 5. Tente Advinhar')
print('-=-' * 20)
jogador = int(input('EM QUE NUMERO ESTOU PENSANDO ? : ')) # jogador tentar advinhar
print('PROCESSANDO.....')
sleep(2)

if jogador == computador:
    print('PARABÉNS ! Voce consegiu me vencer...')
else:
    print('GANHEI " eu pensei no número {} e não no {}'. format(computador, jogador))
