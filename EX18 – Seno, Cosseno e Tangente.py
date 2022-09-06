import math
angulo = float(input('DIGITE UM ANGULO QUE VOCE DESEJA: '))
seno = math.sin(math.radians(angulo)) #pega o angulo, converte pra radiano e calcular o seno dele
print(f'>> O ANGULO DE {angulo} TEM O SENO DE {seno:.2f}')
coseno = math.sin(math.cos(angulo))
print(f'>> O ANGULO DE {angulo} TEM O COSENO DE {coseno:.2f}')
tangente = math.tan(math.tan(angulo))
print(f'>> O ANGULO DE {angulo} TEM A TANGENTE DE {tangente:.2f}')