import pygame

pygame.init()

pygame.mixer.music.load('sonic.mp3')
pygame.mixer.music.play()
pygame.event.wait()