cube = lambda x: x**3 # complete the lambda function 

def fibonacci(n):
    # return a list of fibonacci numbers
    if n == 0: return []
    if n == 1: return [0]
    a = 0
    b = 1
    l = [a,b]
    while(len(l)<=n-1):
        c = a+b
        l.append(c)
        a = b
        b = c
    return l

