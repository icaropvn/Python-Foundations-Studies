# Exercício 017
# Ler as medidas do cateto oposto e adjacente, e imprimir a medida da hipotenusa

import math

cb = float(input('Insira o valor do cateto B (cm): '))
cc = float(input('Insira o valor do cateto C (cm): '))

# hip = math.sqrt(cb**2 + cc**2)

print(f'\nA medida da hipotenusa é {math.hypot(cb, cc):.2f}cm')
# A hipotenusa pode ser calculada manualmente, mas também pela função "hypot" da biblioteca "math"
