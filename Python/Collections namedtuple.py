# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import namedtuple
n = int(input())
tup = namedtuple('tup',input())
a = 0
for i in range(n):
    t1 = tup(*(input().split()))
    a += int(t1.MARKS)
print(a/n)
