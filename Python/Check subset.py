# Enter your code here. Read input from STDIN. Print output to STDOUT
t = int(input())
for i in range(t):
    x = int(input())
    a = set(map(int, input().split()))
    y = int(input())
    b = set(map(int, input().split()))
    if(a.issubset(b)):
        print('True')
    else:
        print('False')
