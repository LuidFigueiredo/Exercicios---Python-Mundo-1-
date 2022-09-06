frase = str(input('Digite uma frase: ')).upper()
print('a letra (A) APARECE {} vezes na frase. '.format(frase.count('A')))
print('a letra A apareceu na posição. {} '.format(frase.find('A')+1))
print('a ultima letra A apareceu na posição. {} '.format(frase.rfind('A')+1))
