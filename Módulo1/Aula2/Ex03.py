'''
Atividade 03:
Verificação de Maioridade e Habilitação:
Crie um programa que peça a idade do usuário e se ele possui habilitação
(sim ou não). Use operadores lógicos para verificar se ele é maior de idade
(>= 18) e possui habilitação.
'''
idade = int(input('Insira sua idade: '))

if idade < 18:
    print('Você prcisa ter ao menos 18 anos para tirar habilitação!')
elif idade >= 18:
    possuiHabilitacao = input('Você possui habilitação? (Responda com Sim/Não: )')
    if possuiHabilitacao == 'Sim':
      print('Você pode dirigir!')
    elif possuiHabilitacao == 'Não':
      print('Você não pode dirigir.')


