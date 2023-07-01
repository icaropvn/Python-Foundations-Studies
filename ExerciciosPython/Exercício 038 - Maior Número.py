'''
Exercício 038
"Maior Número"

Algoritmo para ler 2 números e verificar (e imprimir)
o maior entre eles ou se eles são iguais.
'''

green = '\033[32m'
ita_yellow = '\033[3;33m'
end = '\033[m'

num1 = int(input('Insira um valor: '))
num2 = int(input('Insira mais um valor: '))

if num1 > num2:
    print(f'\n{green}{num1} é maior que {num2}{end}')
elif num1 < num2:
    print(f'\n{green}{num2} é maior que {num1}{end}')
else:
    print(f'\n{ita_yellow}Os números são iguais.{end}')
