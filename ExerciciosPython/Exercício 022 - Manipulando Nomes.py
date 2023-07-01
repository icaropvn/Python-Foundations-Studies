'''
Exercício 022

Algoritmo para ler o nome de uma pessoa e mostrar:

- O nome com todas as letras maiúsculas
- Todas minúsculas
- Quantos caracteres (sem considerar os espaços)
- Quantas letras tem o primeiro nome
'''

nome = str(input('Insira seu nome completo: ')).strip()

nome_M = nome.upper()
nome_m = nome.lower()
nome_lista = nome.split()
nome_lista2 = ''.join(nome_lista)

print(f'- {nome_M}\n'
      f'- {nome_m}\n'
      f'- Quantidade de letras: {len(nome_lista2)}\n'
      f'- Quantidade de letras do primeiro nome: {len(nome_lista[0])}')
