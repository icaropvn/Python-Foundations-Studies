'''
Exercício 048
"Ímpares e Múltiplos de 3"

Algoritmo para calcular a soma de todos os
números ímpares que são múltiplos de três e que
se encontram no intervalo de 1 a 500.
'''

ita_green = '\033[3;32m'
end = '\033[m'

soma = 0
nums = 0

# Forma 1
#   for i in range(1, 501, 2):
#       if i % 3 == 0:
#           print(i)
#           soma += i

# Forma 2 (otimizada)
for i in range(3, 501, 6):
    print(i)
    soma += i
    nums += 1

print(f'\nA soma final dos {nums} valores é: {ita_green}{soma}{end}')
