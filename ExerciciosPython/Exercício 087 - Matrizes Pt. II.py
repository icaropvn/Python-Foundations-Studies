'''
Exercício 087
"Matrizes Pt. II"

    Utilizando de base o algoritmo desenvolvido no exercício 086,
apprimorá-lo implementando:

1) A soma dos valores pares inseridos
2) A soma dos valores da terceira coluna
3) O maior valor da segunda linha
'''

from random import choice

matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
inputs = ['Insira um número: ', 'Digite um número: ', 'Escolha um número: ']

soma_pares = 0
soma_terceira_col = 0
maior_valor_segunda_lin = 0

for i in range(0, 3):
    for j in range(0, 3):
        valor = int(input(choice(inputs)))
        matrix[i][j] = valor

        if valor % 2 == 0:
            soma_pares += valor

        if j == 2:
            soma_terceira_col += valor

        if i == 1:
            if j == 0 or valor > maior_valor_segunda_lin:
                maior_valor_segunda_lin = valor

print()

for i in range(0, 3):
    for j in range(0, 3):
        if j == 0:
            print(f'| {matrix[i][j]:2} ', end='')
        elif j == 2:
            print(f' {matrix[i][j]:2} |')
        else:
            print(f'{matrix[i][j]:2}', end='')

print(f'\nSoma dos valores pares: {soma_pares}\n'
      f'Soma dos valores da terceira coluna: {soma_terceira_col}\n'
      f'Maior valor da segunda linha: {maior_valor_segunda_lin}')