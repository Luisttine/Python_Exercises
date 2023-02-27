def find_outlier(integers):
    odd, even = '', ''
    for i in integers:
        if i%2 == 0: even += str(i)
        else: odd += str(i)
    if len(odd) < len(even): return int(odd)
    else: return int(even)


print(find_outlier([160, 3, 1719, 19, 11, 13, -21]))
