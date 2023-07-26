'''
Exercício 081
"Análise de Dados (listas)"

Algoritmo para ler inúmeros valores e colocá-los em
uma lista.

No final, mostrar:
- quantos números foram inseridos
- a lista em ordem decrescente
- verificar quantas vezes o número 5 aparece, e em quais posições

'''

red = '\033[3;31m'
end = '\033[m'

nums = list()
stop = 0

while True:
    nums.append(int(input('Insira um número: ')))
    while True:
        answer = str(input('Deseja inserir mais números? [S/N]\n')).strip().lower()
        if answer == 'sim' or answer == 's':
            print('\n', end='')
            break
        elif answer == 'não' or answer == 'nao' or answer == 'n':
            stop = 1
            break
        else:
            print(f'{red}Resposta inválida{end}\n')

    if stop == 1:
        break

print(20 * '=-=')

nums_copia = nums[:]
nums.sort(reverse=True)
print(f'1. Quantidade de valores inseridos: {len(nums)}\n'
      f'2. Lista em ordem decrescente: {nums}')

times5 = nums.count(5)
index5 = 0
if times5 > 0:
    print(f'3. O número 5 aparece {times5} vez(es) na lista.\n'
          f'   Nas posições: ', end='')
    for i in range(1, times5 + 1):
        if i == 1:
            index5 = nums_copia.index(5)
            print(f'{index5 + 1} ', end='')
        else:
            index5 = nums_copia.index(5, index5 + 1)
            print(f'{index5 + 1} ', end='')
else:
    print(f'{red}O número 5 não se encontra na lista{end}', end='')
print('\n', end='')
