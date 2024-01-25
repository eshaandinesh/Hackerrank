# Enter your code here. Read input from STDIN. Print output to STDOUT
n = int(input())
l = list(map(str,input().split()))
#for i in range(n):
#    print(l[i])
if all(int(l[i])>0 for i in range(n)):
    for j in range(n):
        rev = ''.join(reversed(l[j]))
        #print(rev)
        if(l[j]==rev): 
            print('True')
            exit()
print('False')
    #print(any(l[j] == ''.join(reversed(l[j])) for j in range(n)))
