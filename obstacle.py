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
        self.position = pygame.math.Vector2(position)
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
        self.start_pos = pygame.math.Vector2(start_pos)
        self.end_pos = pygame.math.Vector2(end_pos)
        self.width = width

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, self.width)


class FlipperObstacle(Obstacle):
    def __init__(self, color, position, size, angle):       
        self.color = color
        self.position = position
        self.size = size
        self.angle = angle
        self.rect = pygame.Rect(position, size)

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def rotate(self, angle):
        self.angle += angle    


# ObstacleManager class
class ObstacleManager:
    def __init__(self):
        self.obstacles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)

    def draw(self, screen):
        for obstacle in self.obstacles:
            obstacle.draw(screen)
