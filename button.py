import pygame
import pygame_menu
from pygame.locals import *
import sys


pygame.init()

h = 720
w = 720
res = (h,w)
screen = pygame.display.set_mode(res)
bg = pygame.image.load('background.gif')

white = (255,255,255)
red = (220,20,60)
darkred = (178,34,34)
cyan = (64,244,208)

clock = pygame.time.Clock()

tutorial_text = ["Press the button after go.","Try to get as close to five","seconds as possible.","The closer the better.", "                     "]


pygame.time.set_timer(pygame.USEREVENT, 1000)
smallfont = pygame.font.SysFont('computer_modern',35)
largefont = pygame.font.SysFont('computer_modern',70)

def game():
    counter = 3
    counter_text = str(counter).rjust(3)
    score_text = '0'
    button_text = 'button'
    unpressed = True

    while True:
        screen.fill(cyan)
        mouse = pygame.mouse.get_pos()

        for ev in pygame.event.get():
            if ev.type == pygame.USEREVENT:
                counter -= 1
                counter_text = str(counter).rjust(3) if counter > 0 else 'Go!'

            if ev.type == pygame.MOUSEBUTTONDOWN:
                if (mouse[0]-w/2)**2+(mouse[1]- h/2)**2 <= 250**2 and unpressed:
                    time_first_press = pygame.time.get_ticks()
                    score_text = str(max(0,5-abs((time_first_press -8000)/1000)))
                    button_text = "Don't"
                    unpressed = False
            if ev.type == pygame.MOUSEBUTTONUP and not unpressed:
                screen.fill((0,0,0))
                screen.blit(largefont.render(score_text, True, white), (w/2-20,h/2-30))
                screen.blit(largefont.render("Your score:", True, white), (w/2-20,h/2-70))
                pygame.display.update()
                pygame.time.wait(3000)
                pygame.quit()
            if ev.type == pygame.QUIT:
                pygame.QUIT
        if (mouse[0]-w/2)**2+(mouse[1]- h/2)**2 <= 250**2:
            pygame.draw.circle(screen,red,(w/2,h/2),250)
        else:
            pygame.draw.circle(screen,darkred,(w/2,h/2),250)

        screen.blit(smallfont.render(counter_text, True, white),(32,48))
        screen.blit(smallfont.render(score_text, True, white), (550,48))
        screen.blit(smallfont.render(button_text,True,white), (w/2-40,h/2-30))

        pygame.display.update()
    pass

instruction_menu = pygame_menu.Menu('Instructions', 500,400, theme=pygame_menu.themes.THEME_BLUE)




for t in tutorial_text:
    instruction_menu.add.label(t)
instruction_menu.add.button('Go Back', pygame_menu.events.BACK)

leader_menu = pygame_menu.Menu('Leaderboard', 500,400, theme=pygame_menu.themes.THEME_BLUE)
leader_menu.add.label("your score is ")
leader_menu.add.button('Go Back' , pygame_menu.events.BACK)

menu = pygame_menu.Menu('The Button Game', 500, 400, theme=pygame_menu.themes.THEME_BLUE)

menu.add.button('Play', game)
menu.add.button('How to play', instruction_menu )
menu.add.button('Quit', pygame_menu.events.EXIT)
menu.mainloop(screen)
