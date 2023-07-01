'''
Exercício 043
"Cálculo de IMC"

Algoritmo para ler o peso e a altura de uma pessoa,
calcular seu IMC e mostrar seu status:

< 18.5 - Abaixo do Peso
< 25 - Peso Ideal
< 30 - Sobrepeso
< 40 - Obesidade
> 40 - Obesidade Mórbida

IMC = peso / (altura²)
'''

green = '\033[3;32m'
yellow = '\033[3;33m'
red = '\033[3;31m'
italic = '\033[3m'
end = '\033[m'

peso = float(input('Insira o peso (Kg): '))
altura = float(input('Insira a altura (m): '))

imc = peso / altura**2

if imc < 18.5:
    status = f'{yellow}Abaixo do Peso{end}'
elif imc < 25:
    status = f'{green}Peso Ideal{end}'
elif imc < 30:
    status = f'{yellow}Sobrepeso{end}'
elif imc <= 40:
    status = f'{red}Obesidade{end}'
else:
    status = f'{red}Obesidade Mórbida{end}'

print(f'Seu IMC é {italic}{imc:.1f}{end}, sua classificação é: {status}')
