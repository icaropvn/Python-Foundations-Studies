'''
Exercício 078
"Maior e menor (listas)"

Algoritmo para ler 5 valores e guardá-los numa lista.

No final, mostrar o maior e menor valores com suas
respectivas posições na lista.
'''

nums = list()

for i in range(0, 5):
    nums.append(int(input(f'Digite o valor para o índice {i}: ')))

maior = max(nums)
menor = min(nums)

print(20 * '===')
print(f'Valores digitados: {nums}\n'
      f'Maior valor: {maior}, ', end='')

temp = nums.count(maior)
if temp > 1:
    print('nas posições ', end='')
else:
    print('na posição ', end='')
for i in range(0, 5):
    if nums[i] == maior:
        print(f'{i+1} ', end='')

print(f'\nMenor valor: {menor}, ', end='')

temp = nums.count(menor)
if temp > 1:
    print('nas posições ', end='')
else:
    print('na posição ', end='')
for i in range(0, 5):
    if nums[i] == menor:
        print(f'{i+1} ', end='')
print('\n', end='')
