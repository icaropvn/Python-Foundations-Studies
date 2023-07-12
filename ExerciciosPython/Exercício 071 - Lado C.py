'''
Exercício 071 - Forma 3
"Caixa Eletrônico"

Algoritmo para simular o funcionamento de
um caixa eletrônico.

No início perguntar ao usuário o valor a ser sacado (int),
e em seguida informar em quantas cédulas de cada valor serão
entregues.

Considerando as cédulas: R$50, R$20, R$10 e R$1
'''

name = 'SIRSO\'S BANK'
print(15*'--' + f'\n{name:^30}\n' + 15*'--')

valor = int(input('Quanto deseja sacar? R$'))

ced = 50
tot_ced = 0
while True:
    if valor >= ced:
        valor -= ced
        tot_ced += 1
    else:
        if valor == 0:
            break
        if tot_ced > 0:
            print(f'Total de {tot_ced} cédulas de R${ced}')
        tot_ced = 0
        if ced == 50:
            ced = 20
        elif ced == 20:
            ced = 10
        else:
            ced = 1
