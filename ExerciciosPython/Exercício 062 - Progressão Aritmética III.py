'''
Exercício 062
"Progressão Aritmética III"

Refazer algoritmo 062, mas perguntar para
o usuário se o programa deve mostrar mais termos,
se sim, quantos.
'''

yellow = '\033[33m'
cian = '\033[3;36m'
ita = '\033[3m'
end = '\033[m'

termo1 = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

termo = termo1
tot_quantity = 10
quantity = 0
answer = 'S'
while answer == 'S' or answer == 'SIM':
    print('PA = (', end='')
    i = 1
    while i <= tot_quantity:
        if i == tot_quantity:
            if i > tot_quantity - quantity:
                print(f'{yellow}{termo}{end}', end=')')
            else:
                print(termo, end=')')
        else:
            if i > tot_quantity - quantity:
                print(f'{yellow}{termo}{end}', end=', ')
            else:
                print(termo, end=', ')
        termo += razao
        i += 1
    termo = termo1
    answer = str(input('\n\nDeseja imprimir mais termos? (S/N) ')).upper()
    if answer == 'S' or answer == 'SIM':
        quantity = int(input('Quantos? '))
        tot_quantity += quantity

print(f'\n{ita}Você gerou no total {cian}{i-1}{end}{ita} termos da PA.{end}\n'
      f'{cian}Até a próxima!{end}')
