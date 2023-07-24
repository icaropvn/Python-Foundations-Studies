'''
Exercício 075
"Análise de Dados (tuplas)"

Algoritmo para ler 4 valores e colocá-los
numa tupla. Ao final, mostrar:

- Quantas vezes o número 9 foi digitado
- Em qual posição foi digitado o primeiro valor 3
- Quais foram os números pares digitados
'''

from random import choice

questions = ('Insira outro número: ', 'Insira mais um número: ', 'Insira outro: ', 'Mais um: ')

nums = (int(input('Insira um número: ')), int(input(choice(questions))),
        int(input(choice(questions))), int(input(choice(questions))))

count9 = nums.count(9)
if 3 in nums:
    pos3 = nums.index(3) + 1
else:
    pos3 = -1

if count9 > 0:
    if count9 == 1:
        print(f'\n1. Você digitou o número \'9\' 1 vez')
    else:
        print(f'\n1. Você digitou o número \'9\' {count9} vezes')
else:
    print(f'\n\033[3;31m1. Você não digitou o número 9 em nenhum momento\033[m')

if pos3 == -1:
    print(f'\033[3;31m2. O número 3 não se encontra na lista\033[m')
else:
    print(f'2. O primeiro número 3 se encontra na {pos3}ª posição')

print('3. Os números pares digitados foram: ', end='')
flag = 0
flag_par = 0
for i in range(0, 4):
    if nums[i] % 2 == 0:
        if flag_par == 0:
            print(nums[i], end='')
        else:
            print(f', {nums[i]}', end='')
        flag_par = 1
    else:
        flag += 1

if flag == 4:
    print('\033[3;31mnenhum\033[m')
else:
    print('\n', end='')
