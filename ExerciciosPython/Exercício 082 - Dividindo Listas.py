'''
Exercício 082
"Dividindo Listas"

    Algoritmo para ler inúmeros valores e colocar em uma
lista.
    Depois disso, criar duas outras listas, uma para armazenar
os valores pares e outra, os ímpares.
    No final, mostrar o conteúdo das 3 listas.

'''

red = '\033[3;31m'
ita = '\033[3m'
end = '\033[m'

nums = []
pares = []
impares = []

stop = 0
while True:
    nums.append(int(input('> Digite um valor: ')))

    while True:
        answer = str(input(f'{ita}Continuar? [S/N]{end}\n')).strip().lower()
        if answer == 'sim' or answer == 's':
            print('\n', end='')
            break
        elif answer == 'não' or answer == 'nao' or answer == 'n':
            stop = 1
            break
        else:
            print(f'{red}Resposta inválida.{end}\n')

    if stop == 1:
        break

for num in nums:
    if num % 2 == 0:
        pares.append(num)
    else:
        impares.append(num)

print('\n' + 20 * '===')
print(f'Lista Completa: {nums}')

if len(pares) > 0:
    print(f'Lista (pares): {pares}')
else:
    print(f'Lista (pares): {red}A lista não contém nenhum elemento{end}')

if len(impares) > 0:
    print(f'Lista (ímpares): {impares}')
else:
    print(f'Lista (ímpares): {red}A lista não contém nenhum elemento{end}')
