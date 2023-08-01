'''
Exercício 085
"Pares e Ímpares (listas compostas)'

    Algoritmo para ler 7 valores e cadastrá-los numa lista,
separando os valores pares dos ímpares.
    No final mostrar os valores pares e ímpares em ordem crescente.
'''

nums = [[], []]

for i in range(0, 7):
    num = int(input(f'Digite o {i+1}º número: '))
    if num % 2 == 0:
        nums[0].append(num)
    else:
        nums[1].append(num)

nums[0].sort()
nums[1].sort()

print(30 * '-')

print(f'Lista dos pares: {nums[0]}\n'
      f'Lista dos ímpares: {nums[1]}')
