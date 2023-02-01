""" This program tries to create a square in the center of screen and the gradually increase its dimensions in all directions. After reaching a certain point, the squate starts reducing its size. Values have been Defined Statically, and might not be the best way to design this program.
"""

import os
import time


def draw(side, offset, line):

    # Number of Lines to skip from the Top to start making the drawing
    for i in range(line):
        print("")
    
    #Skips number of places to start drawing the square in a line
    print(" "*(offset), end="")
    
    # Draws the Top line
    print("-"*((side*2)+2))

    # Draws the middle portion of the Square after leaving same number od spaces
    for i in range(side):
        print(" "*(offset-1), end="")
        print("|", " "*(side*2), "|")

    #Leaves the spaces for last line
    print(" "*offset, end="")

    # Finally, draws the bottom line of the square
    print("-"*((side*2)+2))


side = 1 # Length of square
offset = 88 # Space to leave from starting
line = 15 # Lines to leave from top
flag = False # Flag tells whether to inflate or deflate the Square.

while True:

    # Clear everthing from the Terminal screen
    os.system('clear')

    draw(side, offset, line)

    # Turn Flag on as soon as square reaches its max Size
    if line <= 0:
        flag = True

    # Turb off the Flag as soon as it reaches Max Size
    if line >= 15:
        flag = False

    # Flag : True -> Deflate the Square
    if flag:
        side -= 2
        offset += 1
        line += 1

    # Flag : False -> Inflate the Square
    else:
        side += 2
        offset -= 1
        line -= 1
    
    # To slow down the speed and give it a nice animated effect
    time.sleep(0.05)
