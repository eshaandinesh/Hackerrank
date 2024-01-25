if __name__ == '__main__':
    x = []
    y = []
    z = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        x.append([name,score])
        z.append(score)
    a = min(z)
    while a in z:
        z.remove(a)
    for i in range(len(x)):
        if x[i][1] == min(z):
            y.append(x[i][0])
    y.sort()
    for i in y:
        print(i)
