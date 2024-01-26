# Enter your code here. Read input from STDIN. Print output to STDOUT
import numpy
numpy.set_printoptions(legacy = '1.13')
x = list(map(int,input().split()))
print(numpy.eye(x[0],x[1],k=0))
