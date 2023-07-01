'''
Exercício 046
"Feliz Ano Novo!"

Algoritmo para mostrar uma contagem regressiva para o
estouro de fogos de artifício do ano novo, indo de 10 a 0,
com uma pausa de 1 segundo entre eles.
'''

from time import sleep
import emoji

for secs in range(10, 0, -1):
    print(secs)
    sleep(1)

print(emoji.emojize(f'\033[3;36mFELIZ ANO NOVO!!!\033[m :sparkler:'))