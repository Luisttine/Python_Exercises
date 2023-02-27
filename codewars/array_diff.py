def array_diff(a, b):
    final = []
    for i in a:
        if i in b: continue
        else: final.append(i)
    return final

print(array_diff([1,2,3], [1]))
