'''
JEIT PÉSSIMO DE PROGRAMAR DO LUIZINHO

import re
s = input()

vowel = 'aeiou'
conss = 'qwrtypsdfghjklzxcvbnm'
cont = 0
passou = ''

for i in s:
    if i in vowel or i in vowel.upper():
        if s[cont-1] in conss or s[cont-1] in conss.upper():
            if s[cont+1:] in conss or s[cont-+1] in conss.upper():
                passou+=i
            else: passou+=i
    else:
        if passou != '' and len(passou) >= 2:
            print(passou)
            passou = ''

    cont+=1
'''

'''
JEITO CERTO DE FAZER COM REGEX
'''
import re

s = input()
#match = map(lambda x: x.group re.finditer("[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU]", s)
match = map(lambda x: x.group(),re.finditer("[^aeiouAEIOU]([aeiouAEIOU]{2,})[^aeiouAEIOU]", s))

if not match: print(-1)
else:
    for i in match: print(i)
