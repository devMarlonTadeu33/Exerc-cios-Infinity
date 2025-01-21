'''
Atividade 13:
Sistema de Login Simples:
Desenvolva um programa que peça ao usuário um nome de usuário
e uma senha e use if para verificar se são iguais a 
"admin" e "1234", respectivamente.
'''

usuario = input('Insira seu usuário: ')
senha = input('Insira sua senha: ')

if usuario == 'admin' and senha == '1234':
    print('Login bem sucedido. Seja bem vindo(a)!')
else: print('Usuário ou senha incorretos!')

