def print_rangoli(size):
    x = []
    p = []
    j = 0
    for i in range(size):
        for j in range(ord(chr(96+size)),ord(chr(96+size))-i-1,-1):
            p.append(chr(j))
        for j in range(j+1,ord(chr(96+size))+1):
            p.append(chr(j))
        print('-'.join(p).center(size*4-3,'-'))
        x.append(p)
        p = []
    x.pop()
    x.reverse()
    for i in range(len(x)):
        for k in range(len(x[i])):
            p.append(x[i][k])
        print('-'.join(p).center(size*4-3,'-'))
        p = []
        

