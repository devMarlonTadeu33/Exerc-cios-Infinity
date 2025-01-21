'''
Atividade 11:
Verificar Par ou Ímpar e Positivo ou Negativo:
Escreva um programa que peça um número e use if para verificar
se ele é par ou ímpar e também se é positivo ou negativo.
'''

numero = float(input('Digite um número: '))

if numero > 0 and numero % 2 ==0:
    print("O número é positivo e par!")
elif numero < 0 and numero % 2 == 0:
    print('O número é negativo é par!')
elif numero > 0 and numero % 2 != 0:
    print('O número é positivo e ímpar!')
elif numero < 0 and numero % 2 != 0:
    print('O número é negativo e ímpar!')
else: print('O número 0 é considerado neutro, pois não é positivo nem negativo. E é um número par!')

