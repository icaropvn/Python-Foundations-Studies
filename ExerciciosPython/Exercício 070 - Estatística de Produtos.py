'''
Exercício 070
"Estatística de Produtos"

Algoritmo para ler o nome e o preço de
indeterminados produtos. O programa deve perguntar
se o usuário deseja continuar. E no final deve
mostrar:

- Qual é o total a ser pago
- Quantos produtos custam mais de R$1000
- Qual é o nome do produto mais barato
'''

red = '\033[31m'
ita = '\033[3m'
end = '\033[m'

shop_name = 'SIRSO\'S COMPANY'
print(14*'---' + f'\n{shop_name:^42}\n' + 14*'---')

tot = 0
maiormil = 0
barato = 0
cont = 1
while True:
    name = str(input(f'Nome do produto {cont}: '))
    price = float(input(f'Preço do produto {cont}: R$'))
    print(14*'---')

    if cont == 1:
        barato = price
        barato_name = name

    tot += price

    if price > 1000:
        maiormil += 1
    if price < barato:
        barato = price
        barato_name = name

    while True:
        answer = str(input(f'{ita}Deseja cadastrar mais produtos? [S/N]{end} ')).strip().upper()
        if answer == 'S':
            cont += 1
            break
        elif answer == 'N':
            break
        else:
            print(f'{red}Resposta inválida.{end}\n' + 14*'---')

    print(14 * '---')
    if answer == 'N':
        break

print(f'Total a pagar: {ita}R${tot}{end}\n'
      f'Produtos que custam mais de R$1000: {ita}{maiormil}{end}\n'
      f'Produto mais barato: {ita}{barato_name} (R${barato:.2f}){end}')
