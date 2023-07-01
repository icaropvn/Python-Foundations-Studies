# Exercício 018
# Ler um ângulo e mostrar o valor de seu seno, cosseno e tangente

from math import sin, cos, tan, radians

angulo = int(input('Insira um ângulo em graus: '))

sin = sin(radians(angulo))
cos = cos(radians(angulo))
tg = tan(radians(angulo))

print(f'\nAs relações trigonométricas do ângulo {angulo} são:\n'
      f'{angulo}º em radianos: {radians(angulo):.2f} rad\n'
      f'sen({angulo}) = {sin:.2f}\n'
      f'cos({angulo}) = {cos:.2f}\n'
      f'tg({angulo}) = {tg:.2f}')
