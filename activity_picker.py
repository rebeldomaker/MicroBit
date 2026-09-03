from microbit import *
import random

def chores():
    x = random.randint(1, 10)
    if x == 1:
        display.scroll('Shower')
    elif x == 2:
        display.scroll('Dishes')
    elif x == 3:
        display.scroll('Throw out trash')
    elif x == 4:
        display.scroll('Clean WC')
    elif x == 5:
        display.scroll('Clean PC desk')
    elif x == 6:
        display.scroll('Vacuum')
    elif x == 7:
        display.scroll('Gardening')
    elif x == 8:
        display.scroll('Make the bed')
    elif x == 9:
        display.scroll('Laundry')
    else:
        x == 10
        display.scroll('Homework')

while True:
    if button_a.is_pressed() or button_b.is_pressed():
        chores()
        