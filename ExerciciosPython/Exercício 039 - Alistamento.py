'''
Exercício 039
"Alistamento"

Algoritmo para ler a data de nascimento do usuário e informar:

- Se ele ainda vai se alistar no serviço militar
- Se está na hora de ele se alistar
- Se já passou da hora de se alistar

Mostre o tempo faltante ou excedente.
'''

from datetime import date
ano = date.today().year

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
italic = '\033[3m'
end = '\033[m'

genre = str(input('Insira seu sexo biológico: ').strip().lower())

if genre == 'feminino':
    print(f'{italic}{yellow}De acordo com a legislação brasileira, não é necessário para você realizar o '
          f'Alistamento Militar Obrigatório.{end}')
elif genre == 'masculino':
    data = str(input('Insira sua data de nascimento (dd/mm/aa): '))
    data = data.replace('/', ' ')
    data = data.split()

    data[2] = int(data[2])
    age = ano - data[2]

    if age < 18:
        print(f'{green}Você ainda não precisa se alistar. Ainda falta(m): {yellow}{18 - age}{green} ano(s)! '
            f'({data[2] + 18}){end}')
    elif age == 18:
        print(f'{red}Este é o ano do seu alistamento! Que merda...{end}')
    else:
        print(f'{red}Seu alistamento está {yellow}{age - 18}{red} ano(s) atrasado. '
            f'({data[2] + 18}){end}')
else:
    print(f'{red}Insira uma opção válida.{end}')
