# Exemplo 005

num1 = input('Digite um valor: ')
num2 = int(input('Digite um segundo valor: '))
num3 = float(input('Agora digite um número real (float): '))
num4 = bool(input('Digite mais um valor: '))

print('\nTipo 1: {}\nConteúdo de num1: {}'.format(type(num1), num1))
print('\nTipo 2: {}\nConteúdo de num2: {}'.format(type(num2), num2))
print('\nTipo 3: {}\nConteúdo de num3: {}'.format(type(num3), num3))
print('\nTipo 4: {}'.format(type(num4)))  # Se houver algo dentro da variável, é considerado True, caso contrário, False
print('Conteúdo de num4: {}'.format(num4))
