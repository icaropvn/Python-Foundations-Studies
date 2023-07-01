'''
Exercício 029
"Limite de Velocidade"

Algoritmo para ler a velocidade de um carro.
Se a velocidade for maior que 80Km/h, o motorista será multado.
A multa custa R$7.00 por cada Km acima do limite.
'''

red = '\033[31m'
green = '\033[32m'
negative = '\033[7m'
end = '\033[m'

velocidade = float(input('Insira a velocidade do veículo (Km/h): '))

if velocidade > 80:
    multa = (velocidade - 80) * 7
    print(f'{red}Você ultrapassou o limite de velocidade e receberá uma multa de {negative}R${multa:,.2f}{end}{red}.{end}')
else:
    print(f'{green}Você estava dentro do limite de velocidade. Nenhuma multa será cobrada.{end}')
