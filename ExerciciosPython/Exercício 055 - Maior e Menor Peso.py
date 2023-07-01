'''
Exercício 055
"Maior e Menor Peso"

Algoritmo para ler o peso de cinco pessoas.
Depois mostrar o maior e o menor peso lidos.
'''

red = '\033[31m'
blue = '\033[34m'
end = '\033[m'

maior = 0
menor = 0

for i in range(1, 6):
    peso = float(input(f'Insira o peso da pessoa {i}: '))
    if i == 1:
        menor = peso
        maior = peso
    else:
        if peso > maior:
            maior = peso
        if peso < menor:
            menor = peso

print(f'\n{red}O maior peso foi {maior}Kg{end}\n'
      f'{blue}O menor foi {menor}Kg{end}')