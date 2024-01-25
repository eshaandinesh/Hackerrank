def merge_the_tools(string, k):
    # your code goes here
    t = []
    u = []
    for i in range(len(string)//k):
        t.append(string[0:k])
        string = string[k:]
        u.append('')
    #print(t)
    #print(u)
    for i in range(len(t)):
        for j in t[i]:
            if j not in u[i]:
                u[i] = u[i] + j
                
    for i in u:
        print(i)

