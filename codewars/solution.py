def solution(s):
    lista = []
    z = '_'
    for i in s:
        if not s[:1]:
            lista.append(s[:1] + z)
        else:
            lista.append(s[:1] + s[1:2])
        s = s[2:]
    if len(s)%2 != 0:
        lista = lista[-2] + x
    pass
    return lista[:5]


print(solution('abc'))
