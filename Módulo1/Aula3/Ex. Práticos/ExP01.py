'''
1 - Soma de Números Pares:
Crie um programa que use um laço while para somar
todos os números pares de 1 a 100 e exiba o resultado.
'''
soma = 0
contador = 0

while contador < 100:
    contador += 1
    if contador % 2 == 0:
        soma += contador

print(soma)
