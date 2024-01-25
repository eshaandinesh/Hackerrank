# Enter your code here. Read input from STDIN. Print output to STDOUT
l = input()
a = []
b = []
c = []
d = []
for i in l:
    if i.islower():
        a.append(i)
        a.sort()
    elif i.isupper():
        b.append(i)
        b.sort()
    elif int(i)%2 != 0:
        c.append(i)
        c.sort()
    else:
        d.append(i)
        d.sort()
#a.sort()
#b.sort()
#c.sort()
#d.sort()
a.extend(b)
a.extend(c)
a.extend(d)
for i in range(len(l)):
    print(a[i],end = '')
