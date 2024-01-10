from SwarmEnv import SwarmEnv
from Particles import Particle
# Defining the main function
def main():   
    swarmFlock = SwarmEnv(env_params, swarm_params)
    
    while swarmFlock.running:
        swarmFlock.swarmEnv.event_on_game_window(swarmFlock)
        
        swarmFlock.swarmEnv.screen.fill(swarmFlock.swarmEnv.BGCOLOR)
        swarmFlock.calculate_collision_metrics(swarmFlock.collision_threshold)

        mouse_pos = swarmFlock.getMousePos()
        # particles = initialize_particles(num_particles, screen_width, screen_height, max_velocity)

        # Update and draw the particles
        swarmFlock.step(mouse_pos)
        for particle in swarmFlock.particles:
            particle.draw_particles(swarmFlock.swarmEnv.screen, swarmFlock.radius, swarmFlock.swarmEnv.BLUE)

        swarmFlock.render()
    swarmFlock.closeWindow()
    
if __name__=="__main__":
    env_params = {}
    env_params['FULSCRN'] = False
    env_params['SCREEN_WIDTH'] = 1200 
    env_params['SCREEN_HEIGHT'] = 800
    env_params['CORNER_X'] = 50
    env_params['CORNER_Y'] = 50
    env_params['FPS'] = 60
    
    swarm_params = {}
    swarm_params['NUM_PARTICLES'] = 10
    swarm_params['RADIUS'] = 5
    swarm_params['MAX_VELOCITY'] = 3
    swarm_params['NEIGHBOR_DISTANCE'] = 50
    swarm_params['SEPARATION_DISTANCE'] = 50
    swarm_params['COHESION_FACTOR'] = 0.04
    swarm_params['SEPARATION_FACTOR'] = 0.2
    swarm_params['ALIGNMENT_FACTOR'] = 0.1
    swarm_params['AVOIDANCE_FACTOR'] = 0.4
    swarm_params['COLLISION THRESHOLD']=50
    main()
