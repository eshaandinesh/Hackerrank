# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy 
numpy.set_printoptions(legacy='1.13')
n = numpy.array(list(map(float,input().split())))
print(numpy.floor(n))
print(numpy.ceil(n))
print(numpy.rint(n))
