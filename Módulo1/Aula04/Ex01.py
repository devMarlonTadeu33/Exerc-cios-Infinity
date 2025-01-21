"""
Atividade 01:
Tabuada de um Número:
Faça um programa que solicite um número ao usuário e use
um laço for para exibir a tabuada desse número (de 1 a 10).
"""

#ENTRADA

numero = int(input("Insira um número: "))
tabuada = []
#PROCESSAMENTO

for i in range(1,10 + 1):
    tabuada.append(numero*i)

#SAÍDA
print(f'A tabuada do número {numero} é: ')
for i in tabuada:
    print(i)
