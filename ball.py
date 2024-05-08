import pygame

class Ball:

    RADIUS = 20
    speed = 300
    velocity = 2000
    GRAVITY = 200
    FRICTION = 50

    def __init__(self, window, x, y):
        self.x = x
        self.y = y
        self.window = window
       
    def update(self, delta_time):
        self.movement(delta_time)
        self.draw()

    def draw(self):
        pygame.draw.circle(self.window, "red", (self.x, self.y), self.RADIUS)

    def movement(self, delta_time):
        
                    
        self.velocity = self.velocity - self.FRICTION

       

        #Constant Velocity
        self.speed = self.speed + self.velocity * delta_time
        self.y += self.GRAVITY * delta_time
        
        
        #Active Controlls
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += self.speed * delta_time
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed * delta_time
        if keys[pygame.K_UP]:
            self.y -= self.speed * delta_time
            