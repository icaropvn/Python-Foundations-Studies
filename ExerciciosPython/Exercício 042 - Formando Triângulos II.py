'''
Exercício 042
"Formando Triângulos II"

Algoritmo para ler o comprimento de 3 retas e retornar se elas
podem ou não formar um triângulo.
Em seguida dizer o tipo de triângulo que pode ser formado:

Equilátero - todos os lados iguais
Isósceles - dois lados iguais
Escaleno - todos os lados diferentes
'''

red = '\033[31m'
green = '\033[32m'
blue = '\033[34m'
end = '\033[m'

a = float(input('Insira a medida do lado A: '))
b = float(input('Insira a medida do lado B: '))
c = float(input('Insira a medida do lado C: '))

if a + b > c and a + c > b and b + c > a:
    check = f'{green}É possível formar um triângulo!{end}'
    if a == b == c:
        print(f'{check} {blue}O triângulo é equilátero.{end}')
    elif a == b or a == c or b == c:
        print(f'{check} {blue}O triângulo é isósceles.{end}')
    else:
        print(f'{check} {blue}O triângulo é escaleno.{end}')
else:
    print(f'{red}Não é possível formar um triângulo.{end}')