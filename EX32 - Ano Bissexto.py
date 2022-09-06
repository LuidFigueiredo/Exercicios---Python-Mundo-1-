from datetime import date

ano = int(input('QUE (ANO) VOCE QUER ANALISAR / COLOQUE (0) PARA ANALISAR ANO ATUAL : '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 ==0 :
    print(f'O ANO {ano} É BISSEXTO ')
else:
    print(f'O ANO {ano} NÃO É BISSEXTO')