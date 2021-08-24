def solution(s):
    lista = []
    i = len(s)
    x = '_'
    while i != 0:
        if len(s)%2 != 0:
            lista.append(s[:1] + s[1:2])
            s = s[2:]    
        else:
            lista.append(s[:1] + s[1:2])
            s = s[2:]
        i = i - 2
        
    pass
    return lista

print(solution('asdfasdfx'))
