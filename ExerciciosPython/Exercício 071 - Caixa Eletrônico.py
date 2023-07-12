'''
Exercício 071 - Forma 1
"Caixa Eletrônico"

Algoritmo para simular o funcionamento de
um caixa eletrônico.

No início perguntar ao usuário o valor a ser sacado (int),
e em seguida informar em quantas cédulas de cada valor serão
entregues.

Considerando as cédulas: R$100, R$50, R$20, R$10, R$5, R$2 e R$1
'''

ita = '\033[3m'
end = '\033[m'

name = 'SIRSO\'S BANK'
print(15*'--' + f'\n{name:^30}\n' + 15*'--')

valor = int(input('Quanto deseja sacar? R$'))
resto = valor
print('\n', end='')

ced = 100
totced = 0
cont = 1
while True:
    if resto == 0:
        break
    totced = resto // ced
    resto = resto % ced
    if totced == 1:
        print(f'{ita}Total de {totced} cédula de R${ced}{end}')
    elif totced > 0:
        print(f'{ita}Total de {totced} cédulas de R${ced}{end}')
    if cont == 1:
        ced = 50
    elif cont == 2:
        ced = 20
    elif cont == 3:
        ced = 10
    elif cont == 4:
        ced = 5
    elif cont == 5:
        ced = 2
    else:
        ced = 1
    cont += 1
