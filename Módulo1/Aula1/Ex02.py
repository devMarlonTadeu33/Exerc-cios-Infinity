'''
ATIVIDADE PRÁTICA

Atividade 02: Crie um programa que peça ao usuário para digitar:
1.Seu nome;
2.Sua idade;
3.Sua altura;
4.Em seguida, imprima esses valores e seus respectivos tipos.
Objetivo: Praticar a declaração e uso de variáveis de diferentes tipos,
além de aprender a verificar e imprimir seus tipos em Python.

Observação: Conhecer e utilizar diferentes tipos de variáveis
é fundamental para manipular dados de maneira eficaz.

'''

nome = input("Digite seu nome: ")
idade = int(input("Digite sua idade: "))
altura = float(input("Digite sua altura: "))

print(f"Meu nome é {nome}")
print(type(nome))
print(f"Minha idade é {idade} anos")
print(type(idade))
print(f"Minha altura é {altura}")
print(type(altura))
