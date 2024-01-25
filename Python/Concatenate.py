import numpy
x = list(map(int,input().split()))
a = numpy.array([input().split() for _ in range(x[0])],int)
b = numpy.array([input().split() for _ in range(x[1])],int)
print(numpy.concatenate((a,b)))
