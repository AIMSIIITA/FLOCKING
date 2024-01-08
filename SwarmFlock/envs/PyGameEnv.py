import pygame

class Env_setup:
    def __init__(self, env_params):
        pygame.init()
        self.win_height, self.win_width = env_params['SCREEN_HEIGHT'], env_params['SCREEN_WIDTH']
        pygame.display.set_caption("Swarm Flock Simulation")
        
        if env_params['FULSCRN']:
            resol = (pygame.display.Info().current_w, pygame.display.Info().current_h)
            self.screen = pygame.display.set_mode(resol, pygame.SCALED)
        else: self.screen = pygame.display.set_mode((env_params['SCREEN_WIDTH'], env_params['SCREEN_HEIGHT']), pygame.RESIZABLE)
        
        # Set up colors
        #self.BLACK = pygame.Color(0, 0, 0)
        self.WHITE = pygame.Color(255, 255, 255)
        #self.RED = pygame.Color(255, 0, 0)
        #self.GREEN = pygame.Color(0, 255, 0)
        self.BLUE = pygame.Color(0, 0, 255)
        
        self.BGCOLOR = self.WHITE
        self.font = pygame.font.SysFont('Arial', 30)
        self.clock = pygame.time.Clock()
        self.fps = env_params['FPS']
                
    def event_on_game_window(self, swarm):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                swarm.running = False
