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
light_people_counter = 0
heavy_people_counter = 0

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
        elif weight == maior:
            heavy_people_counter += 1

        if weight < menor:
            menor = weight
        elif weight == menor:
            light_people_counter += 1

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

person = 0

print(f'Número de pessoas cadastradas: {len(people)}\n'
      f'Pessoas mais pesadas ({maior:.2f}Kg): ', end='')
for i in range(0, len(people)):
    if people[i][1] == maior:
        person += 1
        if person == heavy_people_counter:
            print(f'e {people[i][0]}', end='')
        elif person == heavy_people_counter - 1:
            print(f'{people[i][0]} ', end='')
        else:
            print(f'{people[i][0]}, ', end='')

person = 0

print(f'\nPessoas mais leves ({menor:.2f}Kg): ', end='')
for i in range(0, len(people)):
    if people[i][1] == menor:
        if person == light_people_counter:
            print(f'e {people[i][0]}', end='')
        elif person == light_people_counter - 1:
            print(f'{people[i][0]} ', end='')
            person += 1
        else:
            print(f'{people[i][0]}, ', end='')
            person += 1
print()
