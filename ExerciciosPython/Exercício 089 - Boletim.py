'''
Exercício 089
"Boletim"

    Algoritmo para guardar nome, notas e média de alunos
em uma lista composta e mostrar um boletim apenas com a média e
a situação do aluno (APR ou REP)
    O algoritmo deve conseguir dar ao usuário a escolha de
ver as notas que compõem a média de um aluno específico.
'''

alunos = [['Almeida', [8.7, 5.6]], ['Garcia', [3.5, 9]], ['Novaes', [4.5, 8.2]], ['Alencar', [6.4, 8.9]],
          ['Moff Gideon', [9.3, 2.7]]]

for aluno in alunos:
    notas = aluno[1]
    media = sum(notas) / len(notas)
    aluno.append(media)

counter = 1
print('| Código |        Nome        | Média | Situação |')
print('|--------|--------------------|-------|----------|')
for aluno in alunos:
    print(f'| {counter:6} | {aluno[0]:^18} | {aluno[2]:5.2f} |', end='')
    if aluno[2] < 5:
        print('      REP |')
    else:
        print('      APR |')
    counter += 1
print('|--------|--------------------|-------|----------|')

print()

while True:
    answer = int(input('[1] Buscar Notas\n[0] Sair\nR: '))

    if answer == 1:
        codigo_aluno = int(input('\nInsira o código do aluno desejado para visualizar suas notas: '))
        codigo_aluno -= 1
        print('----------------------------------------')
        print(f'Notas de {alunos[codigo_aluno][0]}: {alunos[codigo_aluno][1]}')
        print('----------------------------------------')
    elif answer == 0:
        print('\nTenha um bom dia!')
        break
    else:
        print(f'\033[31mOpção inválida. Escolha uma das opções acima.\033[m')