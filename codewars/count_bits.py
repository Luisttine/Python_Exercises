def count_bits(n):
    x = ''
    while n > 0:
        x = x.append(n%2)
        n = n%2
        print('opa')
    return x
