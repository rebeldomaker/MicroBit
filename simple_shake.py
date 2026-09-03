from microbit import *
import random
import music

def shake():
    x = [Image.MEH, Image.SURPRISED, Image.SKULL, Image.SAD, Image.CONFUSED, Image.ANGRY, Image.ASLEEP, Image.GHOST]
    face_react = random.choice(x)
    display.show(face_react)
    music.play(music.FUNERAL)    
    display.clear()

while True:
    if button_a.is_pressed() and button_b.is_pressed():  # Check both buttons correctly
        display.show(Image.HAPPY)
        music.play(music.NYAN)
        display.clear()
    elif button_a.is_pressed():  # Use elif to avoid conflicts
        display.show(Image.YES)
        music.play(music.BA_DING)
        display.clear()
    elif button_b.is_pressed():
        display.show(Image.NO)
        music.play(music.WAWAWAWAA)
        display.clear()
    if accelerometer.was_gesture('shake'):
        shake()


# he accelerometer can sense other ‘gestures’ such as ‘freefall’ and whether it’s tilted left or right – try them out.
