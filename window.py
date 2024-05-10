import pygame

class Window:
    WINDOWWIDTH = 800 #WINDOWWIDTH (int): The width of the window
    WINDOWHEIGHT = 1000 #WINDOWHEIGHT (int): The height of the window
    CAPTION = "2D Flipper Automat" #CAPTION (str): The caption of the window
    
    #__init__(self): Initializes the window
    def __init__(self):
        self.window = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT)) #create the window
        pygame.display.set_caption(self.CAPTION) #set the caption of the window

   # Calculate the window resolution into real units
    def realUnits(pixel):
        pixel /= 10
        return pixel