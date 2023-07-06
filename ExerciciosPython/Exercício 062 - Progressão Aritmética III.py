'''
Exercício 062
"Progressão Aritmética III"

Refazer algoritmo 062, mas perguntar para
o usuário se o programa deve mostrar mais termos,
se sim, quantos.
'''

yellow = '\033[33m'
cian = '\033[3;36m'
end = '\033[m'

termo1 = int(input('Insira o primeiro termo da PA: '))
razao = int(input('Insira a razão da PA: '))

termo = termo1
tot_quantity = 10
quantity = 0
answer = 'S'
while answer == 'S' or answer == 'SIM':
    print('PA = (', end='')
    for i in range(1, tot_quantity+1):
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
    termo = termo1
    answer = str(input('\n\nDeseja imprimir mais termos? (S/N) ')).upper()
    if answer == 'S' or answer == 'SIM':
        quantity = int(input('Quantos? '))
        tot_quantity += quantity

print(f'\n{cian}Até a próxima!{end}')
