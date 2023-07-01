'''
Exemplo 009
Manipulando Strings
'''

frase = 'Curso em Vídeo Python'

print(frase[2])
# Imprime o caractere de índice 2

print(frase[0:14])
# Imprime caracteres de índice 0 à 13

print(frase[3:16:2])
# Imprime caractere de índice 3 à 15, pulando de 2 em 2

print(frase[:])
# Imprime do índice 0 até o final da string (tudo)

print("""Gelo II é uma forma cristalina romboedral do gelo
com uma estrutura altamente ordenada. É formado pela
compressão do gelo Ih em uma temperatura de 198 K (−75,1 °C) à 300 MPa ou
pela descompressão do gelo V. Quando aquecido sofre transformação para o gelo III.
O gelo de água comum é conhecido como gelo Ih (na nomenclatura de Bridgman).""")
# Forma de imprimir uma string de mais de uma linha
