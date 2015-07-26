# Mystery computation in Python
# Takes input n and computes output named result

import simplegui

# global state

n= int(raw_input("Enter the beginning number: "))
max=0
# timer callback

def update():
    global n, max
    if n > 1:
        if n%2 == 0: # if n is even
            n = n/2
            print n
        else:
            n = 3*n+1
            print n
        if max<=n:
            max=n
            print "max" + str(max)
    else:
        timer.stop()
    print "max" + str(max)
# register event handlers

timer = simplegui.create_timer(1, update)

# start program
timer.start()



