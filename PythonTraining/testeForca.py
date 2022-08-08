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
erradas = ''
para = 0
acertos = ''
cont = 0

while para == 0:
    print(f'Dica: começa com {p[0].upper()} e termina com {p[-1].upper()}')
    chute = input('Chute uma letra: ')

    if chute in erradas or chute in acertos:
        print('Essa ja foi...tente de novo')
        continue
    else:
        if acertos != '':
            print('As letras acertadas digitadas são: ')
            chutes = [i for i in acertos]
            print(chutes, '\n')
        if erradas != '':
            print('As letras erradas são:')
            errado = [i for i in erradas]
            print(errado, '\n')
    
    if chute in p:
        acertos+=chute
        print('Você acertou uma letra!!\n')
        continue
    else:
        print('Errou burrao...')
        print(forca[cont], '\n')
        erradas+=chute
        cont+=1
    if len(erradas) == len(forca):
        print(f'A palavra é: {p}')
        para = input('Você foi enforcado...digite 0 para continuar ou 1 para sair: ')
        if para == 0: break




'''
    if certas == len(p):
            print(final)
            break
    print(f'Dica: começa com {p[0]} e termina com {p[-1]}')
    chute = input('\nChute uma letra: ').lower()

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
            print(forca[para])

                   
    if cont == 8:
        print('Fim de jogo')
        stop = input('Para recomeçar digite 1 ou para sair digite 0: ')
        if stop == 1:
            cont = 0
            para = 0
            chute = input('Chute uma letra: ').lower()
        else:
            break
'''
