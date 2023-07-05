'''
Exercício 063
"Sequência de Fibonacci"

Algoritmo para ler um número N do usuário e
mostrar os N primeiros termos da Sequência de
Fibonacci.

1, 1, 2, 3, 5, 8, 13, 21, ...
'''

num = int(input('Insira a quantidade de termos da sequência a serem impressos: '))

print('1, 1', end=', ')
termo = 2
i = 1
while i != num:
    print(termo, end=', ')
    termo = termo + termo-1
    i += 1