if __name__ == '__main__':
    l = s = 20000000000000
    nlist = []
    x = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        nlist.append([name,score])
    for i in range(len(nlist)):
        if l>= nlist[i][1]:
            l = nlist[i][1]
    for i in range(len(nlist)):
        if s>=nlist[i][1] and nlist[i][1]>l:
            s = nlist[i][1]
    for i in range(len(nlist)):
        if s == nlist[i][1]:
            x.append(nlist[i][0])
    x.sort()
    for i in range(len(x)):
        print(x[i])
