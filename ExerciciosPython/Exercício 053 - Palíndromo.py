'''
Exercício 053
"Palíndromo"

Algoritmo para ler uma frase qualquer e mostrar se
ela é um palíndromo (desconsiderando espaços).
'''

blue = '\033[34m'
cian = '\033[36m'
red = '\033[31m'
green = '\033[32m'
end = '\033[m'

phrase = str(input('Insira a frase a ser analisada: ')).upper().strip()
phrase = phrase.split()
phrase = ''.join(phrase)
reverse = ''

# Forma 1 (for)
for i in range(len(phrase) - 1, -1, -1):
    reverse += phrase[i]

# Forma 2 (tratamento de string)
# reverse = phrase[::-1]

print(f'\nO inverso da frase {blue}{phrase}{end} é {cian}{reverse}{end}')

if reverse == phrase:
    print(f'{green}A frase é um palíndromo!{end}')
else:
    print(f'{red}A frase não é um palíndromo.{end}')
