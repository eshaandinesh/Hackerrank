# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n,m = input().split()
n = int(n)
a = []
for i in range(n):
    a.append(list(map(float,input().split())))
a = numpy.array(a)
print(numpy.mean(a,axis = 1))
print(numpy.var(a, axis = 0))
print(round(numpy.std(a),11))
