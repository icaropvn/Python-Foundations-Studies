'''
Exercício 050
"Soma dos Pares"

Algoritmo para ler 6 números inteiros e
mostrar a soma apenas se o valor digitado for par.
Caso seja ímpar, descartar.
'''

red = '\033[31m'
ita_green = '\033[3;32m'
end = '\033[m'

soma = 0

for i in range(1, 7):
    num = int(input(f'Insira o valor {i}: '))
    if num % 2 == 0:
        soma += num

if soma == 0:
    print(f'\n{red}Nenhum valor par foi encontrado.{end}')
else:
    print(f'\nO valor da soma dos pares é: {ita_green}{soma}{end}')
