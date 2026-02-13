import pygame
from data import PIXEL_SIZE, SCREEN_HEIGHT

def render_fire(matrix, colors, rows, columns, surface):
    '''
    function used to render the matrix once every position intensity its already calculated
    '''
    for i in range(rows):
        for j in range(columns):
            rect = (j*PIXEL_SIZE, SCREEN_HEIGHT-i*PIXEL_SIZE, PIXEL_SIZE, PIXEL_SIZE)
            pygame.draw.rect(surface, colors[matrix[rows - (i + 1)][j]], rect)