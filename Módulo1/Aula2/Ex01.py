'''
Atividade 01:
Comparação de Idades:
Peça ao usuário duas idades e use operadores de comparação para
verificar se a primeira idade é maior, menor ou igual à segunda.
'''

idade01 = int(input('Digite a idade da 1ª pessoa: '))
idade02 = int(input('Digite a idade da 2ª pessoa: '))

if idade01 > idade02:
    print('A primeira pessoa é mais velha!')
elif idade01 < idade02:
    print('A segunda pessoa é mais velha!')
else: print('As pessoas tem a mesma idade!')

