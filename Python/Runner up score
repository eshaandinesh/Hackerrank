if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    x = list(arr)
    f = x[0]
    s = -1000
    for i in range(n):
        if(x[i]>f):
            f = x[i]
    for j in range(n):
        if(x[j]>s and x[j]<f):
            s = x[j]
    print(s)
