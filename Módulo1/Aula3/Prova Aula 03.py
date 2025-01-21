'''
Você está criando um programa em Python para simular um jogo simples de adivinhação. 
O programa deve ter um número fixo, por exemplo, 7, que o jogador deve adivinhar. 
O jogador terá até 3 tentativas para acertar o número.

Implemente o jogo utilizando um loop while para permitir que o jogador faça múltiplas 
tentativas até acertar ou atingir o limite de tentativas.
Utilize a estrutura else para exibir uma mensagem de encorajamento caso o jogador acerte
e uma mensagem de consolo caso as 3 tentativas se esgotem sem sucesso.
'''

numero =float(4)
print('NÚMERO MÁGICO')
print('Advinhe o número correto (0 a 10)')
print('Você possui 3 tentativas.')
tentativa = float(input('Advinhe o número que estou pensando: '))
chances = 0


while tentativa != numero:
    chances += 1
    if chances == 3:
        print('Suas chances acabaram!')
        break
    print('Você errou! Tente novamente.')
    tentativa = float(input('Advinhe o número que estou pensando: '))
if tentativa == numero:
        print('Parabéns. Você acertou!!')
        