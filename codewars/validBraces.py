def valid_braces(string):
    ope = []
    clo = []

    for i in string:
        if i in ["{", "[", "("]:
            ope.append(i)
        elif i in ["}", "]", ")"]:
            clo.append(i)
    x = 0
    count = 0
    while x < len(string)/2:
        if ope[x]+clo[x] in ["{}", "[]", "()"]:
            count = count+1
        else:
            print("PUTAAA")
        x = x+1
    if count != 0:
        return True
    else:
        return False
    
print(valid_braces("{}()[]"))
