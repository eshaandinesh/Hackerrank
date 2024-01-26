#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    h,m,se,t = re.search(r'(\d{2}):(\d{2}):(\d{2})(AM|PM)',s).groups()
    if(t=='AM' and h =='12'):
        return (f'00:{m}:{se}')
    elif(t=='AM'):
        return s[0:-2]
    if(t=='PM' and h == '12'):
        return s[0:-2]
    if(t=='PM'):
        return (f'{int(h)+12}:{m}:{se}')
        
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
