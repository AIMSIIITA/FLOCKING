# PSO-Visualization
# Simple visualization of how the Particle Swarm Optimization algorithm works using pygame.

# https://medium.com/analytics-vidhya/implementing-particle-swarm-optimization-pso-algorithm-in-python-9efc2eb179a6
# And
# https://towardsdatascience.com/particle-swarm-optimisation-in-machine-learning-b01b1d2ad8a8


import pygame
import random as rd
import math
import numpy as np
from operator import attrgetter

# Pygame initialization
pygame.init()
win_height = 800
win_width = 800
window = pygame.display.set_mode((win_width, win_height))
pygame.display.set_caption("PSO Treasure Hunt Visualization")
green = (0, 0, 255)
red = (255, 0, 0)

# PSO attributes
W = 0.5
c1 = 1
c2 = 2
pbest_value = float('inf')
pbest_position = np.array([(0), (0)])


class Particle():
    def __init__(self):
        self.position = np.array([rd.randint(0, win_width), rd.randint(0, win_height)])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0])
        self.fitness = float('inf')

    def step(self, treasurex, treasurey, gbest_position, gbest_value):
        self.position = self.position + self.velocity
        x = self.position[0]
        y = self.position[1]
        self.bound()
        pygame.draw.polygon(window, green, ((x, y + 10), (x - 5, y), (x + 5, y)))

        self.fitness = math.sqrt((x - treasurex) ** 2 + (y - treasurey) ** 2)
        self.set_pbest()
        self.set_velocity(gbest_position, gbest_value)

    def set_pbest(self):
        if (self.fitness < self.pbest_value):
            self.pbest_value = self.fitness
            self.pbest_position = self.position

    def set_velocity(self, gbest_position, gbest_value):
        r1 = rd.random()
        r2 = rd.random()

        vel_cognitive = c1 * r1 * (self.pbest_position - self.position)
        vel_social = c2 * r2 * (gbest_position - self.position)

        new_velocity = W * self.velocity + vel_cognitive + vel_social
        self.velocity = new_velocity

    def bound(self):
        if (self.position[0] > 800):
            self.position[0] = 800

        elif (self.position[0] < 0):
            self.position[0] = 0

        if (self.position[1] > 800):
            self.position[1] = 800

        elif (self.position[1] < 0):
            self.position[1] = 0

    def reset(self):
        self.position = np.array([rd.randint(0, win_width), rd.randint(0, win_height)])
        self.pbest_position = self.position
        self.pbest_value = float('inf')
        self.velocity = np.array([0, 0])
        self.fitness = float('inf')


def update(particle_list, treasurex, treasurey):
    closest_particle = min(particle_list, key=attrgetter('fitness'))
    gbest_value = closest_particle.fitness
    gbest_position = closest_particle.position

    window.fill((0, 0, 0))
    pygame.draw.circle(window, red, [treasurex, treasurey], 5)

    for particle in particle_list:
        particle.step(treasurex, treasurey, gbest_position, gbest_value)

    # self.trajectory.append((x, y))
    # for i in range(len(self.trajectory) - 1):
    #     pygame.draw.line(screen, self.trajec_color, self.trajectory[i], self.trajectory[i + 1], 2)
    pygame.display.update()


def main():
    particle_list = [Particle() for _ in range(10)]
    run = False

    while not run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                treasurex, treasurey = pygame.mouse.get_pos()
                pygame.draw.circle(window, red, [treasurex, treasurey], 5)


                run = True

    while run:
        pygame.time.delay(100)  # 60fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                treasurex, treasurey = pygame.mouse.get_pos()
                for particle in particle_list:
                    particle.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        update(particle_list, treasurex, treasurey)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()