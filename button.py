import pygame
from pygame.locals import *
import sys


pygame.init()


res = (720,720)
white = (255,255,255)
screen = pygame.display.set_mode(res)
red = (220,20,60)
darkred = (178,34,34)
cyan = (64,244,208)
button_text = 'button'

h = screen.get_height()
w = screen.get_width()

smallfont = pygame.font.SysFont('Arial',35)

while True:
    screen.fill(cyan)
    mouse = pygame.mouse.get_pos()

    for ev in pygame.event.get():
        if ev.type == pygame.MOUSEBUTTONDOWN:
            if w/2 <= mouse[0] <= w/2+140 and h/2 <= mouse[1] <= h/2+40:
                time_first_press = pygame.time.get_ticks()
                print(time_first_press)
                button_text = "Don't"

                # check time
    if w/2 <= mouse[0] <= w/2+140 and h/2 <= mouse[1] <= h/2+40:
        pygame.draw.circle(screen,red,(w/2,h/2),250)
    else:
        pygame.draw.circle(screen,darkred,(w/2,h/2),250)

    screen.blit(smallfont.render(button_text,True,white), (w/2-40,h/2-30))

    pygame.display.update()
