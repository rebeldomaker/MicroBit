from microbit import *
import music

def intro():
    music.play(music.PYTHON)
    display.scroll("Welcome !!! ")
    
def herd():
    display.scroll("I HERD U LIEK DUCKS?")
    display.show(Image.SAD)
    sleep(1500)


def heart():
    for i in range(5):
        display.show(Image.HEART)
        sleep(400)
        display.show(Image.HEART_SMALL)
        sleep(400)

def duck_loop():
    display.show(Image.DUCK)
    sleep(1500)
    display.show(Image.HAPPY)
    sleep(1500)
    display.clear()
    sleep(1000)

intro()
while True:
    herd()
    display.scroll("I", loop=False)
    heart()
    duck_loop()