'''
Exercício 054
"18+"

Algoritmo para ler o ano de nascimento de 7 pessoas
e mostrar quantas delas já são maiores e quantas ainda não
são.
'''

green = '\033[3;32m'
red = '\033[3;31m'
end = '\033[m'

from datetime import date

current = date.today().year
maior = 0
menor = 0

for i in range(1, 8):
    born = int(input(f'Insira o ano de nascimento da pessoa {i}: '))
    if current - born >= 21:
        maior += 1
    else:
        menor += 1

print(f'\nDas 7, {green}{maior} pessoas já são maior de idade{end} e {red}{menor} não são.{end}')
