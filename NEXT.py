from particle import *
from operator import attrgetter
def update(particle_list, targetx, targety):
    closest_particle = min(particle_list, key=attrgetter('fitness'))
    gbest_value = closest_particle.fitness
    gbest_position = closest_particle.position

    window.fill((0, 0, 0))
    pygame.draw.circle(window, red, [targetx, targety], 5)

    for particle in particle_list:
        particle.movement(targetx, targety, gbest_position, gbest_value)

    pygame.display.update()