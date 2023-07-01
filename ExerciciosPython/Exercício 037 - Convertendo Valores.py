'''
Exercício 037
"Convertendo Valores"

Algoritmo para ler um número inteiro e perguntar ao
usuário um código equivalente à base de conversão
desejada.

1 - Binário
2 - Octal
3 - Hexadecimal
'''

red = '\033[31m'
end = '\033[m'

num = abs(int(input('Insira um número para ser convertido: ')))
choice = int(input('Escolha a base de conversão:\n1 - Binário\n2 - Octal\n3 - Hexadecimal\nR: '))

if choice == 1:
    print(f'\nO número {num} é, em binário: {bin(num).removeprefix("0b")}')
elif choice == 2:
    print(f'\nO número {num} é, em octal: {oct(num).removeprefix("0o")}')
elif choice == 3:
    print(f'\nO número {num} é, em hexadecimal: {hex(num).removeprefix("0x")}')
else:
    print(f'\n{red}O valor digitado é inválido.{end}')
