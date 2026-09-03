from microbit import *
import music

while True:
    if microphone.current_event() == SoundEvent.LOUD:
        display.show(Image.SURPRISED)
        sleep(850)
        display.show(Image.ANGRY)
        music.play(music.WAWAWAWAA)
        sleep(1300)
        display.show(Image.SAD)
        sleep(1200)
#         display.clear()
    elif microphone.current_event() == SoundEvent.QUIET:
        display.show(Image.ASLEEP)
