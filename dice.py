from microbit import *
import random
import music as mp3

while True:
    if accelerometer.was_gesture('shake'):
        display.show(random.randint(1, 6))
        sleep(100)
        mp3.play(mp3.POWER_UP)
        sleep(500)
        display.clear()

