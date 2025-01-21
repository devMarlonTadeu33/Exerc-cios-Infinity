'''
Atividade 04:
Verificação de Notas Aprovadas:
Escreva um programa que peça duas notas de um aluno. Use operadores
lógicos para verificar se as duas notas são maiores ou iguais a 6.
'''

nota01 = float(input('Digite a 1ª nota: '))
nota02 = float(input('Digite a 2ª nota: '))

if nota01 >= 6 and nota02 >= 6:
    print('Párabens, você foi aprovado(a)!!')
elif nota01 >= 6 and nota02 <6:
    print('Que pena, você foi reprovado(a) pois a sua segunda nota foi abaixo da média!')
elif nota01 <= 6 and nota02 >= 6:
    print('Que pena, você foi reprovado(a) pois a sua primeira nota foi abaixo da média!')
else: print('Que pena, nenhuma das suas notas alcançou a média. Você foi reprovado(a)!')
