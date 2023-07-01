# Exercício 008
# Conversor de Metros para centímetros e milímetros

metro = float(input('Insira o valor a ser convertido (m): '))

km = metro / 1000
hm = metro / 100
dam = metro / 10
dm = metro * 10
cm = metro * 100
mm = metro * 1000

print(f'Valor em quilômetros: {km:,}km\n'
      f'Valor em hectômetros: {hm:,}hm\n'
      f'Valor em decâmetros: {dam:,}dam\n'
      f'Valor em decímetros: {dm:,}dm\n'
      f'Valor em centímetros: {cm:,}cm\n'
      f'Valor em milímetros: {mm:,}mm')
