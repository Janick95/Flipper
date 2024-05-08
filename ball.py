import pygame

class Ball:

    RADIUS = 20

    def __init__(self, window, x, y):
        self.x = x
        self.y = y
        self.window = window
       
    def update(self, speed, delta_time, GRAVITY):
        self.movement(speed, delta_time, GRAVITY)
        self.draw()

    def draw(self):
        pygame.draw.circle(self.window, "red", (self.x, self.y), self.RADIUS)

    def movement(self, speed, delta_time, GRAVITY):
        
        self.y += GRAVITY * delta_time
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        
        #Active Controlls
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += speed * delta_time
        elif keys[pygame.K_LEFT]:
            self.x -= speed * delta_time
        if keys[pygame.K_UP]:
            self.y -= speed * delta_time