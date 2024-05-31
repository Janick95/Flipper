# Import necessary library
import pygame

# Define the Window class
class Window:
    # Define the window dimensions, caption, and initialize the window
    WINDOWWIDTH = 800                                   # The width of the window in pixels
    WINDOWHEIGHT = 1000                                 # The height of the window in pixels
    CAPTION = "2D Flipper Automat"                      # The title of the window

    # Initialize the Window class with the screen and the window caption
    def __init__(self):
        # Create a window with the specified dimensions and caption
        self.screen = pygame.display.set_mode((self.WINDOWWIDTH, self.WINDOWHEIGHT))
        # Set the window caption
        pygame.display.set_caption(self.CAPTION)