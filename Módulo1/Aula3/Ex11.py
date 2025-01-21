'''
Atividade 11:
Entrada Válida:
Crie um programa que solicite ao usuário um número entre 1 e 10.
Continue pedindo até que o usuário forneça um valor válido.
'''
numero = float(input('Digite um número: '))

while numero :
    if numero >= 1 and numero <= 10:
        print('Entrada Válida')
        break
    else:
        numero = float(input('Entrada Inválida. Digite outro número: '))
