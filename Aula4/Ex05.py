'''
Atividade 05:
Contagem de Números Positivos e Negativos:
Escreva um programa que solicite ao usuário 10 números e use um
laço for com uma condicional para contar quantos são positivos e
quantos são negativos.
'''
#ENTRADA
positivos = 0
negativos = 0

#PROCESSAMENTO
for i in range(10):
    numero = int(input('Digite um número: '))
    if numero >= 0: 
        positivos = positivos + 1
    else: negativos = negativos + 1
#SAÍDA 

print(f'Dos números digitados, {positivos} são positivos e {negativos} são negativos.')
