#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'diagonalDifference' function below.
#
# The function is expected to return an INTEGER.
# The function accepts 2D_INTEGER_ARRAY arr as parameter.
#

def diagonalDifference(arr):
    # Write your code here
    x = 0
    y = 0
    for i in range(len(arr)):
        for j in range(len(arr)):
            if i==j:
                x+=arr[i][j]
                #print('x',arr[i][j])
            if i+j == len(arr)-1:
                y+=arr[i][j]
                #print('y',arr[i][j])
    #print(x,y)
    #print(abs(x-y))
    return abs(x-y)
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
