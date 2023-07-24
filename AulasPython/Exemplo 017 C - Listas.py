'''
Exemplo 017 - Lado C
"Listas"
'''

a = [2, 3, 5, 7]

'''
    A ação de atribuição quando aplicada às listas, cria uma relação de
conexão ou dependência, e não de cópia.

    Quando uma é alterada, ambas são.
'''

# Relação criada entre as listas A e B
b = a

# Alterando um elemento da lista B
b[1] = 0

# Imprimindo para ver o resultado
print(f'Lista A: {a}\n'
      f'Lista B: {b}')

'''
    Para copiar de fato uma lista, basta fazer com que a lista B
receba todos os elementos da lista A um por um.
'''

# B recebendo os elementos de A através do fatiamento de listas
b = a[:]

# Alterando um elemento da lista B
b[3] = 11

# Imprimindo para ver o resultado
print(f'\nLista A: {a}\n'
      f'Lista B: {b}')