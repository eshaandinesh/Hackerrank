# Enter your code here. Read input from STDIN. Print output to STDOUT
n,m  = input().split()
h = 0
x = list(map(int,input().split()))
a = set(map(int,input().split()))
b = set(map(int,input().split()))
for i in x:
    if i in a: h+=1
    if i in b: h-=1
print(h)
