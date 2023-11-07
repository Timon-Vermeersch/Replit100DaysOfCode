import pygame
import time
import threading 

#establish 

def play_music(mp3file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file)
    pygame.mixer.music.play()

#playa 
state = ""
print("1 for play\n2 for stop\nq for quit: ")
while True:
    state = input("input?: ")
    if state == "1":
        play_music('Cynthia.mp3')
        print("Playing{mp3file}")
    elif state == "2":
        print("stopping the bitch")
        pygame.mixer.music.stop()
    elif state == "q":
        print("exiting this bitch")
        break
