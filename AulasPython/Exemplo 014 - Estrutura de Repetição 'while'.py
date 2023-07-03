'''
Exemplo 014
"Estrutura de Repetição 'while'"
'''

# Quando sabe-se o limite
i = 1
while i < 10:
    print(i)
    i += 1

# Quando NÃO se sabe o limite
num = 1
while num != 0:
    num = int(input('Digite um valor (diferente de 0): '))
print('Eu avisei.')