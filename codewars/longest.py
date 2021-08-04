def longest(a1, a2):
    l = ''
    x = a1 + a2
    x = sorted(x)
    
    for i in x:
        if i in l:
            continue
        else:
            l = l+i
    return l