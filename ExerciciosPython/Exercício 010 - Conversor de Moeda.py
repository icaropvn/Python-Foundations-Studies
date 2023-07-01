# Exercício 010
# Conversor de Real para Dólar e Euro
# US$1.00 = R$5.05 (23/04/2023)
# 1.00 € = R$5.55 (23/04/2023)

real = float(input('Insira a quantidade a ser convertida: R$'))

dolar = real / 5.05
euro = real / 5.55

print(f'Você conseguirá comprar US${dolar:.2f} e {euro:.2f} €')
