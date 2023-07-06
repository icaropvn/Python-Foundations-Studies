'''
Exercício 059
"Menu de Opções"

Algoritmo para ler 2 números e mostrar um menu na tela:

[1] Somar
[2] Multiplicar
[3] Maior Valor
[4] Digitar Novos Valores
[5] Sair
'''

from time import sleep

italic = '\033[3m'
red = '\033[31m'
ita_yellow = '\033[3;33m'
ita_blue = '\033[3;34m'
end = '\033[m'

num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

answer = 0
while answer != 5:
    answer = int(input((f'{italic}\nO que deseja fazer?{end}\n'
                        '[1] Somar\n'
                        '[2] Multiplicar\n'
                        '[3] Maior Valor\n'
                        '[4] Digitar Novos Valores\n'
                        f'{red}[5] Sair{end}\n'
                        f'R: ')))

    if answer == 1:
        print(f'\n{ita_blue}A soma entre {num1} e {num2} é igual a {num1 + num2}{end}')
    elif answer == 2:
        print(f'\n{ita_blue}O produto de {num1} * {num2} é igual a {num1 * num2}{end}')
    elif answer == 3:
        if num1 > num2:
            maior = num1
        else:
            maior = num2
        print(f'{ita_blue}\nO maior valor é {maior}{end}')
    elif answer == 4:
        num1 = int(input('\nInsira um novo número: '))
        num2 = int(input('Insira outro número: '))
    elif answer != 5:
        print(f'{red}{italic}Opção inválida. Tente novamente.{end}')

    if answer != 5:
        sleep(2)

print(f'\n{ita_yellow}Finalizando...{end}', end='')
sleep(1.5)
print(f'{italic}\nAté a próxima!{end}')
