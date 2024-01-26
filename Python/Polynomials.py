# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
a = list(map(float,input().split()))
b = float(input())
print(numpy.polyval(a,b))
