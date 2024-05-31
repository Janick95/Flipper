import pygame

class Window:
    WINDOWWIDTH = 800 
    WINDOWHEIGHT = 1000 
    CAPTION = "2D Flipper Automat" 
    
    
    def __init__(self):
        self.screen = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT)) 
        pygame.display.set_caption(self.CAPTION)