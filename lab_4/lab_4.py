import random
from random import randint
import pygame
from pygame.draw import circle
pygame.init()

#screen
FPS = 50
screen = pygame.display.set_mode((900, 500))

#create colors
color_1 = (221, 160, 221)
color_2 = (199, 20, 133)
color_3 = (255, 165, 0)
color_4 = (255, 255, 50)
color_5 = (255, 180, 190)
color_6 = (185, 85, 210)
colors = [color_1, color_2, color_3, color_4, color_5, color_6]
color_screen = (35, 0, 90)

#variable for ball
balls = []
def new_ball():
    x = randint(100, 800)
    y = randint(100, 400)
    r = randint(30, 50)
    color = colors[randint(0, 5)]
    dx = randint(-9, 9)
    dy = randint(-9, 9)
    newball = []
    newball.append([x, y])
    newball.append([dx, dy])
    newball.append(r)
    newball.append(color)
    balls.append(newball)

#balls motion
def move_balls(screen):
    for ball in balls:
        if ball[0][0]+ball[2] >= 900 or ball[0][0]-ball[2] <= 0:
            ball[1][0] *= -1
        if ball[0][1]+ball[2] >= 500 or ball[0][0]-ball[2] <= 0:
            ball[1][1] *= -1
        ball[0][0] += ball[1][0]
        ball[0][1] += ball[1][1]
        circle(screen, ball[3], (ball[0][0], ball[0][1]), ball[2])


pygame.display.update()
clock = pygame.time.Clock()
finished = False
points = 0

for i in range(3):
    new_ball()

while not finished:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            finished = True
        elif event.type == pygame.MOUSEBUTTONDOWN:
            for ball in balls:
                if ((event.pos[0] - ball[0][0]) ** 2 + (event.pos[1] - ball[0][1]) ** 2) <= ball[2] ** 2:
                    print('Поймал!')
                    balls.remove(ball)
                    points += 1
                    print('Вы заработали', points, 'очков')
                    new_ball()
                    break
                else:
                    print('Мимо!')

    move_balls(screen)

    pygame.display.update()
    screen.fill(color_screen)

pygame.quit()