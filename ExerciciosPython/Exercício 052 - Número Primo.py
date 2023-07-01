'''
Exercício 052
"Número Primo"

Algoritmo para ler um número inteiro
e mostrar se ele é um número primo ou não.
'''

green = '\033[32m'
red = '\033[31m'
end = '\033[m'

flag = 0
num = int(input('Insira um número: '))

if num != 1 or num != 0:
    for i in range(2, 10):
        if i != num and num % i == 0:
            flag = 1
else:
    flag = 1

if flag == 0:
    print(f'\n{green}O número {num} é primo!{end}')
else:
    print(f'\n{red}O número {num} NÃO é primo.{end}')