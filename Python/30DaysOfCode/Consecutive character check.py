#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    highest = 0
    x = 0
    n = int(input().strip())
    b = []
    while n>=1:
        if(n==1):
            b .append(1)
            n = 0
        else:
            b.append(n%2)
            n//=2
    b.reverse()
    for i in range(len(b)):
        if b[i] == 1:
            x+=1
        else:
            if x>= highest:
                highest = x
                x = 0
            else:
                x = 0
        if x>=highest:
            highest = x
    print(highest)
