'''
Exercício 068
"Par ou Ímpar"

Jogo do par ou ímpar.

O jogo será interrompido quando o jogador perder,
mostrando ao final o total de vitórias consecutivas dele.
'''

from random import randint
from time import sleep

red = '\033[31m'
blue = '\033[34m'
cian = '\033[36m'
green = '\033[32m'
ita = '\033[3m'
end = '\033[m'

title = f'JOGO DO {blue}PAR{end} OU {red}ÍMPAR{end}'
title2 = f'{ita}a game by Ícaro{end}'
print(20*f'{blue}=-={end}' + f'\n{title:^68}\n{title2:^70}\n' + 20*f'{red}=-={end}')

sleep(1.5)
print('> PC: Vamos jogar par ou ímpar!')
sleep(1.5)
user = str(input(f'> PC: {ita}Qual você quer ser? (impar/par){end} ')).strip().lower()
if user == 'par':
    pc = 'impar'
else:
    pc = 'par'
print(f'> PC: Certo! Eu sou {pc}.')
sleep(1.5)

wins = 0
while True:
    user_num = int(input(f'> PC: {ita}Diga seu valor:{end} '))
    pc_num = randint(0, 10)
    if (user_num + pc_num) % 2 == 0:
        win = 'par'
    else:
        win = 'impar'
    print(f'\n> VALORES:\n'
          f'PC: {pc_num}\n'
          f'VOCÊ: {user_num}\n'
          f'SOMA: {user_num + pc_num} ({win})\n')
    if user == win:
        print(f'> PC: {green}VOCÊ VENCEU!{end} Vamos de novo!')
        wins += 1
    else:
        print(f'> PC: {red}Você perdeu...{end}\n> PC: {cian}Total de vitórias consecutivas: {wins}{end}')
        answer = str(input('\n> PC: Deseja começar de novo com o contador de vitórias zerado?\n')).strip().lower()
        if answer == 'sim' or answer == 's':
            wins = 0
            user = str(input(f'> PC: {ita}Qual você quer ser? (impar/par){end} ')).strip().lower()
        else:
            break

print(f'\n{ita}Mal posso esperar para jogar com você de novo!\nAté mais!{end}')
