'''
Atividade 08:
Verificação de Palavras em uma Frase:
Peça ao usuário para inserir uma frase e uma palavra.
Use in para verificar se a palavra está na frase.
'''

frase = input('Digite uma frase: ')
palavra = input('Digite a palavra que deseja procurar: ')

resultado = palavra in frase 
print(resultado)

