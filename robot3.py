import RPi.GPIO as GPIO
import time
import sys
import Tkinter as tk
import random
from sensor import distance
from rrb2 import *


##################   INITIALIZATIONS     #################
GPIO.setmode(GPIO.BOARD)
rr = RRB2()

##########################################################


def init():
#    GPIO.setmode(GPIO.BOARD)
    print("Nothing")
#GPIO.setmode(GPIO.BOARD)

def wheel_cleanup():
    rr.set_motors(0, 0, 0, 0)                           # turn off all motors
    
def forward(tf):                                        # tf = 'time frame' or how the long the function will run for
    rr.set_motors(0.9, 0, 1, 0)                         # rr.setmotors(LEFT%, LEFT-DIRECTION[0=FORWARD, 1=REVERSE], RIGHT%, RIGHT-DIRECTION[0=FORWARD, 1=REVERSE)
    time.sleep(tf)
    rr.stop()

def reverse(tf):
    rr.set_motors(0.9, 1, 1, 1)
    time.sleep(tf)
    rr.stop()

def turn_left(tf):
    rr.set_motors(0, 0, 1, 0)
    time.sleep(tf)
    rr.stop()

def turn_right(tf):
    rr.set_motors(0.9, 0, 0, 0)
    time.sleep(tf)
    rr.stop()

def pivot_left(tf):
    rr.set_motors(0.9, 1, 1, 0)
    time.sleep(tf)
    rr.stop()

def pivot_right(tf):
    rr.set_motors(0.9, 0, 1, 1)
    time.sleep(tf)
    rr.stop()
'''
def key_input(event):
    init()
    print 'Key: ', event.char
    key_press = event.char
    sleep_time = 0.030
    
    if key_press.lower() == 'w':
        forward(sleep_time)
    elif key_press.lower() == 's':
        reverse(sleep_time)
    elif key_press.lower() == 'a':
        turn_left(sleep_time)
    elif key_press.lower() == 'd':
        turn_right(sleep_time)
    elif key_press.lower() == 'q':
        pivot_left(sleep_time)
    elif key_press.lower() == 'e':
        pivot_right(sleep_time)
    else:
        pass
    
    curDis = distance()
    print (curDis)
    if curDis < 12:
        reverse(2)

command = tk.Tk()
command.bind('<KeyPress>', key_input)
command.mainloop()
'''
def check_front():
    dist = distance()
    if dist < 12:
        print("Too close, ", dist)
        reverse(2)
        dist = distance()
        if dist < 12:
            print("Too close, ", dist)
            pivot_left(2)
            if dist < 12:
                print("Too close, giving up", dist)
                sys.exit()

def autonomy():
    tf = 0.030
    x = random.randrange(0,4)
    
    if x == 0:
        for y in range(30):
            check_front()
            forward(tf)    
    elif x == 1:
        for y in range(30):
            check_front()
            pivot_left(tf)
    elif x == 2:
        for y in range(30):
            check_front()
            turn_right(tf)
    elif x == 3:
        for y in range(30):
            check_front()
            turn_left(tf)

for z in range(10):
    autonomy()
  
