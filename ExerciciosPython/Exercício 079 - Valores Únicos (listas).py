'''
Exercício 079
"Valores Únicos (listas)"

Algoritmo para ler valores indeterminados do usuário e
cadastrá-los numa lista. Caso o número já esteja nela, ele
não será adicionado.

No final, serão exibidos todos os valores únicos da lista
em ordem CRESCENTE
'''

nums = list()

while True:
    nums.append(int(input('Digite um valor: ')))