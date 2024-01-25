# Enter your code here. Read input from STDIN. Print output to STDOUT
import itertools
n = int(input())
l = list(map(str,input().split()))
k = int(input())
x = list(itertools.combinations(l,k))
b = len(x)
#print(b)
a = 0
for i in x:
    #print(i)
    if 'a' in i:
        a += 1
#print(a)
print(a/b)
