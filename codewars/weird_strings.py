def to_weird_case(words):
    x, f = 0, ''
    for i in words:
        if i == ' ':
            f += i
            x=0
        elif x%2 == 0:
            f += i.upper()
            x+=1
        else:
            f += i.lower()
            x+=1
    return f

print(to_weird_case("This is a Test"))
