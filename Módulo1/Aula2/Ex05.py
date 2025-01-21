'''
Atividade 05:
Desconto em Preço:
Peça ao usuário para inserir o preço de um produto e, em seguida,
use o operador de atribuição -= para aplicar um desconto de 5%.
'''

preco = float(input('Insira o preço do produto: '))
preco -= (preco/100*5)
print(f'O novo preço do produto com desconto é R$ {preco}.')


