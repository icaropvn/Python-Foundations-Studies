# Exercício 007 - Média das Notas de um aluno

nome = input('Qual o nome do aluno?\n')

nota1 = float(input(f'\nInsira a nota da prova parcial de {nome}: '))
nota2 = float(input(f'Insira a nota da prova final de {nome}: '))

# media = nota1*0.4 + nota2*0.6
media = (nota1 + nota2) / 2

print(f'\nA média de {nome} é: {media:.2f}')
