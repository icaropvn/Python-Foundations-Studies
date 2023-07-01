# Exercício 015
# Aluguel de Carros - Ler dias, Km e imprimir preço
# R$60/dia - R$0.15/km

dias = int(input('Por quantos dias o carro foi alugado? '))
km = float(input('Qual foi a quilometragem rodada? '))

print(f'O preço a pagar é de R${dias*60 + km*0.15:.2f}')
