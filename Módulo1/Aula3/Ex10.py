'''
Escreva um programa que use um laço while para somar
números consecutivos começando de 1 e termine quando
a soma atingir ou ultrapassar 50.
'''

contador = 1
soma = 0
while contador >= 1:
    soma += contador
    contador += 1
    if soma >= 50:
        print(soma)
        break