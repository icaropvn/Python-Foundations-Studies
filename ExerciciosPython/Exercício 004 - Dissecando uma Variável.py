# Atividade 004
# Imprima todos os possíveis testes para a variável

something = input('Digite algo: ')

tipo = type(something)
alnum = something.isalnum()
alpha = something.isalpha()
num = something.isnumeric()
space = something.isspace()
upper = something.isupper()
low = something.islower()
cap = something.istitle()

print('\nTipo do dado: {}\nÉ alfanumérico? {}'.format(tipo, alnum))
print('É alfabético? {}\nÉ numérico? {}\nContém apenas espaços? {}'.format(alpha, num, space))
print('Está em maiúsculo? {}\nEstá em minúsculo? {}\nContém apenas a primeira letra maiúscula? {}'.format(upper, low, cap))
