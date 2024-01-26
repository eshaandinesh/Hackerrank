# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
x = list(map(int,input().split()))
a = numpy.array([input().split() for i in range(x[0])],int)
b = numpy.array([input().split() for i in range(x[0])],int)

print(numpy.add(a, b) )
print(numpy.subtract(a, b) )
print(numpy.multiply(a, b) )
print(numpy.floor_divide(a, b) )
print(numpy.mod(a, b) )
print(numpy.power(a, b))
