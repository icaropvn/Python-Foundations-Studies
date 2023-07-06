'''
Exercício 063
"Sequência de Fibonacci"

Algoritmo para ler um número N do usuário e
mostrar os N primeiros termos da Sequência de
Fibonacci.

1, 1, 2, 3, 5, 8, 13, 21, ...
'''

num = int(input('Insira a quantidade de termos da sequência a serem impressos: '))
print(f'\nSequência de Fibonacci com {num} termo(s): ', end='')

termo_ant = 1
termo = 1
termo_novo = 1
posicao = 0
while posicao != num-1:
    if posicao == num-2:
        print(termo_novo, end='')
    else:
        print(termo_novo, end=', ')
    if posicao == 0 and num != 1:
        print('1', end=', ')
    termo_novo = termo_ant + termo
    termo_ant = termo
    termo = termo_novo
    posicao += 1

print('\n', end='')