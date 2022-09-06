

'''cateto_oposto = float(input('1. DIGITE O > CATETO OPOSTO < :'))
cateto_adjacente = float(input('2. DIGITE > CATETO ADJACENTE < :'))
hipotenusa = ( cateto_oposto ** 2 + cateto_adjacente ** 2 ) ** (1/2)
print('\n')
print(f'// A HIPOTENUSA VAI MEDIR // {hipotenusa}.')'''


#RESOLVENDO COMA  BIBLIOTECA ( MATH )
import math

cateto_oposto = float(input('1. DIGITE O > CATETO OPOSTO < :'))
cateto_adjacente = float(input('2. DIGITE > CATETO ADJACENTE < :'))
hipotenusa = math.hypot(cateto_oposto, cateto_adjacente)
print(f'O VALOR DA HIPOTENUSA É {hipotenusa:.2f}')