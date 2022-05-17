##CÓDIGO Q TENTEI FAZER - N PASSOU NO ULTIMO TESTE
def balanced(expression):
    #your code goes here
    stack = []
    cont = 1
    expression = list(expression)
    if expression[0] == ")": return False
    for i in expression:
        if i == "(":
            stack.insert(0, i)
        else: continue
        for x in expression[cont:]:
            cont += 1
            if x == ")":
                if stack == False:
                    return False
                stack.pop()
                break
            else: continue
    if stack == False: return True
    return True if len(stack) == 0 else False
        
print(balanced(input()))

##CÓDIGO CORRETO

def balanced(expression):
       stack = []
       opening = set('(')
       closing = set(')')
       pair = {')' : '('}
       for i in expression :
           if i in opening :
               stack.append(i)
           if i in closing :
               if not stack :
                   return False
               elif stack.pop() != pair[i] :
                   return False
               else :
                   continue
       if not stack :
           return True
       else :
           return False
        
print(balanced(input()))

        
