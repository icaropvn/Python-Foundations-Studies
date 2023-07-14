'''
Exemplo 016
"Tuplas"
'''

lanche = ('Hamburger', 'Juice', 'Pizza', 'Pudding', 'French Fries')
# Tuplas são IMUTÁVEIS
# lanche[1] = 'Refrigerante' --- ERRO!

print(lanche, '\n')

print(len(lanche), '\n')

# Forma 1 de usar 'for' com tuplas (com índice)
for i in range(0, len(lanche)):
    print(lanche[i])
print('\n', end='')

# Forma 2 de usar 'for' com tuplas (sem índice)
for i in lanche:
    print(f'Eu quero {i} hoje!')
print('\n', end='')

# Forma 3 de usar 'for' com tuplas (com índice)
for index, element in enumerate(lanche):
    print(f'Elemento {element} no índice {index}')
print('\n', end='')

# Forma de imprimir a tupla organizada por ORDEM ALFABÉTICA, transformada em lista
print(sorted(lanche))