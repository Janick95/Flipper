import pygame

# Colors (for reference)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Obstacle base class
class Obstacle:
    def __init__(self, color):
        self.color = color

    def draw(self, screen):
        pass

class CircleObstacle(Obstacle):
    def __init__(self, color, position, radius):
        super().__init__(color)
        self.position = position
        self.radius = radius

    def draw(self, screen):
        pygame.draw.circle(screen, self.color, self.position, self.radius)

class RectObstacle(Obstacle):
    def __init__(self, color, rect):
        super().__init__(color)
        self.rect = rect

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

class LineObstacle(Obstacle):
    def __init__(self, color, start_pos, end_pos, width):
        super().__init__(color)
        self.start_pos = start_pos
        self.end_pos = end_pos
        self.width = width

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, self.width)

# ObstacleManager class
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
