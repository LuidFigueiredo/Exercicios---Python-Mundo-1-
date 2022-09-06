print('1. Escreva um programa que converta uma temperatura digitando em graus Celsius e converta para graus Fahrenheit.\n')

#Fórmula de conversão	(0 °C × 9/5) + 32 = 32 °F

celsius = float(input('INFORME A TEMPRERATURA EM CELSIUS: '))
fahrenheit = ((9*celsius)/5)+32
#primeiro a mutiplicacao depois a divisão esse resultado somado com 32

print(f'>>A TEMPRERATURA EM {celsius} C, CORRESPONDE {fahrenheit} F<<')