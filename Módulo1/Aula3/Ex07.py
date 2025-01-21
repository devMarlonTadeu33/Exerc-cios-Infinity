'''
Atividade 07:
Tabuada com Condicional:
Faça um programa que solicite um número ao usuário e use
um laço while para exibir a tabuada desse número (de 1 a 10),
mas apenas para os resultados que forem múltiplos de 3.
'''

numero = int(input('Insira um número: '))
resultado = 0
contador = 0 
print('Os números presentes na tabuada do número digitado multiplos de 3 são:')
while contador < 10:
    if numero * contador % 3 == 0:
        resultado = numero * contador
        print(resultado)
    contador += 1