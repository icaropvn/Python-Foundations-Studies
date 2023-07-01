# Exemplo 006

s1 = input('Digite algo: ')
s2 = input('Digite outra coisa: ')
s3 = input('Digite mais um pouco: ')

alnum1 = s1.isalnum()
numeric2 = s2.isnumeric()
alpha3 = s3.isalpha()

print('\ns1 é alfa-numérico?\n{}'.format(alnum1))
print('\ns2 é numérico?\n{}'.format(numeric2))
print('\ns3 é alfabético?\n{}'.format(alpha3))
