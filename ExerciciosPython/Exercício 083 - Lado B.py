'''
Exercício 083
"Validando Expressões"
Lado B
'''

red = '\033[3;31m'
green = '\033[3;32m'
yellow = '\033[3;33m'
end = '\033[m'

expression = str(input('Insira uma expressão matemática: '))
aux = []

for char in expression:
    if char == '(':
        aux.append(char)
    elif char == ')':
        if len(aux) > 0:
            aux.pop()
        else:
            aux.append(')')

if len(aux) == 0:
    print(f'{green}Expressão válida!{end}')
else:
    if aux[0] == '(':
        print(f'{red}Expressão inválida.{end}\n'
              f'{yellow}Sua expressão possui parênteses a serem fechados.{end}')
    else:
        print(f'{red}Expressão inválida.{end}\n'
              f'{yellow}Sua expressão possui parênteses a mais.{end}')
