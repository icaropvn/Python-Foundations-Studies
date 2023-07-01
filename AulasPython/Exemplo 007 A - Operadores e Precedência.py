# Exemplo 007

num1 = int(input('Insira um número: '))
num2 = int(input('Insira outro número: '))

print(f'\nA soma entre {num1} e {num2} é {num1 + num2}\n'
      f'A diferença é {num1 - num2}\n'
      f'O produto é {num1 * num2}\n'
      f'O quociente é {num1 / num2}\n'
      f'O quadrado de {num1} é {num1 ** 2}\n'
      f'A divisão inteira é {num1 // num2}\n'
      f'O resto da divisão é {num1 % num2}\n'
      f'A raiz quadrada de {num2} é {num2 ** (1/2)}', end=' | ')

print(f'Divisão Formatada: {num1 / num2:.2f}')
