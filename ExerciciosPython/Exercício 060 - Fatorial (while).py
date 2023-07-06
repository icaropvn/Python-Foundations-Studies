'''
Exercício 060
"Fatorial (while)"

Algoritmo para ler um número
e mostrar seu fatorial.
'''

# from math import factorial
# A biblioteca math possui um método para o cálculo de fatorial

cian = '\033[3;36m'
yellow = '\033[3;33m'
end = '\033[m'

num = int(input('Insira um número para calcular o fatorial: '))

print(f'{cian}{num}!{end} = ', end='')

fat = 1
while num > 0:
    fat *= num
    if num > 1:
        print(f'{num} * ', end='')
    num -= 1

print(f'{num+1} = {yellow}{fat}{end}\n', end='')
