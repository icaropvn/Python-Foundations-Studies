'''
Exercício 071 - Forma 1
"Caixa Eletrônico"

Algoritmo para simular o funcionamento de
um caixa eletrônico.

No início perguntar ao usuário o valor a ser sacado (int),
e em seguida informar em quantas cédulas de cada valor serão
entregues.

Considerando as cédulas: R$50, R$20, R$10 e R$1
'''

valor = int(input('Valor a ser sacado: '))

c50 = valor // 50
c20 = (valor % 50) // 20
c10 = (valor % 20) // 10
c1 = valor % 10

print(f'Cédulas de R$50: {c50}\n'
      f'Cédulas de R$20: {c20}\n'
      f'Cédulas de R$10: {c10}\n'
      f'Cédulas de R$1: {c1}\n')
