'''
Exemplo 016 - Lado C
"Tuplas"
'''

# Tuplas podem conter dados de diferentes tipos
person = ('Maria Clara', 17, 'F', 1.68, 'Perfeita')
print(person, '\n')

print(f'Nome: {person[0]}\n'
      f'Idade: {person[1]} anos\n'
      f'Sexo: {person[2]}\n'
      f'Altura: {person[3]}m\n'
      f'O que ela é? {person[4]}\n')

# Maneira para redefinir uma tupla durante o programa
# !!! UMA TUPLA INTEIRA PODE SER DELETADA, MAS UM ÚNICO ELEMENTO DELA NÃO !!!
tupla1 = (1, 2, 3, 4, 5)
print(f'Tupla antiga: {tupla1}')
del(tupla1)
print('\033[3m*tupla deletada*\033[m')
tupla1 = (6, 7, 8, 9, 10)
print(f'Tupla nova: {tupla1}')