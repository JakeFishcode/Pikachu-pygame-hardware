import time
import pygame
file='try.mp3'
pygame.mixer.init()
print("play")
track = pygame.mixer.music.load(file)
print('over')
pygame.mixer.music.play()

time.sleep(10)
pygame.mixer.music.stop()
