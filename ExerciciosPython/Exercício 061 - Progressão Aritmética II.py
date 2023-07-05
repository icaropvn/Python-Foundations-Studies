'''
Exercício 061
"Progressão Aritmética II"

Refazer algoritmo 051 usando while.
'''

termo = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

print(f'\nPA = (', end='')
i = 1
while i != 11:
    if i == 10:
        print(termo, end=')')
    else:
        print(termo, end=', ')
    termo += razao
    i += 1

print('\n', end='')