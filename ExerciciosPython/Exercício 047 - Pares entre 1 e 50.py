'''
Exercício 047
"Pares entre 1 e 50"

Algoritmo para mostrar todos os números
pares no intervalo de 1 a 50.
'''

# Forma 1
'''
for i in range(1, 51):
    if i % 2 == 0:
        print(i)
'''

# Forma 2 (forma mais otimizada)
for i in range(2, 51, 2):
    print(i)
