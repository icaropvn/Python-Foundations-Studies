from random import randint

red = '\033[31m'
yellow = '\033[33m'
green = '\033[32m'
cian = '\033[36m'
purple = '\033[35m'
italic = '\033[3m'
end = '\033[m'

title = 'PEDRA, PAPEL OU TESOURA'
subtitle = 'a game by Ícaro'

print(30*f'{red}=={end}' + '\n' + f'{cian}{title:^60}\n{italic}{subtitle:^60}{end}' + '\n' + 30*f'{red}=={end}')

options = ('Pedra', 'Papel', 'Tesoura')
pc = randint(0, 2)

player = int(input('Escolha uma opção:\n'
                   '[ 0 ] Pedra\n'
                   '[ 1 ] Papel\n'
                   '[ 2 ] Tesoura\n'
                   'R: '))

if player == 0 or player == 1 or player == 2:
    print('\n' + 12*'==' +
          f'{purple}\nEscolha do PC: {options[pc]}{end}\n'
          f'{cian}Sua Escolha: {options[player]}{end}\n' +
          12*'==' + '\n')
    if pc == player:
        print(f'{yellow}EMPATE!{end}')
    else:
        if pc == 0:
            if player == 1:
                print(f'{green}Você Venceu!!!{end}')
            else:
                print(f'{red}PC Venceu{end}')
        elif pc == 1:
            if player == 2:
                print(f'{green}Você Venceu!!!{end}')
            else:
                print(f'{red}PC Venceu{end}')
        else:
            if player == 0:
                print(f'{green}Você Venceu!!!{end}')
            else:
                print(f'{red}PC Venceu{end}')
else:
    print(f'{red}Opção Inválida{end}')
