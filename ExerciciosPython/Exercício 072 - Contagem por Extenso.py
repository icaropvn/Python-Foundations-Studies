'''
Exercício 072
"Contagem por Extenso"

Algoritmo que inicia com uma tupla definida com os números de 0 a 20
escritos por extenso.

Ler um número entre 0 e 20 do usuário e mostrá-lo por extenso.
'''

from time import sleep

red = '\033[3;31m'
ita = '\033[3m'
end = '\033[m'

# Criação da tupla
nums = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze',
        'catorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

stop = 0
while True:
    user = int(input('Insira um número entre 0 e 20: '))
    if user < 0 or user > 20:
        print(f'{red}Resposta inválida.{end}')
    else:
        print(f'O número {user} por extenso é: {ita}{nums[user]}{end}\n')
        sleep(1.5)
        while True:
            answer = str(input(f'{ita}Gostaria de inserir outro número? [S/N]{end}\n')).strip().lower()
            if answer == 's' or answer == 'sim':
                break
            elif answer == 'n' or answer == 'nao' or answer == 'não':
                stop = 1
                break
            else:
                print(f'{red}Resposta inválida.{end}')
        if stop == 1:
            break

print(f'\n{ita}Certo! Até a próxima!{end}')