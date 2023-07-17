'''
Exercício 075
"Análise de Dados (tuplas)"

Algoritmo para ler 4 valores e colocá-los
numa tupla. Ao final, mostrar:

- Quantas vezes o número 9 foi digitado
- Em qual posição foi digitado o primeiro valor 3
- Quais foram os números pares digitados
'''

nums = (int(input('Insira um número: ')), int(input('Insira outro número: ')),
        int(input('Insira mais um número: ')), int(input('Insira o último número: ')))

count9 = nums.count(9)
if 3 in nums:
    pos3 = nums.index(3) + 1
else:
    pos3 = -1

if count9 > 0:
    print(f'\n1. Você digitou o número \'9\' {count9} vezes')
else:
    print(f'\n\033[3;31m1. Você não digitou o número 9 em nenhum momento\033[m')

if pos3 == -1:
    print(f'\033[3;31m2. O número 3 não se encontra na lista\033[m')
else:
    print(f'2. O primeiro número 3 se encontra na {pos3}ª posição')

print('3. Os números pares digitados foram: ', end='')
flag = 0
for i in range(0, 4):
    if nums[i] % 2 == 0:
        print(nums[i], end=', ')
    else:
        flag += 1

if flag == 4:
    print('\033[3;31mnenhum\033[m')
else:
    print('\n', end='')
