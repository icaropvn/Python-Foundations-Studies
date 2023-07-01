'''
Exercício 023

Algoritmo para ler um número entre 0 e 9999 e imprimir o
valor de suas unidades, dezenas, centenas e milhares
'''

blue = '\033[34m'
purple = '\033[35m'
green = '\033[32m'
yellow = '\033[33m'
negative = '\033[7m'
end = '\033[m'

num = str(input('Insira um valor: ')).strip()
num_int = int(num)

unidade = f'Unidade: {num_int % 10}'
dezena = f'Dezena: {(num_int % 100) // 10}'
centena = f'Centena: {(num_int % 1000) // 100}'
milhar = f'Milhar: {(num_int % 10000) // 1000}'

# Forma Matemática 1
print(f'\n{negative}', 10*'=', 'Forma 1', 10*'=', f'{end}')
print(f'{blue}{unidade:^31}{end}\n'
      f'{purple}{dezena:^31}{end}\n'
      f'{yellow}{centena:^31}{end}\n'
      f'{green}{milhar:^31}{end}')

# Forma Matemática 2
print(f'\n{negative}', 10*'=', 'Forma 2', 10*'=', f'{end}')
print(f'{blue}Unidade: {num_int // 1 % 10}{end}\n'
      f'{purple}Dezena: {num_int // 10 % 10}{end}\n'
      f'{yellow}Centena: {num_int // 100 % 10}{end}\n'
      f'{green}Milhar: {num_int // 1000 % 10}{end}')
