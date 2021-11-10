import pygame
from pygame.draw import *

pygame.init()
screen = pygame.display.set_mode((600, 550)) #ширина высота
clock = pygame.time.Clock()
FPS = 30 #частота кадров
rect(screen, (127, 255, 210), (0, 0, 599, 599))
circle(screen, (0, 0, 0), (300, 250), 101)
circle(screen, (255, 255, 0), (300, 250), 100)
circle(screen, (0, 128, 0), (260, 220), 18)
circle(screen, (0, 128, 0), (340, 220), 18)
circle(screen, (0, 0, 0), (260, 220), 8)
circle(screen, (0, 0, 0), (340, 220), 8)
rect(screen, (220, 20, 60), (250, 280, 100, 25))
polygon(screen, (139, 69, 19), [(300, 200), (370, 140), (370, 155), (300, 215)])
rect(screen, (139, 69, 19), (200, 180, 80, 12))
pygame.display.update()
finished = False
while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
pygame.quit()




