import pygame
from pygame.locals import *
from particle import *


# Using draw.rect module of
# pygame to draw the solid circle
def circle(window, x,y, color):
    pygame.draw.circle(window, (255,0,0),
                       (x, y), 3)
    pygame.display.update()
# pygame.stop(10)
# Draws the surface object to the screen.
