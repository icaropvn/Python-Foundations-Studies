'''
Exemplo 010 (Lado B)
Condições
'''

n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))

media = (n1 + n2) / 2

if media < 5:
    print(f'Reprovado com média {media:.1f}')
elif media <= 6:
    print(f'Aprovado com média {media:.1f}')
else:
    print(f'Aprovado com média {media:.1f}!')
