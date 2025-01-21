'''
Atividade 09:
Verificar Números Pares e Impares com Interrupção:
Crie um programa que use um laço for para contar de 1 a 20. Use condicionais para
identificar números pares e ímpares. Pare o loop ao encontrar o número 15, usando break.
'''

pares = []
impares = []

for i in range(20):
    if i % 2 == 0:
        pares.append(i)
    else:
        impares.append(i)
    if i == 15:
        break

print(pares,impares)
