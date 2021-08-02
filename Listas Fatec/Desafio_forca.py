import random
import requests

url = 'https://www.ime.usp.br/~pf/dicios/br-sem-acentos.txt'
palavras = requests.get(url).text.lower().split()

forca = [
'''   -----+
        |
        |
        |
        |
        |
--------+''',
'''   -----+
    |   |
        |
        |
        |
        |
--------+''',
'''   -----+
    |   |
    O   |
        |
        |
        |
--------+''',

'''   -----+
    |   |
    O   |
    |   |
        |
        |
--------+''',

'''   -----+
    |   |
    O   |
   /|   |
        |
        |
--------+''',
'''   -----+
    |   |
    O   |
   /|\  |
        |
        |
--------+''',

'''   -----+
    |   |
    O   |
   /|\  |
   /    |
        |
--------+''',

'''   -----+
    |   |
    O   |
   /|\  |
   / \  |
        |
--------+''']



p = random.choice(palavras)
certas = ''
erradas = ''
para = 0
cont = 0


while para < len(p):

    if para == len(p):
            print(final)
            break
    print(f'Dica: começa com {p[0]} e termina com {p[-1]}')
    chute = input('Chute uma letra: ').lower()

    for x in p:
        if  chute in certas+erradas:
            chute = input('Essa é uma letra repetida, tente novamente: ').lower()
        if x in chute:
            print(x, end = ' ')
            erradas = erradas + x
            print('Acertou um!!')
        else:
            print('_', x, end = ' ')
            certas = certas + x
            para = para + 1
            cont = cont + 1
                   
    if cont == 8:
        print('Fim de jogo')
        stop = input('Para recomeçar digite 1 ou para sair digite 0: ')
        if stop == 1:
            cont = 0
            para = 0
            chute = input('Chute uma letra: ').lower()
        else:
            break

                    
