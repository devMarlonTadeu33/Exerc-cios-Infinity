'''
Atividade 05:
Contagem até o Número Inserido:
Crie um programa que solicite um número ao usuário e use
um laço while para contar de 1 até o número inserido,
exibindo apenas os números ímpares.
'''

numero = int(input('Digite um número: '))
contador = 0

print(f'Os números ímpares entre 0 e {numero} são:')
while contador <= numero:
    
    if contador % 2 != 0:
        print(contador)
    contador += 1
    
