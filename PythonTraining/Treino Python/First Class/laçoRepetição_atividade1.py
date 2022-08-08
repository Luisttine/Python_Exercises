'''
CÓDIGO GRANDE DEMAIS POREM FUNCIONAL

nomes = []
tam = []

for i in range(7):
    cont = 0
    nome, nomef = input('Digite um nome: '), ''

    if len(nome)%2 != 0:
        nome = nome[::-1]
        for x in nome:
            if x == 'p': nomef+='X'
            else: nomef+=x
        print(nomef,'\n')
    if len(nome)%2 == 0:
        for x in nome:
            if x == 'p': nomef+='X'
            else: nomef+=x
        nomef = nomef.upper()
        print(nomef,'\n')

    tam.append(len(nomef))
    nomes.append(nomef)

maximo = max(tam)
for y in nomes:
    if len(y) < maximo:
        y+= (maximo-len(y))*'Z'
    print(y)
'''

'''
TENTAVIA DE CÓDIGO ENXUTO


nomes = []
tam = []

for i in range(7):
    nome = input('Digite um nome: ')

    if len(nome)%2 != 0:
        nome = nome[::-1]
        nome.replace('p', 'X')
        print(nome,'\n')
            
    if len(nome)%2 == 0:
        nome.replace('p', 'X')
        nome = nome.upper()
        print(nome,'\n')

    tam.append(len(nome))
    nomes.append(nome)

maximo = max(tam)
for y in nomes:
    if len(y) < maximo: y+= (maximo-len(y))*'Z'
    print(y)
'''
def nomes_sub(nome, self):
    nomes = []
    tam = []

    for i in range(7):
        if len(nome)%2 != 0:
            return nome[::-1].replace('p', 'X')
                
        if len(nome)%2 == 0:
            return nome.replace('p', 'X').upper()
            nome.replace('p', 'X')

        tam.append(len(nome)).self
        nomes.append(nome).self

def tamanho(nomes.self, tam.self):
    maximo = max(tam.self)
    for y in nomes.self:
        return y+= (maximo-len(y))*'Z' if len(y) < maximo

print(nomes_sub())
