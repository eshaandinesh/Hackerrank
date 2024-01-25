if __name__ == '__main__':
    N = int(input())
    l = []
    temp = ''
    for i in range(N):
        x = input()
        if 'insert' in x:
            temp,pos,inte = x.split()
            pos = int(pos)
            inte = int(inte)
            l.insert(pos,inte)
        if 'print' in x:
            print(l)
        if 'remove' in x:
            temp,inte = x.split()
            inte = int(inte)
            l.remove(inte)
        if 'append' in x:
            temp,inte = x.split()
            inte = int(inte)
            l.append(inte)
        if 'sort' in x:
            l.sort()
        if 'pop' in x:
            l.pop()
        if 'reverse' in x:
            l.reverse()
