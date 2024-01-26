# Enter your code here. Read input from STDIN. Print output to STDOUT
a = set(map(int,input().split()))
n = int(input())
c = 0
for i in range(n):
    x = set(map(int,input().split()))
    if(a.issuperset(x)):
        c+=1
if(c==n):
    print('True')
else:
    print('False')
