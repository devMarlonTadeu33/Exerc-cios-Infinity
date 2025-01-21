'''
Atividade 07:
Contagem de Vogais em uma Palavra:
Crie um programa que solicite uma palavra ao usuário e use um laço for com
uma condicional para contar quantas vogais (a, e, i, o, u) a palavra contém.
'''
palavra = input('Insira uma palavra: ')
vogais = ['a', 'e','i','o','u','A','E','I','O','U']
contador = 0

for i in palavra:
    if i in vogais:
        contador += 1

print(f'A palavra tem {contador} vogais.')