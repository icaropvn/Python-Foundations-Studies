'''
Exercício 067
"Tabuada III"

Algoritmo para mostrar a tabuada de vários números, uma de cada vez,
para cada valor digitado pelo usuário. O programa será interrompido
caso o valor digitado for negativo.
'''

ita = '\033[3m'
end = '\033[m'

loop = 0
while True:
    if loop == 0:
        num = int(input(f'{ita}Gostaria de ver a tabuada de qual valor?\n(insira um valor negativo para encerrar){end}\n'))
    else:
        num = int(input(f'{ita}\nE agora...? Qual valor?\n(insira um valor negativo para encerrar)\n{end}'))
    if num < 0:
        break
    print(7 * '--')
    for i in range(1, 11):
        print(f'{num:2} x {i:2} = {num*i:2}')
    print(7 * '--')
    loop = 1
print(f'{ita}\nObrigado! Até mais!{end}')