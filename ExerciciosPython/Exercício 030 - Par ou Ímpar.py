'''
Exercício 030
"Par ou Ímpar"

Algoritmo para ler um número inteiro e retornar se é par ou ímpar.
'''

blue = '\033[34m'
yellow = '\033[33m'
end = '\033[m'

num = int(input('Insira um número: '))

if num % 2 == 0:
    print(f'O número {num} é {blue}PAR.{end}')
else:
    print(f'O número {num} é {yellow}ÍMPAR.{end}')
