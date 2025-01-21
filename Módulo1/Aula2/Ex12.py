'''
Atividade 12:
Verificar Classificação de IMC:
Crie um programa que calcule o Índice de Massa Corporal (IMC)
e use if para classificar o resultado em 
"Abaixo do peso","Peso normal","Sobrepeso" e "Obesidade".

enor que 18,5	Magreza
18,5 a 24,9	Normal
25 a 29,9	Sobrepeso
30 a 34,9	Obesidade grau I
35 a 39,9	Obesidade grau II
Maior que 40	Obesidade grau III

'''

print('Calculadora de IMC!(Indicé de Massa Corporal)')
print()
print()

peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
print()
print()
print('Caluculando seu IMC...')
imc = peso / (altura * altura)
print()
print()
if imc < 18.5:
    print(f'Seu IMC é de {imc:.2f}. O seu estado atual é de magreza!')
elif imc > 18.5 and imc < 25:
    print(f'Seu IMC é de {imc:.2f}. O seu estado atual é de peso normal!')
elif imc > 24.9 and imc < 30:
    print(f'Seu IMC é de {imc:.2f}. O seu estado atual é de sobrepeso!')
elif imc > 29.9 and imc < 35:
    print(f'Seu IMC é de {imc:.2f}. O seu estado atual é de Obesidade grau I!')
elif imc > 34.9 and imc < 40:
    print(f'Seu IMC é de {imc:.2f}. O seu estado atual é de obesidade grau II!')
else: print(f'Seu IMC é de {imc:.2f}. O seu estado atual é de obesidade grau III!')

