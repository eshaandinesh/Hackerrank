# Enter your code here. Read input from STDIN. Print output to STDOUT
n,x = input().split()
l = []
for i in range(int(x)):
    l.append(list(map(float,input().split())))
for i in list(zip(*l)):
    print(sum(i)/int(x))
