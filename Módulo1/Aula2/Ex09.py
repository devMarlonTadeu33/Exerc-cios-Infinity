'''
Atividade 09:
Verificar Par ou Ímpar:
Crie um programa que peça ao usuário um número e use a
estrutura condicional if para verificar se ele é par ou ímpar.
'''

numero = int(input('Digite um número: '))

if numero % 2 == 0:
    print(f'O número {numero} é par!')
else: print(f'O número {numero} é ímpar!')