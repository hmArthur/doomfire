import pygame
from doomfire import *
from data import *
from rendering import *

pygame.init()
size = (SCREEN_WIDTH, SCREEN_HEIGHT)
window = pygame.display.set_mode(size)
pygame.display.set_caption("doomfire")

should_run = True
clock = pygame.time.Clock()
  
matrix = gen_matrix(ROWS, COLUMNS)
spread = True

while should_run:
    #checks for input events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            should_run = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                spread = not spread

    window.fill(BLACK_COLOR)
    fire_control(matrix, ROWS, COLUMNS, spread, 1, 1)
    render_fire(matrix, pallete, ROWS, COLUMNS, window)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
