def alphabet_position(text):
    alfabeto = 'abcdefghijklmnopqrstuvwxyz'
    text = text.lower()
    print(text)
    f = ''
    for i in text:
        if i in alfabeto:
            x = str(alfabeto.find(i)+1)
            f = f + x + ' ' 
    pass
    return f[:-1]