import random
from data import ROWS, COLUMNS
import time

def gen_matrix(rows, columns):
    '''
    function used to create the matrix wich gonna represent the fire state
    '''
    matrix = []

    for i in range(rows):
        row = []

        if i == (rows - 1):
            intensity = 35
        else:
            intensity = 0

        for j in range(columns):
            row.append(intensity)

    
        matrix.append(row)

    return matrix


def fire_control(matrix, rows, columns, spread, wind_l, wind_r):
    '''
    Function used to actually spread the fire through the matrix.

    :param spread: basically defines if the fire is either on or off
    :param wind_l: intensity of the wind pointing to the left
    :param wind_r: intensity of the wind pointing to the right
    '''
    
    for i in range(1, rows):
        for j in range(columns):
            intensity = matrix[i][j]
            
            offset = random.randint(-wind_l, wind_r)

            if spread:
                decay = random.randint(0, 3)
            else:
                decay = i

            intensity = max(intensity - decay, 0)
        
            #horizontal randomness, trick for the wind effect
            if 0 <= (j + offset) < columns: 
                matrix[i - 1][j + offset] = intensity
            