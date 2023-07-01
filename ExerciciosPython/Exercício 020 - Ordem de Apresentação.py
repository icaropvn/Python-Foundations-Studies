# Exercício 020
# Ler 4 nomes de alunos e imprimir uma sequência para a ordem de apresentação de um trabalho

import random

blue = '\033[34m'
green = '\033[32m'
yellow = '\033[33m'
red = '\033[31m'
end = '\033[m'

a1 = input('Insira o nome de um aluno: ')
a2 = input('Insira o nome de outro aluno: ')
a3 = input('Insira o nome de mais um aluno: ')
a4 = input('Insira o nome de um último aluno: ')

alunos = [a1, a2, a3, a4]
random.shuffle(alunos)

print(f'\nA ordem do trabalho será:\n'
      f'1º - {blue}{alunos[0]}{end}\n'
      f'2º - {green}{alunos[1]}{end}\n'
      f'3º - {yellow}{alunos[2]}{end}\n'
      f'4º - {red}{alunos[3]}{end}')
