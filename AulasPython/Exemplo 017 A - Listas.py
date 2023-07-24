'''
Exemplo 017
"Listas"
'''

# Listas!
print('1. Declarando uma lista!')
num = [2, 5, 9, 1]
print(f'{num}\n')

# Substituindo um elemento da lista
print('2. Substituindo um elemento da lista:')
num[2] = 3
print(f'{num}\n')

# Adicionando um elemento ao final da lista
print('3. Adicionando um elemento ao final da lista:')
num.append(7)
print(f'{num}\n')

# Adicionando um elemento em um índice específico
print('4. Adicionando um elemento em um índice específico:')
num.insert(2, 0)
print(f'{num}\n')

# Organizando uma lista em ordem CRESCENTE
print('5. Organizando uma lista em ordem CRESCENTE:')
num.sort()
print(f'{num}\n')

# Organizando uma lista em ordem DECRESCENTE
print('6. Organizando uma lista em ordem DECRESCENTE:')
num.sort(reverse=True)
print(f'{num}\n')

# Verificando quantidade de elementos de uma lista
print(f'7. Essa lista possui {len(num)} elementos!\n')

# Removendo o último elemento
print('8. Removendo o último elemento:')
num.pop()
print(f'{num}\n')

# Removendo um elemento específico
print('9. Removendo um elemento específico (com pop):')
num.pop(2)
print(f'{num}\n')

print('10. Removendo um elemento específico (com remove):')
num.remove(7)
print(f'{num}\n')