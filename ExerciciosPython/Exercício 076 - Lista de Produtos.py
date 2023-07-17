'''
Exercício 076
"Lista de Produtos"

Algoritmo que contenha uma tupla com nomes de produtos,
seguidos de seus preços.

Mostrar em forma de tabela a listagem dos produtos e seus
preços.
'''

produtos = ('Jaqueta', 140, 'Camiseta', 80.5, 'Calça Preta', 189.9, 'Tênis Casual', 459.99, 'Coturno Preto', 530,
            'Bolsa de Ombro Nike', 104.9, 'Tênis Esportivo Mizuno', 479.9)

name = 'SIRSO\'s STORE'
print(43*'-' + f'\n{name:^43}\n' + 43*'-')

for i in range(0, 14, 2):
    print(f'{produtos[i]:.<35}R${produtos[i+1]:6.2f}')
print(43*'-')