'''
Exercício 044
"Comprando"

Algoritmo para ler o valor de um produto e
calcular o desconto/juros de acordo com a forma de
pagamento:

1 - À vista no DINHEIRO/PIX: 10% de desconto
2 - À vista no CARTÃO: 5% de desconto
3 - Até 2x no CARTÃO: Preço Normal
4 - Acima de 2x no CARTÃO: 20% de Juros
'''

red = '\033[31m'
blue = '\033[34m'
ita_yellow = '\033[3;33m'
ita_purple = '\033[3;35m'
end = '\033[m'

loja = ' JOANA MODAS '
print(f'{blue}{loja:=^40}{end}')

valor = float(input('Insira o valor da compra: R$'))
choice = int(input('\nEscolha sua forma de pagamento:\n'
                   '1 - DINHEIRO/PIX\n'
                   '2 - CARTÃO\n'
                   'R: '))
if choice == 1:
    valor = valor * 0.9
    print(f'\nVocê pagará o total de {ita_yellow}R${valor:.2f}{end} à vista no dinheiro/pix.')
elif choice == 2:
    parcelas = abs(int(input('Escolha a quantidade de parcelas desejadas (1 = à vista): ')))
    if parcelas == 1:
        valor = valor * 0.95
        print(f'\nVocê pagará o total de {ita_yellow}R${valor:.2f}{end} à vista no cartão.')
    elif parcelas == 2:
        print(f'\nVocê pagará o total de {ita_yellow}R${valor:.2f}{end} em 2x no cartão.')
    else:
        valor = valor * 1.2
        print(f'\nVocê pagará o total de {ita_yellow}R${valor:.2f}{end} em '
              f'{ita_purple}{parcelas}x de R${valor / parcelas:.2f}{end}')
else:
    print(f'{red}Opção de pagamento inválida. Tente outra vez.{end}')
