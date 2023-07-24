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

print(f'\nMaior valor: {maior}, na posição {nums.index(maior)+1}\n'
      f'Menor valor: {menor}, na posição {nums.index(menor)+1}')
