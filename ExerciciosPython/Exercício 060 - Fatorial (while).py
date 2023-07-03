'''
Exercício 060
"Fatorial (while)"

Algoritmo para ler um número
e mostrar seu fatorial.
'''

num = int(input('Insira um número para o fatorial: '))

i = num
tot = 1
while i != 1:
    tot = tot * i
    i -= 1

print(f'{num}! = {tot}')

