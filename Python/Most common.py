#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


if __name__ == '__main__':
    s = input()
    x = []
    for i in s:
        x.append(i)
    x.sort()
    for k,v in Counter(x).most_common(3):
        print(k,v)
