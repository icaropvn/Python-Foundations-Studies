'''
Exercício 025

Algoritmo para ler um nome de uma pessoa e dizer
se ele possui "Silva" nele.
'''

green = '\033[32m'
red = '\033[31m'
end = '\033[m'

nome = str(input('Insira seu nome: ')).strip().title()

if 'Silva' in nome:
    print(f'{green}Seu nome contém "Silva"!{end}')
else:
    print(f'{red}Você não é da família Silva.{end}')
