'''
Exercício 031
"Preço de Viagens"

Algoritmo para calcular o preço de uma viagem de uma distância lida.

- R$0,50/Km para viagens de até 200Km
- R$0,45/Km para viagens mais longas
'''

blue = '\033[34m'
end = '\033[m'

distancia = float(input('Insira a distância da viagem (Km): '))

if distancia > 200:
    preco = distancia * 0.45
else:
    preco = distancia * 0.5

# Forma alternativa usando "if simplificado"
# preco = distancia * 0.45 if distancia > 200 else distancia * 0.5

print(f'O preço da passagem será de {blue}R${preco:.2f}{end}')
