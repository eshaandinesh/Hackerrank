# Enter your code here. Read input from STDIN. Print output to STDOUT
m = int(input())
a = set(map(int,input().split()))
m = int(input())
b = set(map(int,input().split()))
x = a.union(b)
y = a.intersection(b)
bruh = list(x.difference(y))
bruh.sort()
for i in bruh:
    print (i)
