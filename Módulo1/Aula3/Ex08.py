'''
Atividade 08:
Média de Notas:
Desenvolva um programa que solicite as notas dos alunos até
que o usuário digite -1. Calcule e exiba a média das notas
inseridas.
'''

nota = float(input('Insira uma nota: '))
soma = []
while nota != -1:
    soma.append(nota)
    nota = float(input('Insira outra nota: '))
print(f'A média das notas digitadas é {sum(soma) / len(soma)}.')

