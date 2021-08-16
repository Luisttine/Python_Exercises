def count_bits(n):
    x = 0

    for i in str(n):
        x = n%2
        n = n/2
        x = x + int(i)
    return  x
