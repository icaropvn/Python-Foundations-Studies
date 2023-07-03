'''
Exercício 057
"Validação de Dados"

Algoritmo para ler o sexo de uma pessoa, mas que só aceita
como resposta 'M', 'F' ou 'OUTRO'.
Caso a resposta seja inválida, ler novamente.
'''

sexo = ''

while sexo != 'M' and sexo != 'F' and sexo != 'OUTRO':
    sexo = str(input('Insira seu sexo (M, F ou OUTRO): ')).upper()

if sexo == 'M':
    print('\nBem-vindo!')
elif sexo == 'F':
    print('\nBem-vinda!')
else:
    print('\nBem-vindo(a)!')