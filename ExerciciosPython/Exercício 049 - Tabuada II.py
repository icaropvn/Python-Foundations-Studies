'''
Exercício 049
"Tabuada II"

Refazer algoritmo 009 com os
conhecimentos do 'for'.
'''

num = int(input('Insira um valor para a tabuada: '))
quantity = int(input('Insira a quantidade de valores da tabuada: '))

nome = f'TABUADA DO {num}'
print('\n' + 14 * '-')
print(f'{nome:^14}\n')

for i in range(1, quantity+1):
    print(f'{num:2} x {i:2} = {num*i:3}')

print(14 * '-')
