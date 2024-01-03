'''
Exercício 088
"Mega Sena"

    Algoritmo para gerar uma quantidade de sequências de sorteios da Mega Sena
escolhida pelo usuário.
'''

from random import sample
from time import sleep

historico_sorteios = list()
sorteio_atual = list()

quant_sorteios = int(input('Quantos jogos deseja sortear?\nR: '))

print(f'\nSorteando {quant_sorteios} jogos...')
sleep(2)
print('---------------------------------------')

for i in range(0, quant_sorteios):
    numeros = list(range(1, 61))
    sorteio_atual = sample(numeros, 6)
    historico_sorteios.append(sorteio_atual[:])

for i in range(0, quant_sorteios):
    print(f'Jogo {i+1:2}: {historico_sorteios[i]}')
    sleep(0.5)

print('---------------------------------------')
print('Pronto! Aqui estão seus jogos. Boa Sorte!')