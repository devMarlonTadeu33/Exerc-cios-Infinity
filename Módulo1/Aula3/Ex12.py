'''
Atividade 12:
Senha Correta:

Desenvolva um programa que peça ao usuário para digitar uma
senha e continue pedindo até que a senha correta (previamente
definida) seja inserida.
'''
senhaCorreta = '45'

senha = input('Digite sua senha: ')

while senha:
    if senha == senhaCorreta:
        print('Acesso permitido!')
        break
    else: 
        senha = input('Senha Incorreta. Tente novamente: ')
        