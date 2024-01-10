import pygame
import numpy as np
import math

class PSOAgent:
    def __init__(self, idx, position):
        self.agent_color = (0, 255, 0)
        self.agent_radius = 10
        self.agent_id = idx
        self.position = np.array(position)
        self.fitness_value = np.inf
        self.P_best_pos = position
        self.velocity = 0
        self.trajectory = []
        
    # def draw_agent_on_map(self, screen):
    #     pygame.draw.circle(screen, self.agent_color, self.position, self.agent_radius)

    def get_velocity(self):
        return self.velocity
        
    def get_position(self):
        return self.position
        
    def update_velocity(self, swarm):
        v_t = self.get_velocity()
        x_t, y_t = self.get_position()#update_velocity func coming from PSO
        #cog_dist = np.sqrt([(self.P_best_pos[0] - x_t)**2 + (self.P_best_pos[1] - y_t)**2])
        #soc_dist = np.sqrt([(swarm.G_best_pos[0] - x_t)**2 + (swarm.G_best_pos[1] - y_t)**2])
        cog_dist = (self.P_best_pos[0] - x_t)**2 + (self.P_best_pos[1] - y_t)**2
        soc_dist = (swarm.G_best_pos[0] - x_t)**2 + (swarm.G_best_pos[1] - y_t)**2
        self.velocity = swarm.inertia*v_t + swarm.cognitive*np.random.uniform(0, 2, 1)*np.sqrt(cog_dist) + swarm.social*np.random.uniform(0, 2, 1)*np.sqrt(soc_dist)

    def update_position(self, swarm):
        dvx = self.velocity
        dvy = self.velocity    
        x_t, y_t = self.position
            
        if x_t + dvx < 20 or x_t + dvx > swarm.screen_width - 20:
            dvx = -dvx
        if y_t + dvy < 15 or y_t + dvy > swarm.screen_height - 50:
            dvy = -dvy
            
        x_t = int(x_t + dvx)
        y_t = int(y_t + dvy)
        self.position = (x_t, y_t)       
        


