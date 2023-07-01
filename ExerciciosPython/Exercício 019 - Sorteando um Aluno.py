# Exercício 019
# Um professor quer sortear um aluno para apagar a lousa entre 4 deles
# Algoritmo para escolher um aleatoriamente e imprimir o nome do escolhido

import random

a1 = input('Insira um nome: ').strip().title()
a2 = input('Insira outro nome: ').strip().title()
a3 = input('Insira outro nome: ').strip().title()
a4 = input('Insira mais um nome: ').strip().title()

alunos = [a1, a2, a3, a4]

print(f'\nO aluno escolhido foi: \033[33m{random.choice(alunos)}!\033[m')
