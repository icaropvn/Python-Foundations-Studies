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

print(f'Número de pessoas cadastradas: {len(people)}\n'
      f'Pessoas mais pesadas ({maior:.2f}Kg): ', end='')
for i in range(0, len(people)):
    if people[i][1] == maior:
        print(f'{people[i][0]} ', end='')

print(f'\nPessoas mais leves ({menor:.2f}Kg): ', end='')
for i in range(0, len(people)):
    if people[i][1] == menor:
        print(f'{people[i][0]} ', end='')

print()
