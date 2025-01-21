'''
Objetivo: Criar um Programa que Peça as 4 Notas
Bimestrais e Mostre a Média

Instruções:

1 - Solicitar as Notas do Usuário:
Use a função input() para pedir ao usuário que insira
cada uma das quatro notas bimestrais. Converta a
entrada do usuário de string para um número (float)
para permitir cálculos.

2 - Calcular a Média das Notas:
Some as quatro notas e divida o resultado
por quatro para obter a média.

3 - Mostrar a Média Calculada para o Usuário:
Use a função print() para exibir a média das notas
calculada.
'''
notas = []
for i in range(1,4):
    nota = float(input(f"Insira a {i}ª nota:"))
    notas.append(nota)
print(notas)

media = sum(notas)/len(notas)
print(f"A média das notas é = {media}!")
