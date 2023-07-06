'''
Exercício 057
"Validação de Dados"

Algoritmo para ler o sexo de uma pessoa, mas que só aceita
como resposta 'M', 'F' ou 'OUTRO'.
Caso a resposta seja inválida, ler novamente.
'''

red = '\033[31m'
ita = '\033[3m'
end = '\033[m'

sexo = str(input('Insira seu sexo (M, F ou OUTRO): ')).upper().strip()
while sexo != 'M' and sexo != 'F' and sexo != 'OUTRO':
    sexo = str(input(f'{red}Dado inválido.{end} Insira seu sexo: ')).upper().strip()

if sexo == 'M':
    print(f'\n{ita}Bem-vindo!{end}')
elif sexo == 'F':
    print(f'\n{ita}Bem-vinda!{end}')
else:
    print(f'\n{ita}Bem-vindo(a)!{end}')