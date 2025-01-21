'''
Atividade 10:
Contar Números Positivos e Negativos:
Peça ao usuário para inserir 10 números. Use um laço for com condicionais para contar quantos
são positivos e quantos são negativos. Pare o loop se o número 0 for inserido, usando break.
'''
positivos = []
negativos = []

for i in range(10):
    numero = float(input('Insira Ex número: '))
    if numero > 0:
        positivos.append(numero)
    elif numero < 0:
        negativos.append(numero)
    else:
        break



