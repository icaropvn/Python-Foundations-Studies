'''
Exercício 071 - Forma 2
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
resto = valor
print('\n', end='')

cedula = 50
totcedula = 0
cont = 1
while True:
    if resto == 0:
        break
    totcedula = resto // cedula
    resto = resto % cedula
    if totcedula > 0:
        print(f'Total de {totcedula} cédulas de R${cedula}')
    if cont == 1:
        cedula = 20
    elif cont == 2:
        cedula = 10
    else:
        cedula = 1
    cont += 1
