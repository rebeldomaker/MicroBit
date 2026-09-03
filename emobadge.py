from microbit import *
import music as mu

def func():
    pass

"""display.scroll('UWU')
while True:
    if button_a.is_pressed():
        display.show(Image.YES)
        sleep(1000)
        display.clear()
    elif button_b.is_pressed():
        display.show(Image.NO)
        sleep(1000)
        display.clear()
    else:
        display.scroll('L O L')"""

display.show(Image.SILLY)
sleep(1500)
display.clear()
while True:
    if button_a.is_pressed():
#        mu.play(mu.BA_DING)
        for i in range(8):
            display.show(Image.YES)
            sleep(400)
            display.clear()
            sleep(400)
    if button_b.is_pressed():
#        mu.play(mu.WAWAWAWAA)
        for i in range(8):
            display.show(Image.NO)
            sleep(200)
            display.clear()
            sleep(200)
























