'''
Atividade 14:
Verificar Status de Taxa de Desconto:
Crie um programa que peça ao usuário o preço original de um produto e
a quantidade comprada. Use if para verificar se a quantidade é maior que
10 para aplicar um desconto de 10% sobre o total.
'''

preco = float(input('Digite o preço do produto: '))
quantidade = float(input('Digite a quantidade comprada: '))

novopreco = 0 

if quantidade > 10:
    novopreco = (preco * quantidade) 
    novopreco = novopreco / 100 * 90
    print(f'O novo preço do produto com desconto é R${novopreco:.2f}.')
else: print(f'O preço total é {quantidade * preco}')

