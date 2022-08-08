def solution(n):
    r = ""
    while n != 0:
        if n%1000 == 0:
            n -= 1000
            r += "M"
        elif n%500 == 0:
            n -= 500
            r += "D"
        elif n%100 == 0:
            n -= 100
            r += "C"
        elif n%50 == 0:
            n -= 50
            r += "L"
        elif n%10 == 0:
            n -= 10
            r += "X"
        elif n%5 == 0:
            n -= 5
            r += "V"
        elif n%1 == 0:
            n -= 1
            r += "I"
    