'''
Exercício 021
Algoritmo para abrir e reproduzir um áudio do tipo MP3
'''

import pygame
pygame.init()

pygame.mixer.music.load('Exercício 021 - Música.mp3')
pygame.mixer.music.play()
pygame.mixer.music.set_volume(0.04)

input()
pygame.event.wait()
