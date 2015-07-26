s = "1lll1l1l1l1ll1l111ll1l1ll1l1ll1ll111ll1ll1ll1l1ll1ll1ll1ll1lll1l1l1l1l1l1l1l1l1l1l1l1ll1lll1l111ll1l1l1l1l1"
i = 0
c=0
print len (s)
while (i < len(s) ):
    if(s[i] == "l"):
        c += 1
    i+=1
print c