import pygame
# from pyswarm
from PSOAgent import PSOAgent
import matplotlib.pyplot as plt
import numpy as np

def createPSOAgent(self):
    # Assign initial position
    initial_pos = []
    agent_list = []
    x = 20
    y = int(self.screen_height/20)
    for i in range(self.no_agents):
        initial_pos.append((x, y))
        y += 40
    
    # Create PSO agents
    agent_list = [PSOAgent(i, initial_pos[i]) for i in range(self.no_agents)]
    
    return agent_list


class PSOEnv:
    def __init__(self, n, w, cognition_weight, social_weight):
        pygame.init()
        self.no_agents = n
        self.screen_height, self.screen_width = 600, 1000
        self.screen = pygame.display.set_mode((self.screen_width, self.screen_height))
        self.map = pygame.image.load('map.png')
        self.caption = pygame.display.set_caption("Particle Swarm Optimization")
        self.clock = pygame.time.Clock()
        self.font = pygame.font.SysFont("Arial", 30)
        self.game_speed = 30
        self.PSOAgents = createPSOAgent(self)
        self.inertia = w
        self.cognitive = cognition_weight
        self.social = social_weight
        self.G_best_pos = (0, 0)
        self.G_best_val = 0
        self.G_best_id = None
        self.convergence_criteria = False
        self.running = True
        
    # def event_on_game_window(self):
    #     for event in pygame.event.get():
    #         if event.type == pygame.QUIT:
    #             self.running = False
    
    def objective_function(self, position):
        # x = -self.screen_width/2 + position[0]
        # y = -self.screen_height/2 + position[1]
        # return x**2 + y**2
        z = np.sum(np.square(position))
        return z


    
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
                        
    # def view(self):
    #     self.screen.blit(self.map, (0, 0))
    #     for i in range(self.no_agents):
    #         self.PSOAgents[i].draw_agent_on_map(self.screen)
    #
        # pygame.display.flip()
        # self.clock.tick(self.game_speed)
