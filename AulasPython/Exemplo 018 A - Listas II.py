'''
Exemplo 018 - Lado A
"Listas II"
'''

print('Teste 1')

teste = list()
teste.append('Gustavo')
teste.append(40)

pessoas = list()
# Da mesma forma que o sinal de '=', quando usado entre listas,
# cria uma relação de dependência entre elas, o comando .append()
# também resulta na mesma coisa.
pessoas.append(teste)

teste[0] = 'Maria'
teste[1] = 17
pessoas.append(teste)

print(f'   {pessoas}')
    # O output será [['Maria', 17], ['Maria', 17]]

del teste
del pessoas

# =================================================================================================

print('Teste 2')

# A forma certa de copiar um dado de uma lista para outra é:
teste = list()
teste.append('Gustavo')
teste.append(40)

pessoas = list()
pessoas.append(teste[:])

teste[0] = 'Maria'
teste[1] = 17
pessoas.append(teste[:])

print(f'   {pessoas}')

# =================================================================================================

print('\nTeste 3')

# Declarando listas compostas
galera = [['Leila', 19], ['Caíque', 33], ['Cláudio', 78], ['Maria Linda', 17]]
print(f'   {galera[0][0]}\n'
      f'   {galera[3][0]}\n'
      f'   {galera[2][1]}')

# =================================================================================================

print('\nTeste 4')

# Usando 'for' com listas compostas
for p in galera:
    print(f'   {p}')

print(30 * '-')

for p in galera:
    print(f'   {p[0]}')

print(30 * '-')

for p in galera:
    print(f'   {p[1]}')
