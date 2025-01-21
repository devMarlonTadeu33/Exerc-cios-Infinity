'''
Atividade 12:
Soma de Números com Desconto:
Peça ao usuário para inserir 5 preços de produtos. Use um laço for para
calcular o total. Aplique um desconto de 10% se o total ultrapassar 100 e
interrompa o loop com break.
'''
total = 0
for i in range(5):
    preço = float(input(f'Insira o preço do {i + 1} produto:'))
    total = total + preço
    if total > 100:
        total -= (total / 100 * 10)
        break
print(total)

