def fun(s):
    if s.count('@')!=1: return False
    if s.count('.')!=1: return False
    l = s.split('@')
    u = l[0]
    l = l[1].split('.')
    w = l[0]
    e = l[1]
    if(len(u)==0 or len(w)==0 or len(e)==0 or len(e)>3): return False
    if(w.isalnum() and e.isalpha()):
        if(u.isalnum()):
            return True
        else:
            for i in u:
                if(i.isalnum()== False and i not in ['-','_']): return False
    else:
        return False
    return True

