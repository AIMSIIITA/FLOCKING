#import numpy as np
import pygame
import random
import math

class Particle():
    def __init__(self, x, y, COLOR, MAX_VELOCITY):
        self.position = (x, y)
        self.velocity_x = random.uniform(-MAX_VELOCITY, MAX_VELOCITY)
        self.velocity_y = random.uniform(-MAX_VELOCITY, MAX_VELOCITY)
        self.color = COLOR
        self.collision_metric=0
        '''self.part_Id = n
        self.image = pygame.Surface((25, 25)).convert()
        self.image.set_colorkey(0)
        self.rect = self.image.get_rect(center = pos)
        self.ang = randint(-180, 180)         
        self.turnDir = pygame.Vector2(1, 0).rotate(self.ang)
        self.position = pygame.Vector2(self.rect.center)
        
        self.pbest_position = self.position
        self.orig_image = pygame.transform.rotate(self.image.copy(), self.ang)
        self.tDistance = 0
        self.tAngle = 0'''
    
    def _align(self, particles, NEIGHBOR_DISTANCE, ALIGNMENT_FACTOR):
        avg_velocity_x = 0
        avg_velocity_y = 0
        count = 0
        for particle in particles:
            if self._distance(particle) < NEIGHBOR_DISTANCE:
                avg_velocity_x += particle.velocity_x
                avg_velocity_y += particle.velocity_y
                count += 1
        if count > 0:
            avg_velocity_x /= count
            avg_velocity_y /= count
            self.velocity_x += (avg_velocity_x - self.velocity_x) * ALIGNMENT_FACTOR
            self.velocity_y += (avg_velocity_y - self.velocity_y) * ALIGNMENT_FACTOR
    
    def _cohere(self, particles, NEIGHBOR_DISTANCE, COHESION_FACTOR):
        avg_pos_x = 0
        avg_pos_y = 0
        count = 0
        for particle in particles:
            if self._distance(particle) < NEIGHBOR_DISTANCE:
                avg_pos_x += particle.position[0]
                avg_pos_y += particle.position[1]
                count += 1
        if count > 0:
            avg_pos_x /= count
            avg_pos_y /= count
            self.velocity_x += (avg_pos_x - self.position[0]) * COHESION_FACTOR
            self.velocity_y += (avg_pos_y - self.position[1]) * COHESION_FACTOR
    
    def _separate(self, particles, SEPARATION_DISTANCE, SEPARATION_FACTOR):
        move_x = 0
        move_y = 0
        for particle in particles:
            if self._distance(particle) < SEPARATION_DISTANCE:
                move_x += (self.position[0] - particle.position[0])
                move_y += (self.position[1] - particle.position[1])
        self.velocity_x += move_x * SEPARATION_FACTOR
        self.velocity_y += move_y * SEPARATION_FACTOR
    
    def _avoid_collision(self, particles, RADIUS, AVOIDANCE_FACTOR):
        move_x = 0
        move_y = 0
        for particle in particles:
            if self._distance(particle) < RADIUS * 2 and particle != self:
                move_x += (self.position[0] - particle.position[0])
                move_y += (self.position[1] - particle.position[1])
        self.velocity_x += move_x * AVOIDANCE_FACTOR
        self.velocity_y += move_y * AVOIDANCE_FACTOR

    def _move_towards(self, mouse_pos, COHESION_FACTOR):
        target_x, target_y = mouse_pos[0], mouse_pos[1]
        self.velocity_x += (target_x - self.position[0]) * COHESION_FACTOR
        self.velocity_y += (target_y - self.position[1]) * COHESION_FACTOR

    def calculate_collision_metric(self, particles, collision_threshold):
        total_collision = 0
        total_collisions_detected = 0

        for particle in particles:
            if particle != self:
                distance = self._distance(particle)

                if distance < collision_threshold:
                    total_collision += distance
                    total_collisions_detected += 1

        if total_collisions_detected > 0:
            self.collision_metric = total_collision / total_collisions_detected
        else:
            self.collision_metric = 0

    def _limit_velocity(self, MAX_VELOCITY):
        velocity = math.sqrt(self.velocity_x**2 + self.velocity_y**2)
        if velocity > MAX_VELOCITY:
            self.velocity_x = (self.velocity_x / velocity) * MAX_VELOCITY
            self.velocity_y = (self.velocity_y / velocity) * MAX_VELOCITY
    
    def _check_boundary_collision(self, SCREEN_WIDTH, SCREEN_HEIGHT):
        x, y = self.position[0], self.position[1]
        
        if x < 0:
            x = 0
        elif x > SCREEN_WIDTH:
            x = SCREEN_WIDTH
        if y < 0:
            y = 0
        elif y > SCREEN_HEIGHT:
            y = SCREEN_HEIGHT
        
        self.position = (x, y)
                                                    
    def _distance(self, particle):
        return math.sqrt((self.position[0] - particle.position[0])**2 + (self.position[1] - particle.position[1])**2)
    
    def draw_particles(self, screen, RADIUS, COLOR):
        angle = math.atan2(self.velocity_y, self.velocity_x)
        angle += math.pi             # Rotate the arrow head
        length = RADIUS * 6          # Increased length
        
        # Calculate the coordinates of the particle shape
        part_points = [
            (self.position[0] + RADIUS * math.cos(angle), self.position[1] + RADIUS * math.sin(angle)),
            (self.position[0] + length * math.cos(angle - 0.5), self.position[1] + length * math.sin(angle - 0.5)),
            (self.position[0] + length * 0.6 * math.cos(angle), self.position[1] + length * 0.6 * math.sin(angle)),
            (self.position[0] + length * math.cos(angle + 0.5), self.position[1] + length * math.sin(angle + 0.5)),
        ]
        
        pygame.draw.polygon(screen, COLOR, part_points)
