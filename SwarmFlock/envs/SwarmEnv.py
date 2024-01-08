import pygame
import math

from PyGameEnv import Env_setup
from Particles import Particle

class SwarmEnv:
    def __init__(self, env_params, swarm_params):
        self.swarmEnv = Env_setup(env_params)
        self.num_particles = swarm_params['NUM_PARTICLES']
        self.radius = swarm_params['RADIUS']
        self.max_velocity = swarm_params['MAX_VELOCITY']
        self.corner_x = env_params['CORNER_X']
        self.corner_y = env_params['CORNER_Y']
        self.neighbor_dist = swarm_params['NEIGHBOR_DISTANCE']
        self.separation_dist = swarm_params['SEPARATION_DISTANCE']
        self.alignment_factor = swarm_params['ALIGNMENT_FACTOR']
        self.cohesion_factor = swarm_params['COHESION_FACTOR']
        self.avoidance_factor = swarm_params['AVOIDANCE_FACTOR']
        self.separation_factor = swarm_params['SEPARATION_FACTOR']
        self.collision_threshold=swarm_params['COLLISION THRESHOLD']
        # Create a flock of particles
        self.particles = [Particle(self.corner_x + (self.radius * 8 + 20) * (i % int(math.sqrt(self.num_particles))),
        		           self.corner_y + (self.radius * 8 + 20) * (i // int(math.sqrt(self.num_particles))),
                                   self.swarmEnv.BLUE, self.max_velocity) for i in range(self.num_particles)]
        self.running = True
    
    def step(self, mouse_pos):
        for particle in self.particles:
            particle._align(self.particles, self.neighbor_dist, self.alignment_factor)
            particle._cohere(self.particles, self.neighbor_dist, self.cohesion_factor)
            particle._separate(self.particles, self.separation_dist, self.separation_factor)
            particle._avoid_collision(self.particles, self.radius, self.avoidance_factor)
            particle._move_towards(mouse_pos, self.cohesion_factor)
            particle._limit_velocity(self.max_velocity)
            
            # Update position the particles
            x, y = particle.position[0], particle.position[1]
            x += particle.velocity_x
            y += particle.velocity_y
            particle.position = (x, y)
            
            particle._check_boundary_collision(self.swarmEnv.win_width, self.swarmEnv.win_height)

    def calculate_collision_metrics(self, collision_threshold):
        for particle in self.particles:
            particle.calculate_collision_metric(self.particles, collision_threshold)

    def render(self):
        pygame.display.flip()
        self.swarmEnv.clock.tick(self.swarmEnv.fps)
        
    def getMousePos(self, ):
        # Get the mouse click position
        target_x, target_y = pygame.mouse.get_pos()
        return (target_x, target_y)
        # target_x = None, target_y=None
        # for event in pygame.event.get():
        #     if event.type == pygame.QUIT:
        #         run = False
        #     if event.type == pygame.MOUSEBUTTONDOWN:
        #         targetx, targety = pygame.mouse.get_pos()
        #     # for particle in particle_list:
        #     #     particle.reset()
        #
        #     if event.type == pygame.KEYDOWN:
        #         if event.key == pygame.K_ESCAPE:
        #             run = False

        
    def closeWindow(self):
        pygame.quit()
