import os
import time

def draw(side, offset, line):
    
    for i in range(line):
        print("")
    print(" "*(offset), end="")
    print("-"*((side*2)+2))

    for i in range(side):
        print(" "*(offset-1), end="")
        print("|", " "*(side*2), "|")
    
    print(" "*offset, end="")
    print("-"*((side*2)+2))

i=1
offset = 88
line = 15
flag=False
while True:
    os.system('clear')
    draw(i, offset, line)

    if line<=0:
        flag=True
    
    if line>=15:
        flag=False

    if flag:
        i-=2
        offset+=1
        line+=1
    else:
        i+=2
        offset-=1
        line -=1
    time.sleep(0.05)