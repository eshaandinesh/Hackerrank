def wrapper(f):
    def fun(l):
        li = []
        for i in l:
            li.append("+91 "+i[-10:-5]+" "+i[-5:])
        f(li)
    return fun

