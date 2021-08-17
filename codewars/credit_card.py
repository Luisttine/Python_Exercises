def maskify(cc):
    ccf = cc[-4:]
    cc = cc[:-4]
    x = ''
    
    for i in cc:
        x = x + '#'
    return x + ccf


print(maskify('testando a codificacao'))
        
