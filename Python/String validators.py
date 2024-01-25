if __name__ == '__main__':
    s = input()
    a = 0
    b = 0
    c = 0
    d = 0
    e = 0
    for i in range(len(s)):
        if(s[i].isalnum()):
            a = 1
        if(s[i].isalpha()):
            b = 1
        if(s[i].isdigit()):
            c = 1  
        if(s[i].islower()):
            d = 1  
        if(s[i].isupper()):
            e = 1 
    print("True" if a ==1 else "False")
    print("True" if b ==1 else "False")
    print("True" if c ==1 else "False")
    print("True" if d ==1 else "False")
    print("True" if e ==1 else "False")
    
