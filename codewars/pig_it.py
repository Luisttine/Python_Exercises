def pig_it(text):
    text = text.split(' ')
    x = 0
    text2 = ""
    for i in text:
        if i.isalpha():
            i = i[1:] + i[0] + 'ay'
            text2 = text2+(i)+' '
            x = x+1
        else:
            text2 = text2+(i)+' '
    return text2[:-1]

print(pig_it('Pig latin is, cool'))
        

        
