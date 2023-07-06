'''
Exercício 058
"Adivinhando Números II"

Melhorar o algoritmo do exercício 28.
O jogador tentará até adivinhar o número sorteado,
no final um contador mostrará a quantidade de palpites
efetuados.
'''

red = '\033[31m'
green = '\033[32m'
purple = '\033[35m'
cian = '\033[36m'
blue = '\033[34m'
yellow = '\033[33m'
end = '\033[m'

from random import randint
from time import sleep

name = 'ADIVINHANDO NÚMEROS 2'
print(15*f'{blue}=-=' + f'{cian}\n{name:^45}\n' + 15*f'{blue}=-={end}')

print(f'{green}PC: > Vou escolher um número entre 0 e 10.')
sleep(1)
print(f'PC: > Tente adivinhar!\n{end}')
pc = int(randint(0, 10))
sleep(1)

player = int(input('Insira aqui sua proposta: '))
palpites = 1
sleep(0.5)
while player != pc:
    if pc > player:
        player = int(input(f'\n{red}PC: > Resposta errada! O número é maior...\n{end}Tente de novo: '))
    else:
        player = int(input(f'\n{red}PC: > Resposta errada! O número é menor...\n{end}Tente de novo: '))
    palpites += 1
    sleep(0.5)

if palpites == 1:
    print(f'{cian}\nPC: > UAU! Você acertou de primeira! Parabéns!\nPC: > Resposta: {pc}\n{end}'
          f'{purple}PC: > Número de tentativas: {palpites}{end}')
elif palpites <= 5:
    print(f'{green}\nPC: > Parabéns! Você acertou, o número era {pc}!\n{end}'
          f'{purple}PC: > Número de tentativas: {palpites}{end}')
else:
    print(f'{yellow}\nPC: > Você acertou, mas com dificuldade... O número era {pc}.\n{end}'
          f'{purple}PC: > Número de tentativas: {palpites}{end}')
