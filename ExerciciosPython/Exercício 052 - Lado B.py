red = '\033[31m'
green = '\033[32m'
end = '\033[m'

num = int(input('Insira um número: '))
cont = 0

if num != 1 and num != 0:
    for i in range(1, 10):
        if num % i == 0:
            cont += 1
            print(f'{red}{i}{end}', end=' ')
        else:
            print(f'{green}{i}{end}', end=' ')
else:
    cont = 0

if cont == 2 or cont == 1:
    print(f'\n{green}O número {num} possui apenas 2 divisores: número PRIMO!{end}')
else:
    print(f'\n{red}O número {num} possui {cont} divisores, ele NÃO é primo.{end}')
