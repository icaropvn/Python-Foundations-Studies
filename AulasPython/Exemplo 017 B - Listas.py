'''
Exemplo 017 - Lado B
"Listas"
'''

valores = list()

for i in range(0, 5):
    valores.append(int(input('Digite seu valor: ')))
print('\n', end='')

# Printando listas com for
print('Os valores são: ', end='')
for valor in valores:
    print(valor, end=' ')
print('\n')

for chave, valor in enumerate(valores):
    print(f'No índice {chave}, há o valor {valor}.')