# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = int(input())
a = []
for i in range(n):
    a.append(list(map(float,input().split())))
print(round(numpy.linalg.det(a),2))
