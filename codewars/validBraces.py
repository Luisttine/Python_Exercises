def valid_braces(string):
    ope = []
    clo = []

    for i in string:
        if i in ["{", "[", "("]:
            ope.append(i)
        elif i in ["}", "]", ")"]:
            clo.append(i)
    x = 0
    while x < len(string)/2
    
print(valid_braces("{}()[]"))
