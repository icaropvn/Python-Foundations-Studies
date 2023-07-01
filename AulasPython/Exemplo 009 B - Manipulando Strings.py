'''
Exemplo 009 (Lado B)
Manipulando Strings
'''

frase = 'Curso em Vídeo Python'
fraseb = '   Curso em Vídeo Python   '

print(frase.count('o'))
print(frase.count('O'))
print(frase.upper().count('O'))

print(len(frase))

print(fraseb.strip())

print(frase.replace('Python', 'JavaScript'))

print('Curso' in frase)

print(frase.find('Vídeo'))
print(frase.find('video'))
print(frase.lower().find('vídeo'))
