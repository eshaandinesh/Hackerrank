# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
x = ''
y = ''
dict = {}
for i in range(t):
    x,y = input().split()
    y = int(y)
    dict[x] = y
while t>0:
    try:
        p = input()
        if(p in dict):
            print(p,"=",dict[p],sep='')
        else:
            print("Not found")
    except EOFError:
        break
