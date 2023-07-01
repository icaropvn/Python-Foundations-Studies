'''
Exercício 033
"Maior e Menor de 3 Números"

Algoritmo para ler 3 números e retornar o maior e o menor entre eles.
'''

blue = '\033[34m'
red = '\033[31m'
end = '\033[m'

n1 = int(input('Insira o primeiro número: '))
maior = n1
menor = n1

n2 = int(input('Insira o segundo número: '))
if n2 > maior:
    maior = n2
if n2 < menor:
    menor = n2

n3 = int(input('Insira o terceiro número: '))
if n3 > maior:
    maior = n3
if n3 < menor:
    menor = n3

print(f'\n'
      f'{blue}Maior:{end} {maior}\n'
      f'{red}Menor:{end} {menor}')
