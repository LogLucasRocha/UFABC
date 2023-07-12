import pygame
pygame.mixer.init()
pygame.mixer.music.load("asset/teste.mp3")
pygame.mixer.music.play()
while pygame.mixer.music.get_busy():
    continue