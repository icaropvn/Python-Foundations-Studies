# Exercício 011
# Pintando uma Parede
# 1L = 2m²

comprimento = float(input('Qual é o comprimento da parede (m)? '))
largura = float(input('Qual é a largura da parede (m)? '))

area = comprimento * largura
tinta = area / 2

print(f'A quantidade de tinta a ser utilizada para pintar {area}m²'
      f'({largura}x{comprimento}) será de {round(tinta+0.5)}L.')
