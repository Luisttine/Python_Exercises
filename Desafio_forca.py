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

palavras = ['sorte', 'luis', 'anao']
chute = input('Chute uma letra: ').lower()
p = random.choice(palavras)
final = ''
cont = 0
para = 0

while para < len(p):
    if chute in p:
        final = final + chute
        para = para + 1
        if para == len(p):
            print('Acertou um!!')
            print(final)
            break
        print('Acertou um!!')
        chute = input('Chute uma letra: ').lower()
        print(final)
            
    else:
        print('Errou seu merda!!')
        print(forca[cont])
        print(final)
        cont = cont + 1
        chute = input('Tente outra letra letra: ').lower()
    if cont == 8:
        print('Fim de jogo')
        stop = input('Para recomeçar digite 1 ou para sair digite 0: ')
        if stop == 1:
            cont = 0
            para = 0
            chute = input('Chute uma letra: ').lower()
        else:
            break

                    