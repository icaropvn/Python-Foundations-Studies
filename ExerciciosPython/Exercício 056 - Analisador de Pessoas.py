'''
Exercício 056
"Analisador de Pessoas"

Algoritmo para ler o nome, idade e sexo de 4 pessoas.
No final, mostrar:

- A média de idade do grupo
- O nome do HOMEM mais velho
- Quantas MULHERES têm MENOS de 20 anos
'''

purple = '\033[3;35m'
cian = '\033[3;36m'
yellow = '\033[3;33m'
end = '\033[m'

women = 0
elder = 0
elder_name = ''
soma = 0
men = 0

for i in range(1, 5):
    if i != 1:
        name = str(input(f'\nInsira o nome da pessoa {i}: ')).title().strip()
    else:
        name = str(input(f'Insira o nome da pessoa {i}: ')).title().strip()

    age = int(input(f'Insira a idade da pessoa {i}: '))
    soma += age

    genre = str(input(f'Insira o sexo biológico da pessoa {i}: ')).lower().strip()

    if genre in 'Mmmasculino':
        men += 1

    if genre in 'Mmmasculino':
        if men == 1:
            elder = age
            elder_name = name
        elif age > elder:
            elder = age
            elder_name = name
    elif genre in 'Fffeminino':
        if age < 20:
            women += 1


print(f'\nA média de idade das pessoas é: {purple}{soma/4}{end}\n'
      f'O homem mais velho é: {yellow}{elder_name}, com {elder} anos.{end}\n'
      f'{cian}{women} mulher(es){end} têm menos de 20 anos.')
