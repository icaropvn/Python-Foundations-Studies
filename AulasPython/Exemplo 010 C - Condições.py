'''
Exemplo 010 (Lado C)
Condições
'''

n1 = float(input('Insira a primeira nota do aluno: '))
n2 = float(input('Insira a segunda nota do aluno: '))

media = (n1 + n2) / 2

# Estrutura condicional simplificada do Python
print('Parabéns!' if media >= 6 else 'Estude mais...', end=' ')
print(f'Sua média foi {media:.1f}')
