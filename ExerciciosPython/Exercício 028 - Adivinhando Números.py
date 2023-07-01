'''
Exercício 028
"Adivinhando Números"

Algoritmo para escolher um número entre 0 e 5.
Ler proposta do usuário e retornar se a ela estava correta ou não
'''

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
purple = '\033[35m'
blue = '\033[34m'
italic = '\033[3m'
end = '\033[m'

from random import randint
from time import sleep

print(f'{blue}=-='*20, f'\n{purple}Vou pensar em número entre 0 e 5. {italic}Tente adivinhar...{end}')
print(f'{blue}=-={end}'*20)

num = randint(0, 5)
num_user = int(input('Insira sua proposta: '))

print('Processando...')
sleep(1.5)

if num_user == num:
    print(f'{green}Resposta correta! O número escolhido foi {num}{end}')
else:
    print(f'{red}Resposta errada. O número escolhido foi {num}{end}')
