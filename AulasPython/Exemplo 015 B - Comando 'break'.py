'''
Exemplo 015 - Lado B
"Comando 'break'"
'''

num = soma = 0
while True:
    num = int(input('Digite um número: '))
    if num == 999:
        break
    soma += num
print(f'\nA soma vale {soma}')