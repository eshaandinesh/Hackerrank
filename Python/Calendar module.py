# Enter your code here. Read input from STDIN. Print output to STDOUT
import calendar
t = list(map(int,input().split()))
print((list(calendar.day_name)[calendar.weekday(t[2],t[0],t[1])]).upper())
