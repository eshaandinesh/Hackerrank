# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
n = list(map(int, input().split()))
arr = numpy.array(n)
print(numpy.zeros(arr,dtype = numpy.int))
print(numpy.ones(arr,dtype = numpy.int))
