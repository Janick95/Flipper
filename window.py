import pygame

class Window:
    WINDOWWIDTH = 800
    WINDOWHEIGHT = 600
    CAPTION = "2D Flipper Automat"
    
    
    def __init__(self):
        self.window = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption(self.CAPTION)
        