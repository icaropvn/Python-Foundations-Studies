'''
Exercício 041
"Categorias de Natação"

A confederação nacional de natação precisa de um algoritmo
para ler o ano de nascimento de um atleta e mostrar sua
respectiva categoria:

<= 9  - Mirim
<= 14 - Infantil
<= 19 - Junior
== 20 - Sênior
>  20 - Master
'''

from datetime import date

blue = '\033[34m'
red = '\033[31m'
negative = '\033[7m'
end = '\033[m'

born = int(input('Insira o ano do seu nascimento: '))
current = date.today().year
flag = 0

age = current - born

if age > 25:
    category = 'MASTER'
elif age > 19:
    category = 'SÊNIOR'
elif age > 14:
    category = 'JÚNIOR'
elif age > 9:
    category = 'INFANTIL'
elif age > 0:
    category = 'MIRIM'
else:
    print(f'{red}Data inválida.{end}')
    flag = 1

if flag == 0:
    print(f'{blue}Sua categoria é {negative}{category}{end}{blue}.{end}')
