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
while True:
    user = str(input(f'> PC: {ita}Qual você quer ser? (impar/par){end} ')).strip().lower()
    if user == 'impar' or user == 'par':
        break
    else:
        print(f'{red}> PC: {ita}Resposta Inválida{end}')

stop = wins = 0
while True:
    if user == 'par':
        pc = 'impar'
    else:
        pc = 'par'
    print(f'> PC: Certo! Eu sou {pc}.')
    sleep(1.5)
    while True:
        user_num = str(input(f'> PC: {ita}Diga seu valor:{end} '))
        if user_num.isnumeric():
            user_num = int(user_num)
            break
        else:
            print(f'{red}> PC: {ita}Valor Inválido{end}')
    pc_num = randint(0, 10)
    if (user_num + pc_num) % 2 == 0:
        win = 'par'
    else:
        win = 'impar'
    sleep(1)
    print(f'\n> VALORES:\n'
          f'PC: {pc_num}\n'
          f'VOCÊ: {user_num}\n'
          f'SOMA: {user_num + pc_num} ({win})\n')
    if user == win:
        print(f'> PC: {green}VOCÊ VENCEU!{end} Vamos de novo!')
        wins += 1
    else:
        print(f'> PC: {red}Você perdeu...{end}\n> PC: {cian}Total de vitórias consecutivas: {wins}{end}')

        while True:
            print(20 * '--')
            answer = str(input('> PC: Deseja começar de novo com o contador de vitórias zerado?\n')).strip().lower()
            if answer == 'sim' or answer == 's':
                wins = 0
                user = str(input(f'> PC: {ita}Qual você quer ser? (impar/par){end} ')).strip().lower()
                break
            elif answer == 'não' or answer == 'nao' or answer == 'n':
                stop = 1
                break
            else:
                print(f'{red}> PC: {ita}Resposta Inválida{end}')

    if stop == 1:
        break

print(f'\n{ita}Mal posso esperar para jogar com você de novo!\nAté mais!{end}')
