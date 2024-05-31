# Import necessary library
import pygame

# Define the Obstacle class
class Obstacle:
    # Initialize the Obstacle class with the screen and the coordinates of the start and end points
    def __init__(self, screen, startX, startY, endX, endY):
        self.screen = screen                                            # The screen where the obstacle will be drawn
        self.startX = startX                                            # The x-coordinate of the start point
        self.startY = startY                                            # The y-coordinate of the start point
        self.endX = endX                                                # The x-coordinate of the end point
        self.endY = endY                                                # The y-coordinate of the end point

    # Draw the obstacle line on the screen
    def draw(self):
        # Draw a line on the screen using the start and end points of the obstacle
        pygame.draw.line(self.screen, "purple", (self.startX, self.startY), (self.endX, self.endY), 10)