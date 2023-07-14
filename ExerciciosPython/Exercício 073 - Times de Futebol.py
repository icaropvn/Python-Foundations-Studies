'''
Exercício 073
"Times de Futebol"

Algoritmo para iniciar uma tupla com os 20 primeiros times
da tabela do brasileirão. E mostrar:

- Os primeiros 5 colocados
- Os últimos 4 colocados
- Uma lista com os times em ordem alfabética
- A posição da tabela que se encontra o time da Chapecoense
'''

times = ('Botafogo', 'Flamengo', 'Grêmio', 'Fluminense', 'Palmeiras', 'Bragantino', 'Fortaleza', 'São Paulo',
         'Cruzeiro', 'Internacional', 'Athletico PR', 'Atlético MG', 'Santos', 'Cuiabá', 'Corinthians', 'Bahia',
         'Goiás', 'Coritiba', 'Vasco da Gama', 'América MG')

print(f'Os 5 primeiros colocados do Brasileirão 2023 são: ', end='')
cont = 1
for i in range(0, 5):
    if cont == 5:
        print(f'e {times[i]}', end='')
    elif cont == 4:
        print(f'{times[i]} ', end='')
    else:
        print(f'{times[i]}, ', end='')
    cont += 1

print(f'\n\nÚltimos 4 colocados: ', end='')
cont = 1
for i in range(16, 20):
    if cont == 4:
        print(f'e {times[i]}', end='')
    elif cont == 3:
        print(f'{times[i]} ', end='')
    else:
        print(f'{times[i]}, ', end='')
    cont += 1

listaordem = sorted(times)
print('\n\nLista dos times em ordem alfbética: ', end='')
cont = 1
for i in range(0, 20):
    if i < 18:
        print(listaordem[i], end=', ')
    elif i == 18:
        print(listaordem[i], end=' e ')
    else:
        print(listaordem[i], end='')
    if cont % 5 == 0:
        print('\n', end='')
    cont += 1

flag = 0
for i in range(0, 20):
    if times[i] == 'Chapecoense':
        posicao = i+1
        flag = 1
        break

if flag == 0:
    print('\nA Chapecoense não se encontra na tabela.')
else:
    print(f'\nA Chapecoense se encontra na posição {posicao} na tabela.')
