# -*- coding: utf-8 -*-
#Lista IV
#Atividade 1

import random

x = random.sample(range(100), 10)
x1 = x2 = x[0]

for i in x[1:]:
    if i > x1:
        x1 = i 
    if i < x2:
        x2 = i

print(f'{x1} é maior')
print(f'{x2} é menor')

#Atividade 2

from random import sample

k = sample(range(100), 20)
par = []
impar = []

for i in k:
    if i % 2 == 0:
         par.append(i)
    else:
        impar.append(i)

print(f'Essa é a lista {k}')
print(f'Esses são os números pares {par}')
print(f'Esses são os ímpares {impar}')

#Atividade 3

from random import sample

vetor1 = sample(range(100), 10)
vetor2 = sample(range(100), 10)
vetor = []

for i in zip(vetor1, vetor2):
    vetor.extend(list(i))

        
print(f'Primeiro vetor: {vetor1}')    
print(f'Segundo vetor: {vetor2}')
print(f'Vetor intercalado: {vetor}')

#Atividade 4

a = '''The Python Software Foundation and the global
   Python community  welcome  and  encourage participation
   by everyone.  Our  community is  based  on mutual respect,
   tolerance, and encouragement, and we are working to help each
   other live up to  these  principles.  We  want our  community
   to  be  more  diverse: whoever you  are,  and whatever  your
   background, we welcome  you.'''.lower()
lista = a.replace(',', '')
lista = a.replace(':', '')
lista = a.replace('.','')
lista = a.split()
resul = []

for i in lista:    
    if i[0] in 'python' or i[-1] in 'python':
        resul.append(i)

print(resul)

#Atividade 5

a = '''The Python Software Foundation and the global
   Python community  welcome  and  encourage participation
   by everyone.  Our  community is  based  on mutual respect,
   tolerance, and encouragement, and we are working to help each
   other live up to  these  principles.  We  want our  community
   to  be  more  diverse: whoever you  are,  and whatever  your
   background, we welcome  you.'''.lower()
lista = a.replace(',', '')
lista = a.replace(':', '')
lista = a.replace('.','')
lista = a.split()
resul = []

def py(x):
    for i in x:
        if i in 'python':
            return True
    return False
for x in lista:
    if py(x) and len(x) > 4:
        resul.append(x)

print(resul)
print(len(resul))
