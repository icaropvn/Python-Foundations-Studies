'''
Exemplo 012
"Condições Aninhadas"

Usando elif para comparar um nome para várias
alternativas de print
'''

nome = str(input('Qual é o seu nome? ')).strip().title()
flag = 0

if nome == 'Ícaro':
    print('Que nome maravilhoso!', end=' ')
elif nome == 'Maria Clara':
    print(f'Você deve ser linda!')
elif nome == 'Almeida':
    print('Faça me o favor...')
    flag = 1
else:
    print('Apenas mais um nome comum...')

if flag == 0:
    print(f'Bom dia, {nome}!')
else:
    print('\033[31mVaza daqui.\033[m')
