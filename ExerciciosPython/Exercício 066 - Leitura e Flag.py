'''
Exercício 066
"Leitura e Flag"

Algoritmo para ler vários valores inteiros.
Parar de ler quando o usuário digitar 999.
No final, mostrar a quantidade de valores lidos e soma entre
eles (desconsiderando o 999 (flag)).
'''

ita = '\033[3m'
end = '\033[m'

cont = soma = 0
while True:
    num = int(input('Digite um valor (999 para parar): '))
    if num == 999:
        break
    cont += 1
    soma += num

if cont > 1:
    print(f'\nA soma dos {ita}{cont}{end} valores é {ita}{soma}{end}')
else:
    print(f'\nO único valor digitado foi {ita}{soma}{end}')