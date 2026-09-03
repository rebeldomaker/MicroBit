from microbit import *
import audio
import music
import random

timer = 0
age = 0
audio.play(Sound.HELLO)

def touching():
    for i in range(4):
        display.scroll(':3')
    sleep(800)
    display.clear()

def die():
    music.play(music.WAWAWAWAA)
    display.show(Image.SKULL)
    music.play(music.FUNERAL)
    sleep(1000)
    display.show(Image.GHOST)
    sleep(200)
    music.play(music.JUMP_DOWN)
    for i in range(10):
        display.scroll('Age: ')
        display.scroll(age)
    for i in range(4):
        display.scroll('DEAD! ')
    display.clear()

def lonely():
    music.play(music.WAWAWAWAA)
    display.show(Image.SAD)
    speech.say('hello')

def nap():
    for i in range(4):
        display.show(Image.ASLEEP)
        speech.say('z z z')
        sleep(200)
        display.clear()

def game1():  # left or right
    global timer  # Use the global timer variable
    choices = ['left', 'right']
    secret_choice = random.choice(choices)  # Randomly choose left or right
    display.scroll('Guess Left or Right!')

    # Wait for user input
    while True:
        if button_a.is_pressed():
            display.scroll('You chose Left!')
            if secret_choice == 'left':
                display.scroll('Win!')
                break
            else:
                display.scroll('You Lose!')
                break
        elif button_b.is_pressed():
            display.scroll('You chose Right!')
            if secret_choice == 'right':
                display.scroll('You Win!')
                break
            else:
                display.scroll('You Lose!')
                break

def game2():
    timer = 0
    game1()  # Call game1 when button A or B is pressed

while True:
    timer += 1
    if timer == 60:
        nap()
    elif timer == 120:
        lonely()
    elif pin_logo.is_touched():
        audio.play(Sound.HAPPY)
        touching()
    elif button_a.is_pressed() or button_b.is_pressed():
        game2()
    elif timer >= 200:  # Change to >= to trigger die() after 200
        die()
