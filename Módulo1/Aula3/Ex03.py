'''
Atividade 03:
Tabuada de um Número:
Faça um programa que solicite um número ao usuário e use
um laço while para exibir a tabuada desse número (de 1 a 10).
'''
numero = float(input('Digite um número para ver a tabuada: '))
multiplicador = 0

while multiplicador <= 10:
    print(f'{numero} x {multiplicador} = {numero * multiplicador}.')
    multiplicador += 1

