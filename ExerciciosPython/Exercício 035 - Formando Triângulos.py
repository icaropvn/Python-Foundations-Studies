'''
Exercício 035
"Formando Triângulos"

Algoritmo para ler o comprimento de 3 retas e retornar se elas
podem ou não formar um triângulo.
'''

yellow = '\033[33m'
green = '\033[32m'
red = '\033[31m'
blue = '\033[34m'
end = '\033[m'

print(f'{blue}-=-{end}' * 10, f'\n{yellow}Verificador de Triângulos{end}')
print(f'{blue}-=-{end}' * 10)

a = float(input('Insira o tamanho da reta 1: '))
b = float(input('Insira o tamanho da reta 2: '))
c = float(input('Insira o tamanho da reta 3: '))

if a < b+c and b < a+c and c < a+b:
    print(f'{green}É possível formar um triângulo!{end}')
else:
    print(f'{red}Não é possível formar um triângulo :({end}')
