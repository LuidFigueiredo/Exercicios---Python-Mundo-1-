print('Faça um algoritmo que leia o preço de um produto e mostre seu novo preço, com 5% de desconto.\n')

preco = float(input('QUAL É O PREÇO DO PRODUTO R$: '))
novopreco = preco- (preco * 5/100)
print(f'O PRODUTO QUE CUSTAVA {preco} NA PROMOÇÃO FICOU POR {novopreco}. ')