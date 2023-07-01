'''
Exemplo 011 A
"Usando Cores em ANSI"

Imprimir na tela frases formatadas da seguinte maneira:
- Texto Branco e Fundo Vermelho
- Texto Amarelo Underlined e Fundo Azul
- Texto Roxo Bold e Fundo Amarelo
- Texto Branco e Fundo Verde
- Texto Cinza e Fundo Preto
- Texto Preto e Fundo Branco
'''

red = '\033[31m'

print('\033[97;41mEu amo demais a Maria Clara.\033[m\n'
      '\033[4;33;44mAlmeida Júnior, seu fiel companheiro.\033[m\n'
      '\033[2;35;43mGarcia Medeiros nasceu em Rolândia, no ano de 1968.\033[m\n'
      '\033[97;42mTa bom... A B C D E F G H I J K L M N O P Q R S T U V W X Y Z\033[m\n'
      '\033[37;40mNão sei o que dizer...\033[m\n'
      '\033[30;107mmerda merda merda merda merda merda merda\033[m\n'
      '\033[7;30;41mSei la, tanto faz na real fodase.\033[m')
