'''
Exercício 069
"Análise de Grupo"

Algoritmo para ler a idade e o sexo de um número
indeterminado de pessoas. A cada pessoa cadastrada, perguntar
se o usuário deseja continuar.

Ao final, mostrar:
- Quantidade de pessoas maiores de 18 anos
- Quantidade de homens cadastrados
- Quantidade de mulheres menores de 20 anos
'''

purple = '\033[35m'
green = '\033[32m'
yellow = '\033[33m'
red = '\033[31m'
ita = '\033[3m'
end = '\033[m'

name = 'CADASTRE UMA PESSOA'
print(10*'-----' + f'\n{name:^50}\n' + 10*'-----')

stop = 0
people18 = men = women20 = 0
i = 1
while True:
    age = int(input(f'Idade da pessoa {i}: '))
    if age > 18:
        people18 += 1

    genre = ' '
    while genre not in 'MF':
        genre = str(input(f'Sexo biológico da pessoa {i} [M/F]: ')).strip().upper()
        if genre not in 'MF':
            print(f'{red}Insira uma resposta válida.{end}')
            print(10 * '-----')
    if genre == 'M':
        men += 1
    if genre == 'F' and age < 20:
        women20 += 1

    print(10*'-----')

    while True:
        answer = str(input(f'{ita}Deseja cadastrar mais pessoas? [S/N]{end} ')).strip().upper()
        if answer == 'S' or answer == 'SIM':
            i += 1
            break
        elif answer == 'N' or answer == 'NÃO' or answer == 'NAO':
            stop = 1
            break
        else:
            print(f'{red}Insira uma resposta válida.{end}')
            print(10 * '-----')

    print(10 * '-----')
    if stop == 1:
        break

print(f'{purple}Pessoas maiores de 18 anos: {people18}{end}\n'
      f'{green}Quantidade de homens: {men}{end}\n'
      f'{yellow}Mulheres menores de 20 anos: {women20}{end}')
