'''
Exercício 026

Algoritmo para ler uma frase qualquer e mostrar:
- Quantas vezes aparece a letra "A"
- Em que posição ela aparece primeiro
- Em que posição ela a aparece por último
'''

blue = '\033[34m'
yellow = '\033[33m'
red = '\033[31m'
end = '\033[m'

frase = str(input('Insira uma frase qualquer para ser analisada: ')).strip()

quantity = frase.lower().count('a')
primeiro = frase.lower().find('a')
ultimo = frase.lower().rfind('a')

if quantity == 1:
    print(f'\nA frase contém {blue}1{end} A')
elif quantity == 0:
    print(f'\nA frase contém {red}0{end} A\'s')
else:
    print(f'\nA frase contém {blue}{quantity}{end} A\'s')

if primeiro != -1 and ultimo != -1:
    print(f'O primeiro se encontra no índice {yellow}{primeiro}{end} (caractere {primeiro + 1})\n'
          f'O último se encontra no índice {yellow}{ultimo}{end} (caractere {ultimo + 1})')
else:
    print(f'{red}Não há nenhuma letra A na frase digitada.{end}')
