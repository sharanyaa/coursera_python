# Simple interactive application

import simplegui

# Define globals.

message = "Welcome!"
count = 0

# Define event handlers.

def button_handler():
    """Count number of button presses."""
    global count
    count += 1
    print message,"  You have clicked", count, "times."
    
def input_handler(text):
    """Get text to be displayed."""
    global message, count
    message = text
    count=0

# Create frame and register event handlers.

frame = simplegui.create_frame("Home", 100, 200)
frame.add_button("Click me", button_handler)
frame.add_input("New message:", input_handler, 100)

# Start frame.

frame.start()