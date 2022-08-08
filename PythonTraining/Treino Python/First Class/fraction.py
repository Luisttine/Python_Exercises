from fractions import Fraction
from functools import reduce

def product(fracs):
    for i in range(fracs):
        t = reduce(lambda x, y : x+y, [1,2,3,4])
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    for _ in range(int(input())):
        fracs.append(Fraction(*map(int, input().split())))
    result = product(fracs)
    print(*result)
