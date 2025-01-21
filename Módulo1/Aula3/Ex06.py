'''
Atividade 06:
Soma de Números Positivos:
Escreva um programa que solicite números ao usuário até
que ele digite um número negativo, somando apenas os
números positivos inseridos.
'''


soma = 0
numero = int(input('Digite um número: '))

while numero > 0:
    soma += numero 
    numero = int(input('Digite outro número: '))
print(f'A soma dos números positivos digitados é {soma}.')


    

