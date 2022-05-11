def balanced(expression):
    #your code goes here
    stack = []
    cont = 0
    for i in expression:
        if i == "(":
            stack.insert(0, i)
        for x in expression:
            if x == ")":
                stack.pop()
    return True if len(stack) == 0 else False
        
print(balanced(input()))

def balanced(expression):
    #your code goes here
    stack = []
    expression = list(expression)
    cont = 0
    if expression[0] == ")": return False
    for i in expression:
        cont += 1
        expression2 = expression[cont:]
        if i == "(":
            stack.insert(0, i)
        else: continue
        for x in expression2:
            if x == ")":
                if stack == False:
                    return False
                stack.pop()
                expression.pop()
                break
            else: return False
        cont = 0
    if stack == False: return True
    return True if len(stack) == 0 else False
        
print(balanced(input()))

