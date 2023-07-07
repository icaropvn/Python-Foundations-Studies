'''
Exercício 064
"Tratamento de Dados"

Algoritmo para ler vários valores inteiros do usuário.
Parar quando o usuário digitar 999 (flag).
Mostrar a quantidade de números inseridos e a soma entre eles,
desconsiderando o flag.
'''

red = '\033[31m'
green = '\033[3;32m'
cian = '\033[3;36m'
ita = '\033[3m'
end = '\033[m'

num = soma = cont = 0
while num != 999:
    num = int(input('Insira um valor inteiro (999 para encerrar): '))
    if num != 999:
        cont += 1
        soma += num

print(f'\n{ita}Quantidade de números inseridos: {green}{cont}{end}\n'
      f'{ita}Soma dos valores inseridos: {cian}{soma}{end}')