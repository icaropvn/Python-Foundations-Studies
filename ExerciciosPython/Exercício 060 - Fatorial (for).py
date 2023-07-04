'''
Exercício 060
"Fatorial (for)"

Algoritmo para ler um número
e mostrar seu fatorial.
'''

blue = '\033[3;34m'
green = '\033[3;32m'
end = '\033[m'

num = int(input('Insira um número para realizar seu fatorial: '))

print(f'{blue}{num}!{end} = ', end='')
fat = 1
for i in range(num, 0, -1):
    fat = fat * i
    if i != 1:
        print(f'{i} * ', end='')

print(f'1 = {green}{fat}{end}')