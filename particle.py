import pygame
import numpy as np
import random as rd
import math
from circle import circle
# Pygame initialization
pygame.init()
win_height = 600
win_width = 600
window = pygame.display.set_mode((win_width,win_height))
pygame.display.set_caption("PSO Visualization")
blue = (0,0,255)
red = (255, 0, 0)

# PSO attributes
W = 0.5
c1 = 1
c2 = 2


pbest_value = float('inf')
pbest_position = np.array([(0), (0)])


class Particle:
    def __init__(self,w,cog_weight,soc_weight):
        self.position= np.array([rd.randint(0,win_width), rd.randint(0,win_height)])
        self.pbest_position=self.position
        self.pbest_value=float('inf')
        self.inertia=w
        self.c1=cog_weight
        self.c2=soc_weight

        self.velocity = np.array([0,0])
        self.fitness = float('inf')

    def movement(self, targetx, targety, gbest_position, gbest_value):
        self.position= self.position+ self.velocity
        x = self.position
        y = self.position
        # pygame.draw.polygon(window, blue, ((x, y + 10), (x - 5, y), (x + 5, y)))
        self.bound()
        circle(window, x,y, red)
        # pygame.draw.circle(window, red,
        #                    (x, y), 3)
        self.fitness = math.sqrt((x-targetx)**2 + (y-targety)**2)
        self.set_pbest()
        self.set_velocity(gbest_position)

    def set_pbest(self):
        if self.fitness< self.pbest_value:
            self.pbest_value = self.fitness
            self.pbest_position = self.position

    def set_velocity(self, gbest_position):
        r1 = np.random.uniform(0, 1, 1)
        r2 = np.random.uniform(0, 1, 1)
        inertia = self.inertia
        cog_dist = self.pbest_position - self.position
        soc_dist = gbest_position - self.position
        vel = inertia * self.velocity + self.c1 * r1 * cog_dist + self.c2 * r2 * soc_dist
        self.velocity = vel

    def bound(self):
        if self.position[0] > 800:
            self.position[0] = 800

        elif self.position[0] < 0:
            self.position[0] = 0

        if self.position[1] > 800:
            self.position[1] = 800

        elif self.position[1] < 0:
            self.position[1] = 0

    def reset(self):
        self.position = np.array([rd.randint(0, win_width), rd.randint(0, win_height)])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0])
        self.fitness = float('inf')





