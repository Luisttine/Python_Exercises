def spin_words(sentence):
    y = ''
    x = sentence.split()
    print(x)
    
    for i in x:
        if len(i) >= 5:
            y = y.join(reversed(i)) + ' '
        else:
            y = y.join(i) + ' '
        x = x[1:]
        print(x)

    return y
    
print(spin_words('Welcome to the jungle'))
