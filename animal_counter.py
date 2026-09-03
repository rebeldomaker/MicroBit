from microbit import *
import music

x = 0
y = 0

# todo play song when you have reached a target number

def button_a_func():
    global x
    x += 1
    music.play(music.BA_DING)
    display.scroll('birds: ')
    display.scroll(x)
    display.show(Image.DUCK)
    sleep(2500)
    display.clear()

def button_b_func():
    global y
    y += 1
    music.play(music.BA_DING)
    display.scroll('mammals: ')
    display.scroll(y)
    display.show(Image.GIRAFFE)
    sleep(2500)
    display.clear()

def heartbeat():
    music.play(music.BA_DING)
    display.scroll('target reached !!! ')
    for i in range(5):
        display.show(Image.HEART)
        sleep(200)
        display.show(Image.HEART_SMALL)
    music.play(music.NYAN)
    display.clear()
    
while True:  # Use a loop to continuously check for button presses
    if button_a.is_pressed():
        button_a_func()
    elif button_b.is_pressed():
        button_b_func()
    elif button_a.is_pressed() and button_b.is_pressed(): # todo if both buttons are pressed, combine total animals counted
        music.play(music.BA_DING)
        display.scroll('total animals: ')
        display.scroll(x + y) # todo do they need type to be converted to int? research it
        display.show(Image.HAPPY)
        sleep(2000)
        display(clear)
    elif x + y == 10:
        heartbeat() # todo make it only play this once, not loop forever. at its current state, it only breaks out of this loop once you count another animal and reach 11 total