def square_digits(num):
    f = ''
    for i in str(num):
        i = int(i)
        x = i**2
        if i == 0:
            f = f + '0'
        else:
            f = f + str(x) 
    pass        
    return int(f)