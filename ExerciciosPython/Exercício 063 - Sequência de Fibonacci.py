'''
Exercício 063
"Sequência de Fibonacci"

Algoritmo para ler um número N do usuário e
mostrar os N primeiros termos da Sequência de
Fibonacci.

1, 1, 2, 3, 5, 8, 13, 21, ...
'''

green = '\033[32m'
purple = '\033[36m'
end = '\033[m'

name = 'GERADOR DE SEQUÊNCIA DE FIBONACCI'
print(15*f'{purple}==={end}' + f'\n{green}{name:^45}{end}\n' + 15*f'{purple}==={end}')

quantity = int(input('Quantos termos gostaria de imprimir? '))
if quantity == 1:
    print(f'\nSequência de Fibonacci com {quantity} termo: ', end='')
else:
    print(f'\nSequência de Fibonacci com {quantity} termos: ', end='')

termo_ant = 0
termo = 1
termo_novo = 0
posicao = 1
while posicao <= quantity:
    if posicao == quantity:
        print(f'{termo}', end='')
    else:
        print(f'{termo}', end=', ')
    termo_novo = termo_ant + termo
    termo_ant = termo
    termo = termo_novo
    posicao += 1

print('\n', end='')