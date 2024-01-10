# PSO-Visualization
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
pygame.display.set_caption("PSO target Hunt Visualization")
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

    def step(self, targetx, targety, gbest_position, gbest_value):
        self.position = self.position + self.velocity
        x = self.position[0]
        y = self.position[1]
        self.bound()
        pygame.draw.polygon(window, green, ((x, y + 10), (x - 5, y), (x + 5, y)))

        self.fitness = math.sqrt((x - targetx) ** 2 + (y - targety) ** 2)
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


def update(particle_list, targetx, targety):
    closest_particle = min(particle_list, key=attrgetter('fitness'))
    gbest_value = closest_particle.fitness
    gbest_position = closest_particle.position

    window.fill((0, 0, 0))
    pygame.draw.circle(window, red, [targetx, targety], 5)

    for particle in particle_list:
        particle.step(targetx, targety, gbest_position, gbest_value)

    pygame.display.update()

def objective_function(self, position):
    # x = -self.screen_width / 2 + position[0]
    # y = -self.screen_height / 2 + position[1]
    x=position[0]
    y = position[1]
    return x ** 2 + y ** 2

def find_global_best(self):
    min_val = self.PSOAgents[0].fitness_value
    min_id = self.PSOAgents[0].agent_id
    min_pos = self.PSOAgents[0].position
    for i in range(1, self.no_agents):
        if min_val > self.PSOAgents[i].fitness_value:
            min_val = self.PSOAgents[i].fitness_value
            min_id = self.PSOAgents[i].agent_id
            min_pos = self.PSOAgents[i].position
    return min_pos, min_val, min_id


def main():
    particle_list = [Particle() for _ in range(10)]
    run = False

    while not run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                targetx, targety = pygame.mouse.get_pos()
                pygame.draw.circle(window, red, [targetx, targety], 5)
                run = True

    while run:
        pygame.time.delay(100)  # 60fps
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.MOUSEBUTTONDOWN:
                targetx, targety = pygame.mouse.get_pos()
                for particle in particle_list:
                    particle.reset()

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False

        update(particle_list, targetx, targety)

    pygame.quit()
    quit()


if __name__ == "__main__":
    main()