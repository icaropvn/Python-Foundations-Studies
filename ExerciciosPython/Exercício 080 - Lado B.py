'''
Exercício 080
"Ordenando Listas"
Lado B
'''

green = '\033[3;32m'
end = '\033[m'

nums = list()

for i in range(0, 5):
    num = int(input(f'Digite o {i + 1}º valor: '))
    # Se o valor for o primeiro a ser digitado, ou maior que o último da lista, ele
    # consequentemente será o último.
    if i == 0 or num > nums[-1]:
        nums.append(num)
        print(f'{green}Valor adicionado no FINAL da lista.{end}')
    else:
        # Se não, o algoritmo entrará em um loop até achar um valor que o número seja
        # menor ou igual, nesse caso, ele irá inserir o número na posição em que o maior que ele
        # estava, deslocando-o para frente
        j = 0
        while j < len(nums):
            if num <= nums[j]:
                nums.insert(j, num)
                print(f'{green}Valor adicionado na posição {j} da lista.{end}')
                break
            j += 1

print(20 * '==' + '\n'
      f'Lista dos valores em ordem crescente:\n'
      f'{nums}')
