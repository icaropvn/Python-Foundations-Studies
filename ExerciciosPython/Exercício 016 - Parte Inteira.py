# Exercício 016
# Programa para ler um número qualquer (float) e imprimir sua parte inteira

from math import trunc

num = float(input('Insira um número real: '))

print(f'A parte inteira de {num} é {trunc(num)}')
# print(f'A parte inteira de {num} é {int(num)}')
