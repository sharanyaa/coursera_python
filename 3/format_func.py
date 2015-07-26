def format(time):
    
#    print time
    a1 = 0
    b1 = 0
    c1 = 0
    d1 = 0
    sec = 0
    
    d1 = time % 10
    time //= 10
    
    a1 = time // 60
    sec = time % 60
    c1 = sec % 10
    b1 = sec // 10
#    print str(a1)+"min "+str(b1)+str(c1)+"sec "+str(d1)+ "msec"
#    print str(a1) + ":" + str(b1) + str(c1) + "." + str(d1) + "\n"
#    a = str(a1)
#    d = str(d1)
#    c = str(c1)
#    b = str(b1)
#    t = a + ":" + b + c + "." + d + "\n"
    return str(a1) + ":" + str(b1) + str(c1) + "." + str(d1)
    pass

###################################################
# Test code for the format function
# Note that function should always return a string with 
# six characters
print format(0) #= 0:00.0
print format(11) #= 0:01.1
print format(321) #= 0:32.1
print format(613) #= 1:01.3
print format(0)
print format(7)
print format(17)
print format(60)
print format(63)
print format(214)
print format(599)
print format(600)
print format(602)
print format(667)
print format(1325)
print format(4567)
print format(5999)

###################################################
# Output from test

#0:00.0
#0:00.7
#0:01.7
#0:06.0
#0:06.3
#0:21.4
#0:59.9
#1:00.0
#1:00.2
#1:06.7
#2:12.5
#7:36.7
#9:59.9

