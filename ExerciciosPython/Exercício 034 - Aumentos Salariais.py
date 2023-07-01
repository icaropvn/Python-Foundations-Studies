'''
Exercício 034
"Aumentos Salariais"

Algoritmo para ler um salário de um funcionário e calcular seu aumento:
- Se salário <= 1250 -- +15%
- Se salário > 1250 -- +10%
'''

blue = '\033[34m'
green = '\033[32m'
end = '\033[m'

salario = float(input('Insira o salário do funcionário: R$'))

if salario > 1250:
    novo = salario * 1.10
    print(f'\nO novo salário é de {blue}R${novo:,.2f}{end}\nCom um aumento de {green}R${novo - salario:.2f}{end}')
else:
    novo = salario * 1.15
    print(f'\nO novo salário é de {blue}R${novo:,.2f}{end}\nCom um aumento de {green}R${novo - salario:.2f}{end}')
