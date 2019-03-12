import sys
import pygame

def run_game() :

    bg_color = (230, 230,230)

    pygame.init()
    screen = pygame.display.set_mode((600,400))
    pygame.display.set_caption("good luck")

    while True:
        for event in pygame.event.get() :
            if event.type==pygame.QUIT :
                sys.exit()

            screen.fill(bg_color)

            pygame.display.flip()

run_game()
