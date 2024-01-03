'''
Exercício 086
"Matriz"

    Algoritmo para criar uma matriz de dimensão 3x3 e
preenchê-la com valores lidos do usuário.
    No final, mostrar a matriz na tela com a formatação correta.
'''

from random import choice

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
inputs = ['Insira um número: ', 'Digite um número: ', 'Escolha um número: ']

for i in range(0, 3):
    for j in range(0, 3):
        matrix[i][j] = int(input(choice(inputs)))

print()

for i in range(0, 3):
    for j in range(0, 3):
        if j == 0:
            print(f'| {matrix[i][j]:2} ', end='')
        elif j == 2:
            print(f' {matrix[i][j]:2} |')
        else:
            print(f'{matrix[i][j]:2}', end='')