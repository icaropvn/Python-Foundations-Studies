'''
Exercício 045
"Pedra, Papel ou Tesoura"

Crie um algoritmo para jogar Pedra,
Papel ou Tesoura contra o usuário.
'''

red = '\033[31m'
cian = '\033[36m'
italic = '\033[3m'
pur_ita = '\033[3;35m'
yellow = '\033[33m'
green = '\033[32m'
end = '\033[m'

from random import choice

print(20*f'{red}==={end}' + f'\n{cian}PEDRA, PAPEL OU TESOURA\n{italic}a game by Ícaro{end}\n' + 20*f'{red}==={end}')

user = str(input('SUA VEZ! Escolha pedra, papel ou tesoura: ')).strip().lower()
pc = choice(['pedra', 'papel', 'tesoura'])

if user == pc:
    print(f'{pur_ita}PC escolheu {pc}.\n{end}'
          f'{yellow}\nEMPATE!{end}')
elif user == 'pedra' and pc == 'tesoura' or user == 'papel' and pc == 'pedra' or user == 'tesoura' and pc == 'papel':
    print(f'{pur_ita}PC escolheu {pc}.\n{end}'
          f'{green}\nVocê Venceu!!!{end}')
else:
    print(f'{pur_ita}PC escolheu {pc}.\n{end}'
          f'{red}\nVocê Perdeu. :({end}')
