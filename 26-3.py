import pygame
import time
import threading

def play_music(mp3file):
    pygame.mixer.init()
    pygame.mixer.music.load(mp3file)
    pygame.mixer.music.play()

def wait_for_input():
    input()
    pygame.mixer.music.stop()

music_thread = threading.Thread(target=play_music, args=('Cynthia.mp3',))
input_thread = threading.Thread(target=wait_for_input)

music_thread.start()
input_thread.start()