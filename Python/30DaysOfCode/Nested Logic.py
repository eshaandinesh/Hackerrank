# Enter your code here. Read input from STDIN. Print output to STDOUT
a = list(map(int,input().split()))
b = list(map(int,input().split()))

if b[2] >= a[2]:
    if(b[2]>a[2]): print(0)
    elif(b[1]>=a[1]):
        if(b[1]>a[1]): print(0)
        elif(b[0]>=a[0]):
            print(0)
        else:
            print(15*(a[0]-b[0]))
    else:
        print(500*(a[1]-b[1]))
else:
    print(10000)
