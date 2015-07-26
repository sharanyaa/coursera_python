slow = 1000
fast = 1
year = 1
while fast < slow:
    slow += slow
    fast += fast
    year += 1
    slow -= 0.4*slow
    fast -= 0.3*fast
    print year, slow, fast

if(fast>=slow):
    print year
    