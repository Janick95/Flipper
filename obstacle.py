import pygame

# Colors (for reference)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
BLACK = (0, 0, 0)
ORANGE = (255, 165, 0)

# Obstacle base class
class Obstacle:
    def __init__(self, color):
        self.color = color
        self.collision_count = 0

    def draw(self, screen):
        pass

    def change_color_on_collision(self):
        self.collision_count += 1
        if self.collision_count == 1:
            self.color = RED
        elif self.collision_count == 2:
            self.color = GREEN
        elif self.collision_count == 3:
            self.color = BLUE

class CircleObstacle(Obstacle):
    def __init__(self, color, position, radius):
        super().__init__(color)
        self.position = pygame.math.Vector2(position)
        #self.normal_vec = pygame.math.Vector2(-position.y, position.x)
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
        self.direction_vec = self.end_pos - self.start_pos
        self.normal_vec = pygame.math.Vector2(-self.direction_vec.y, self.direction_vec.x).normalize()
        self.width = width

    def draw(self, screen):
        pygame.draw.line(screen, self.color, self.start_pos, self.end_pos, self.width)


class FlipperObstacle(Obstacle):
    def __init__(self, color, position, size, angle, identifier, pivot):
        super().__init__(color)
        self.position = pygame.math.Vector2(position)
        self.size = size
        self.angle = angle
        self.original_angle = angle
        self.identifier = identifier
        self.pivot = pygame.math.Vector2(pivot)  # Pivot relative to top-left corner
        self.original_image = pygame.Surface(size, pygame.SRCALPHA)
        self.original_image.fill(pygame.Color(color))
        self.image = pygame.Surface(size, pygame.SRCALPHA)
        self.image.blit(self.original_image, (0, 0))
        self.rect = self.image.get_rect(topleft=self.position)

    def draw(self, screen):
        # Rotate the image around the pivot point
        rotated_image = pygame.transform.rotate(self.original_image, self.angle)
        pivot_offset = self.pivot.rotate(-self.angle)  # Adjust pivot for rotation
        pivot_rect = rotated_image.get_rect(center=self.rect.topleft + pivot_offset)
        screen.blit(rotated_image, pivot_rect.topleft)

    def rotate(self, angle):
        self.angle += angle

    def reset_angle(self):
        self.angle = self.original_angle


    def rotate(self, angle):
        self.angle += angle

    def reset_angle(self):
        self.angle = self.original_angle





# ObstacleManager class
class ObstacleManager:
    def __init__(self):
        self.obstacles = []
        self.active_circles = []

    def add_obstacle(self, obstacle):
        self.obstacles.append(obstacle)
        
    def add_active_circles(self, obstacle):
        self.active_circles.append(obstacle)

    def draw(self, screen):
        self.obstacles = self.obstacles + self.active_circles
        for obstacle in self.obstacles:
            obstacle.draw(screen)
