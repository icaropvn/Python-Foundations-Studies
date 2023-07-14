'''
Exemplo 016 - Lado B
"Tuplas"
'''

a = (2, 5, 4)
b = (5, 8, 1, 2)

# A soma em tuplas junta uma tupla na outra, criando uma nova com todos os elementos
# das anteriores
c = a + b

print(a)
print(b)
print(c)

# .count() retorna a quantidade de elementos encontrado na tupla
print(c.count(5), 'números 5 dentro de c')

# .index() retorna o índice do elemento especificado
print('Índice', c.index(5), 'para o elemento \'5\'')

# .index() mas com excessão (procura do elemento se inicia a partir do índice 2)
print('Índice', c.index(5, 2), 'para o elemento \'5\' a partir do índice 2')
