import matplotlib.pyplot as plt

from SwarmFlock.envs.SwarmEnv import SwarmEnv

# Defining the main function
def main():   
    swarmFlock = SwarmEnv(env_params, swarm_params)
    
    collision_counts = []  # List to store collision count for each section of the path
    
    while swarmFlock.running:
        swarmFlock.swarmEnv.event_on_game_window(swarmFlock)
        
        swarmFlock.swarmEnv.screen.fill(swarmFlock.swarmEnv.BGCOLOR)
        
        # Update and draw the particles
        swarmFlock.step()
        for particle in swarmFlock.particles:
            particle.draw_particles(swarmFlock.swarmEnv.screen, swarmFlock.radius, swarmFlock.swarmEnv.BLUE)
            
        swarmFlock.render()
        
        # Check for collisions and count them
        collision_count = 0
        for particle in swarmFlock.particles:
            pos_x, pos_y = particle.position[0], particle.position[1]
            source_x, source_y = swarmFlock.source[0], swarmFlock.source[0]
            destination_x, destination_y = swarmFlock.destination[0], swarmFlock.destination[1]
            if pos_x >= source_x and pos_y >= source_y and pos_x <= destination_x and pos_y <= destination_y:
                collision_count += 1
        collision_counts.append(collision_count)
        
    swarmFlock.closeWindow()
    
    # Plot the graph of collision count vs section
    sections = list(range(len(collision_counts)))
    plt.plot(sections, collision_counts)
    plt.xlabel('Section')
    plt.ylabel('Collision Count')
    plt.title('Collision Count vs Section')
    plt.savefig('collision_count_graph_plot.png')
    plt.show()
    
if __name__=="__main__":
    env_params = {}
    env_params['FULSCRN'] = False
    env_params['SCREEN_WIDTH'] = 1200 
    env_params['SCREEN_HEIGHT'] = 800
    env_params['CORNER_X'] = 50
    env_params['CORNER_Y'] = 50
    env_params['FPS'] = 60
    env_params['SOURCE'] = (100, 100)
    env_params['DESTINATION'] = (1000, 500)
    
    swarm_params = {}
    swarm_params['NUM_PARTICLES'] = 10
    swarm_params['RADIUS'] = 5
    swarm_params['MAX_VELOCITY'] = 3
    swarm_params['NEIGHBOR_DISTANCE'] = 50
    swarm_params['SEPARATION_DISTANCE'] = 30
    swarm_params['COHESION_FACTOR'] = 0.04
    swarm_params['SEPARATION_FACTOR'] = 0.2
    swarm_params['ALIGNMENT_FACTOR'] = 0.1
    swarm_params['AVOIDANCE_FACTOR'] = 0.4
    main()
