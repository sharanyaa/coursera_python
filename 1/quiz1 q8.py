import math
# 5 sides, each of length 7 inches, has area 84.3033926289 
def area(n,s):
    a=(n*s*s)
    print a
    
    b=math.pi/n
    print b
    
    c=4*math.tan(b)
    print c
    
    d=a/c
    print d
    
    return d

print area(5,7)
print area(7,3)