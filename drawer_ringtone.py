from microbit import *
import music

def main():
    for i in range(5):
        display.show(Image.SILLY)
        sleep(300)
        display.clear()

def counting():
    pass
    # todo count how many times your drawer has been opened by introducing a variable into the program. when a button is pressed, it will scroll to show the variable which will contain an integer number

while True:
    if display.read_light_level() > 1:
        display.show(Image.SURPRISED)
        music.play(music.BA_DING)
        sleep(200)
        display.clear()
        sleep(100)
        main()
        music.play(music.NYAN)
    else:
        display.clear()
        
"""
while True:
    if display.read_light_level() > 70:
        display.show(Image(
        "90909:"
        "09990:"
        "99999:"
        "09990:"
        "90909"))
        music.play(music.RINGTONE)
    else:
        display.clear()
"""