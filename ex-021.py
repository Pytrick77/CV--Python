import pygame 

pygame.mixer.init()
pygame.mixer.music.load('porrada.mp3')
pygame.mixer.music.play()
input()

# Outra forma de resolver o exercício

import pygame

pygame.mixer.init()
pygame.init()
pygame.mixer.music.load('porrada.mp3')
pygame.mixer_music.play()
pygame.event.wait()