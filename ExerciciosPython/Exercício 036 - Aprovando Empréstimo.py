'''
Exercício 036
"Aprovando Empréstimo"

Algoritmo para aprovar um empréstimo bancário
para a compra de uma casa.

Ler valor da casa, salário do comprador e quantos anos levará até
o comprador pagar o empréstimo.
Calcular valor da prestação mensal, sendo que este não pode
exceder 30% do salário, senão o empréstimo será negado.
'''

red = '\033[31m'
green = '\033[32m'
end = '\033[m'

valor_casa = float(input('Insira o valor do imóvel desejado: R$'))
salario = float(input('Insira seu salário: R$'))
anos = int(input('Pretensão de tempo para o pagamento (anos): '))

prestacao = valor_casa / (anos*12)

if prestacao <= salario * 0.3:
    print(f'{green}Empréstimo aceito! Você pagará R${prestacao:.2f} p/ mês durante {anos} anos.{end}')
else:
    print(f'{red}Desculpe. O valor da prestação é maior que 30% do seu salário. Empréstimo Negado.{end}')
