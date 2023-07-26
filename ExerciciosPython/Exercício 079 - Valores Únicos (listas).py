'''
Exercício 079
"Valores Únicos (listas)"

Algoritmo para ler valores indeterminados do usuário e
cadastrá-los numa lista. Caso o número já esteja nela, ele
não será adicionado.

No final, serão exibidos todos os valores únicos da lista
em ordem CRESCENTE
'''

red = '\033[3;31m'
ita = '\033[3m'
end = '\033[m'

nums = list()

stop = 0
while True:
    num = int(input('> Digite um valor: '))
    if num not in nums:
        nums.append(num)
    else:
        print(f'{red}O valor digitado é uma duplicata.{end}\n')

    while True:
        answer = str(input(f'{ita}Gostaria de inserir mais valores? [S/N]{end}\n')).strip().lower()
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

nums.sort()
print(20 * '=-=' + '\n'
      f'{ita}Lista dos valores inseridos:{end}\n'
      f'{nums}')
