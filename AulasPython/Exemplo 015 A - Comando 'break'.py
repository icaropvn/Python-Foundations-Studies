'''
Exemplo 015
"Comando 'break'"
'''

cont = 1

''' O comando 'while' é executado sempre quando sua condição é VERDADEIRA,
    por conta disso, se colocarmos 'True' na condição, o comando será executado
    eternamente (loop infinito) '''

while True:
    print(cont, end='  ')
    cont += 1
print('Fim')