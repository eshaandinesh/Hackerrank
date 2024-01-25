# Enter your code here. Read input from STDIN. Print output to STDOUT
import math

a = int(input())
b = int(input())
ang = round(math.degrees(math.atan(a/b)))
print(ang,chr(176),sep = '')
