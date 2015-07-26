# CodeSkulptor runs Python programs in your browser.
# Click the upper left button to run this simple demo.

# CodeSkulptor runs in Chrome 18+, Firefox 11+, and Safari 6+.
# Some features may work in other browsers, but do not expect
# full functionality.  It does NOT run in Internet Explorer.

import simplegui
import time
t = time.time()
#t = 30758400
print str(t) + "sec"
t= t/60
print str(t) + "min"
t=t/60
print str(t) + "hr"
t=t/24
print str(t) + "d"
t=t/356
print str(t) + "y"
print str(2015 - t)