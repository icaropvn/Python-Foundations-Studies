'''
Exercício 065
"Média, Maior e Menor"

Algoritmo para ler indeterminados valores do usuário.
Mostrar a média, o maior e o menor valor ao final.
Fazer confirmação de leitura ao usuário.
'''

purple = '\033[3;35m'
blue = '\033[3;34m'
yellow = '\033[3;33m'
ita = '\033[3m'
end = '\033[m'

soma = 0
maior = 0
menor = 0
valores = 0
answer = 'S'
while answer == 'S' or answer == 'SIM':
    num = int(input('Insira um valor: '))
    if valores == 0:
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num
    valores += 1
    soma += num
    answer = str(input(f'\n{yellow}Deseja continuar a ler dados?{end} ')).upper()

print(f'\n{ita}Média dos valores inseridos: {purple}{soma/valores:.3f}{end}\n'
      f'{ita}Maior valor lido: {blue}{maior}{end}\n'
      f'{ita}Menor valor lido: {yellow}{menor}{end}')
