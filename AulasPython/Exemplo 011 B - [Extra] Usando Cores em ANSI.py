'''
Exemplo 011 (Lado B)
"Usando Cores em ANSI"

Aplicando cores com variáveis
'''

red_bold = '\033[1;31m'
blue = '\033[34m'
end = '\033[m'

print(f'{red_bold}BEWARE OF THE DOG!!!{end} {blue}LOL it\'s a joke...{end}')
