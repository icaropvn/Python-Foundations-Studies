'''
Exercício 040
"Média do Aluno"

Algoritmo para ler duas notas de um aluno,
calcular sua média e mostrar o estado de aprovação do aluno

Média < 5.0 - REPROVADO
5.0 <= Média <= 6.9 - RECUPERAÇÃO
Média >= 7.0 - APROVADO
'''

red = '\033[31m'
green = '\033[32m'
yellow = '\033[33m'
end = '\033[m'

nota1 = float(input('Insira a nota da primeira prova: '))
nota2 = float(input('Insira a nota da segunda prova: '))

media = (nota1 * 0.4) + (nota2 * 0.6)

if media < 5:
    print(f'{red}O aluno está reprovado com média {media:.1f}.{end}')
elif media < 7:
    print(f'{yellow}O aluno terá que realizar a recuperação. Média {media:.1f}.{end}')
else:
    print(f'{green}O aluno está aprovado com média {media:.1f}.{end}')
