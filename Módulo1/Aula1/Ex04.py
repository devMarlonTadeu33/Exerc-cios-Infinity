'''
Objetivo: Faça um programa que pergunte quanto você ganha por hora e o número de horas
trabalhadas no mês, calcule o salário total e exiba o resultado (Considere que você trabalha
20 dias no mês).

Instruções:
1 - Solicitar o Salário Mensal:
Use a função input() para pedir ao usuário que insira quanto
ele ganha por mês. Converta a entrada do usuário de string
para um número (float) para permitir cálculos.

'''
salario = float(input("Digite o valor do seu salário mensal:"))

'''
2 - Solicitar o Número de Horas Trabalhadas na Semana:
Use a função input() para pedir ao usuário que insira o número
de horas trabalhadas na semana. Converta a entrada do
usuário de string para um número (float) para permitir
cálculos.

'''

horas = float(input("Insira quantas horas você trabalhou na semana:"))

'''
3 - Calcular o Total de Horas Trabalhadas no Mês:
Multiplique o número de horas trabalhadas na semana por 4
para obter o total de horas trabalhadas no mês.

'''

horasMes = horas * 4 

'''
4 - Calcular o Salário por Hora:
Divida o salário mensal pelo total de horas
trabalhadas no mês para obter o salário por
hora.

'''

salarioPorHora = salario / horasMes
'''

5 - Mostrar o Salário por Hora Calculado
para o Usuário:
Use a função print() para exibir o salário por
hora calculado.

'''

print(f'O salário por hora é igual a R$ {salarioPorHora}.')