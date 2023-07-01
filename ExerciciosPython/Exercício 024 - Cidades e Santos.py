'''
Exercício 024

Algoritmo para ler o nome de uma cidade e
dizer se ela começa com a palavra "Santo"
'''

green = '\033[32m'
red = '\033[31m'
end = '\033[m'

cidade = str(input('Insira o nome da sua cidade: ')).strip()

if 'Santo' in cidade[:5].title():
    print(f'{green}A cidade "{cidade}" começa com "Santo"!{end}')
else:
    print(f'{red}A cidade "{cidade}" não começa com "Santo" :({end}')
