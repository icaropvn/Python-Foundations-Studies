'''
Exercício 086
"Matriz"

    Algoritmo para criar uma matriz de dimensão 3x3 e
preenchê-la com valores lidos do usuário.
    No final, mostrar a matriz na tela com a formatação correta.
'''

# SOLUÇÃO CONCEBIDA SOZINHO
columns = []
lines = []

for i in range(0, 3):
    for j in range(0, 3):
        columns.append(int(input(f'Valor [{i}, {j}]: ')))
    lines.append(columns[:])
    columns.clear()

print(30 * '-')

for i in range(0, 3):
    for j in range(0, 3):
        print(f'{lines[i][j]:2} ', end='')
    print()
