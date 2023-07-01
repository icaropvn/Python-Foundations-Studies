'''
Exercício 051
"Progressão Aritmética"

Algoritmo para ler o primeiro termo e a razão
de uma PA. No final, mostrar os 10 primeiros termos
dessa progressão.
'''

termo1 = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

print('\nPA = (', end='')
for i in range(termo1, termo1+10*razao, razao):
    if i == termo1+9*razao:
        print(f'{i})')
    else:
        print(i, end=', ')
