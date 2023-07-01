'''
Exercício 027

Algoritmo para ler o nome completo de uma pessoa e
mostrar o primeiro e último nomes separadamente.
'''

cian_ita = '\033[3;36m'
end = '\033[m'

nome = input('Insira o seu nome completo: ').strip()

lista = nome.split()

print(f'Primeiro nome: {cian_ita}{lista[0]}{end}\n'
      f'Último nome: {cian_ita}{lista[len(lista) - 1]}{end}')
