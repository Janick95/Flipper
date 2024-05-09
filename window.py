import pygame

class Window:
    WINDOWWIDTH = 1920
    WINDOWHEIGHT = 1440
    CAPTION = "2D Flipper Automat"
    
    
    def __init__(self):
        self.window = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        pygame.display.set_caption(self.CAPTION)
        