'''
Exercício 083
"Validando Expressões"

    Algoritmo para ler uma EXPRESSÃO MATEMÁTICA
do usuário.
    O programa deverá reconhecer a expressão como válida ou
não de acordo com a lógica dos parênteses usados.

'''

red = '\033[3;31m'
green = '\033[3;32m'
yellow = '\033[3;33m'
end = '\033[m'

expression = str(input('Insira uma expressão matemática: '))

if expression.count('(') == 0 and expression.count(')') == 0:
    print(f'{green}Expressão válida!{end}')
else:
    if expression.count('(') == expression.count(')'):
        print(f'{green}Expressão válida!{end}')
    else:
        print(f'{red}Expressão inválida.{end}')
        if expression.count('(') > expression.count(')'):
            print(f'{yellow}Sua expressão possui parênteses abertos.{end}')
        else:
            print(f'{yellow}Sua expressão possui parênteses fechados incoerentemente.{end}')