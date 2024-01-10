# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


import pygame
from particle import *
from NEXT import update
from operator import attrgetter
def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.

def running():
    particle_list = [Particle(0.5,1,2) for _ in range(10)]
    run = False

    #swarm = particle()
    while not run:
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                targetx, targety = pygame.mouse.get_pos()
                pygame.draw.circle(window, red, (targetx, targety), 5)
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


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    running()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
