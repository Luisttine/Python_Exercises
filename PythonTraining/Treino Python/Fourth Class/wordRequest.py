import requests
from bs4 import BeautifulSoup

palavra = ' ' + input('Digite uma palavra em inglês para achar páginas: ') + ' '
cont_pags = int(input('Quantas páginas você deseja procurar: '))
cont = 0

open(str(cont_pags)+'_'+palavra+'.txt', 'a', encoding="utf-8").close()


while cont != cont_pags:

    aleatorio = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    url1 = aleatorio.text
    soup = BeautifulSoup(url1, "html.parser")
    x = soup.title.string    

    if palavra in url1:
        
        file = open(str(cont_pags)+'_'+palavra+'.txt', 'a', encoding="utf-8")
        file.write(x+'\n')
        file.close()
        cont+=1
        print(x, '\n', aleatorio.url)
    
    else: print('Tem nada amigao')