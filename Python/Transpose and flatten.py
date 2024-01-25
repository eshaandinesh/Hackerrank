import numpy
a = int(input()[0])
x = numpy.array([input().split() for _ in range(a)],int)
print(x.transpose())
print (x.flatten())
