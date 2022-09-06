print("Escreva um programa que pergunte a quantidade de Km percorridos por um carro\nalugado e a quantidade de dias pelos quais ele foi alugado. \nCalcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.\n")

dias = float(input('> QUANTOS DIAS O CARRO FICOU ALUGADO: '))
km = int(input('> QUANTOS KM RODADOS:'))
valorapagar = (dias * 60) + ( km * 0.15)
print("O TOTAL A PAGAR É DE R${:.2f}".format(valorapagar))