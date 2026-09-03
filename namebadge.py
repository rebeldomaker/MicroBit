from microbit import *
import music as eminem

def slim_shady_theme():
    # A simple melody inspired by "The Real Slim Shady"
    melody = [
        'E4:4', 'E4:4', 'E4:4', 'E4:4',  # E notes
        'G4:4', 'G4:4', 'A4:4', 'G4:4',  # G and A notes
        'E4:4', 'E4:4', 'E4:4', 'E4:4',  # Repeat E notes
        'C4:4', 'C4:4', 'D4:4', 'B4:4',  # C and D notes
        'E4:4', 'E4:4', 'E4:4', 'E4:4'   # Repeat E notes
    ]
    eminem.play(melody)

display.show(Image.DUCK)
slim_shady_theme()  # Start playing the music
while True:
    display.scroll('Hi ! ')
    sleep(100)
    display.scroll('My Name is ')
    sleep(100)
    display.scroll('WHAT ? ! ')
    sleep(100)
    display.scroll('My Name is ')
    sleep(100)
    display.scroll('WHO ? ! ')
    sleep(100)
    display.scroll('My Name is ')
    sleep(100)
    display.scroll('Slim Shady ! ')
    sleep(100)
