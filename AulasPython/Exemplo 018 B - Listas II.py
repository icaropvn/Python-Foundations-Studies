'''
Exemplo 018 - Lado B
"Listas II"
'''

pessoas = []
dados = []

totmaior = totmenor = 0

for i in range(0, 3):
    dados.append(str(input('Nome: ')))
    dados.append(int(input('Idade: ')))

    pessoas.append(dados[:])
    dados.clear()

print()
for p in pessoas:
    if p[1] >= 18:
        print(f'{p[0]} é maior de idade')
        totmaior += 1
    else:
        print(f'{p[0]} é menor de idade')
        totmenor += 1

print(f'Temos {totmaior} pessoas maior de idade e {totmenor} menor.')
