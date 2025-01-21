'''
Atividade 07:
Verificação de Caracteres em uma String:
Crie um programa que peça ao usuário uma frase e um caractere.
Use o operador de associação in para verificar se o caractere está
presente na frase.
'''
frase = input('Digite uma frase: ')
caracter = input('Digite o caracter que deseja procurar: ')

resultado =  caracter in frase
print(resultado)


