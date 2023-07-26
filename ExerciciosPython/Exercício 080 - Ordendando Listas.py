'''
Exercício 080
"Ordenando Listas"

Algoritmo para ler 5 valores e guardá-los numa lista.

O valor deverá ser colocado já no seu lugar para que no final
a lista seja ordenada de forma crescente.

Usar o comando .sort() é proibido.
'''

nums = list()

for i in range(0, 5):
    if i == 0:
        nums.append(int(input(f'Digite o 1º valor: ')))
    else:
        num = int(input(f'Digite o {i+1}º valor: '))
        for j in range(0, len(nums)):
            if num < nums[j]:
                nums.insert(j, num)
                break
            if j == len(nums) - 1:
                nums.append(num)

print(20 * '==' + '\n'
      f'Lista dos valores em ordem crescente:\n'
      f'{nums}')
