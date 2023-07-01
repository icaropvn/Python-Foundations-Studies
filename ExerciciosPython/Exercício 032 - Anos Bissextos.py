'''
Exercício 032
"Anos Bissextos"

Algoritmo para ler um ano qualquer e retornar se ele é bissexto ou não.
'''

# Resolução Inicial
'''
ano = int(input('Insira um ano qualquer: '))

if ano % 4 == 0:
    print(f'O ano {ano} é bissexto.')
else:
    print(f'O ano {ano} NÃO é bissexto.')
'''

yellow = '\033[33m'
green = '\033[32m'
red = '\033[31m'
underline = '\033[4m'
end = '\033[m'

from datetime import date

ano = input(f'{yellow}Insira um ano qualquer {underline}(para ano atual inserir "Atual"){end}{yellow}:{end} ').strip()

if ano.isnumeric():
    ano = int(ano)
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'{green}O ano é bissexto.{end}')
    else:
        print(f'{red}O ano NÃO é bissexto.{end}')
elif ano.lower() == 'atual':
    ano = date.today().year
    if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
        print(f'{green}O ano atual ({ano}) é bissexto.{end}')
    else:
        print(f'{red}O ano atual ({ano}) NÃO é bissexto.{end}')
else:
    print(f'{red}Resposta inválida.{end}')
