'''
Atividade 06:
Soma de Números Pares:
Escreva um programa que use um laço for para somar
todos os números pares de 1 a 50 e exiba o resultado final.
'''
#ENTRADA
soma = 0
#PROCESSAMENTO
for i in range(1,50 + 1):
    if i % 2 == 0:
        soma = soma + i
#SAÍDA
print(f'A soma dos números pares de 1 a 50 é igual a: {soma}')