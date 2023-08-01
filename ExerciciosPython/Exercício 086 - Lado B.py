'''
Exercício 086
"Matriz - Lado B"
'''

matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(0, 3):
    for j in range(0, 3):
        matriz[i][j] = int(input(f'Valor [{i}, {j}]: '))

print(30 * '-')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{matriz[i][j]:5} ', end='')
    print()
