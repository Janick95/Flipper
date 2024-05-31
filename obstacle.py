import pygame

class Obstacle:

    def __init__(self, screen, startX, startY, endX, endY):
        self.screen = screen
        self.startX = startX
        self.startY = startY
        self.endX = endX
        self.endY = endY


    def draw(self):
        pygame.draw.line(self.screen, "purple", (self.startX, self.startY), (self.endX, self.endY), 10)