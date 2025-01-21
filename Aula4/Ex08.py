'''
Cálculo de Média de Notas:
Escreva um programa que solicite 5 notas de alunos. Use um laço for
para somar as notas e uma condicional para exibir a média e a
classificação ("Aprovado" para média >= 6, "Reprovado" para média < 6).
'''
notas = 0
for i in range(5):
    nota = float(input(f'Digite a {i + 1} nota: '))
    notas += nota

media = notas / 5

if media >= 6:
    print(f'Aluno aprovado! A média foi {media}')
else: print(f'Aluno reprovado! A média foi {media}')