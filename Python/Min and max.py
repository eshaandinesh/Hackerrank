# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m = input().split()
n = int(n)
a = []
for i in range(n):
    a.append(list(map(int,input().split())))
a = numpy.array(a)
print(numpy.max(numpy.min(a,axis = 1)))
