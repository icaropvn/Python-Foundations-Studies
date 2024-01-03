'''
Exercício 084
"Análise de Dados (listas compostas)"

    Algoritmo para ler nome e peso de várias pessoas, guardando tudo
em uma lista.
    No final mostrar:

- Quantas pessoas foram cadastradas
- Uma listagem com as pessoas mais pesadas
- Uma listagem com as pessoas mais leves
'''

people = []
temp = []

stop = 0
loop = 1
maior = 0
menor = 0

while True:
    temp.append(str(input('Nome: ')).strip().title())
    weight = float(input('Peso (Kg): '))
    temp.append(weight)
    print(30 * '-')

    people.append(temp[:])

    if loop == 1:
        maior = temp[1]
        menor = temp[1]
    else:
        if weight > maior:
            maior = weight

        if weight < menor:
            menor = weight

    temp.clear()

    while True:
        answer = str(input('Cadastrar mais pessoas? ')).strip().lower()
        if answer == 'sim' or answer == 's':
            print(30 * '-')
            break
        elif answer == 'não' or answer == 'nao' or answer == 'n':
            print(30 * '-')
            stop = 1
            break
        else:
            print('Resposta inválida.')

    loop += 1

    if stop == 1:
        break

temp_counter = 0

print(f'Número de pessoas cadastradas: {len(people)}\n'
      f'Pessoas mais pesadas ({maior:.2f}Kg): ', end='')

for data in people:
    if data[1] == maior:
        temp_counter += 1

for data in people:
    if data[1] == maior:
        if temp_counter > 2:
            print(f'{data[0]}, ', end='')
        elif temp_counter == 2:
            print(f'{data[0]} e ', end='')
        else:
            print(f'{data[0]}', end='')
        temp_counter -= 1

temp_counter = 0

for data in people:
    if data[1] == menor:
        temp_counter += 1

print(f'\nPessoas mais leves ({menor:.2f}Kg): ', end='')
for data in people:
    if data[1] == menor:
        if temp_counter > 2:
            print(f'{data[0]}, ', end='')
        elif temp_counter == 2:
            print(f'{data[0]} e ', end='')
        else:
            print(f'{data[0]}', end='')
        temp_counter -= 1

print()
