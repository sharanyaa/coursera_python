def f(p,q):
    if p == False:
        return False
    elif q == False:
        return False
    else:
        return True

def f1 (p,q):
    return p and (not q)
    
def f2(p,q):    
    return q and p
    
def f3(p,q):    
    return (not p) or (not q)
    
def f4(p,q):    
    return not(p or q)

print f(True, True)
print f(True, False)
print f(False, True)
print f(False, False)
print 
print f1(True, True)
print f1(True, False)
print f1(False, True)
print f1(False, False)
print 
print f2(True, True)
print f2(True, False)
print f2(False, True)
print f2(False, False)
print 
print f3(True, True)
print f3(True, False)
print f3(False, True)
print f3(False, False)
print 
print f4(True, True)
print f4(True, False)
print f4(False, True)
print f4(False, False)
