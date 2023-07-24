'''
Exercício 077
"Vogais"

Algoritmo que contenha uma tupla com várias palavras (sem acentos).
Mostrar para cada palavra quais são suas vogais.
'''

from random import choice

words_seq = ('perola', 'montanha', 'magnetismo', 'salgado', 'castor', 'rico', 'declarar',
             'vampiro', 'clube', 'mascote', 'vergonha', 'cardeal', 'raiva', 'fragmento',
             'anestesia', 'nuvem', 'confianca', 'cometa', 'diplomata', 'acordo')

words = (choice(words_seq), choice(words_seq), choice(words_seq), choice(words_seq),
         choice(words_seq), choice(words_seq), choice(words_seq))

flagA = 0
flagE = 0
flagI = 0
flagO = 0
flagU = 0

for word in words:
    print(f'A palavra {word.upper()} possui as vogais: ', end='')
    for letter in word:
        if letter == 'a' and flagA == 0:
            print(letter, end=' ')
            flagA = 1
        elif letter == 'e' and flagE == 0:
            print(letter, end=' ')
            flagE = 1
        elif letter == 'i' and flagI == 0:
            print(letter, end=' ')
            flagI = 1
        elif letter == 'o' and flagO == 0:
            print(letter, end=' ')
            flagO = 1
        elif letter == 'u' and flagU == 0:
            print(letter, end=' ')
            flagU = 1
    flagA = flagE = flagI = flagO = flagU = 0
    print('\n', end='')
