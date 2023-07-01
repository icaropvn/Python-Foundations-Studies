# Exercício 012
# Cálculo de 5% Desconto em cima de um valor qualquer

preco_0 = float(input('Insira o preço do produto: R$'))
desconto = int(input('Insira o desconto (%): '))

preco_desc = preco_0 * (desconto/100)

print(f'\nPreço Original: R${preco_0:.2f}\n'
      f'Preço com Desconto ({desconto}%): R${preco_0 - preco_desc:.2f}')
