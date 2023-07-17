'''
Exercício 074
"Maior e menor (tuplas)"

Algoritmo para gerar 5 números aleatórios e colocá-los em uma tupla.

Depois, mostrar a listagem de números gerados, indicando o maior e o menor
valor encontrados.
'''

from random import randint

tupla = (randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20), randint(0, 20))

maior = 0
menor = 0
for i in range(0, 5):
    if i == 0:
        menor = tupla[i]
        maior = tupla[i]
    else:
        if tupla[i] > maior:
            maior = tupla[i]
        elif tupla[i] < menor:
            menor = tupla[i]

print('Lista dos números escolhidos:')
for i in range(0, 5):
    if i == 4:
        print(f'{tupla[i]}', end='')
    else:
        print(f'{tupla[i]}', end=', ')

print('\n' + 20*'-' + '\n'
      f'Maior: {maior}\n'
      f'Menor: {menor}')
