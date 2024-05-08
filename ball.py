import pygame

class Ball:

    RADIUS = 20
    speed = 300
    velocity = 500
    GRAVITY = 100
    FRICTION = 50
    currentVelocity = 0 
    up = False
    speedUp = False

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
        self.y += self.GRAVITY * delta_time

        #Constant Velocity
        self.currentVelocity = self.currentVelocity - self.FRICTION
        
        
        if self.up:
            self.y -= self.speed * delta_time
            if self.speedUp:
                self.currentVelocity = self.currentVelocity + 2
                self.speed = self.speed + self.currentVelocity * delta_time
                if self.currentVelocity == self.velocity:
                    self.speedUp = False
            else:
                self.currentVelocity = self.currentVelocity - 2
                self.speed = self.speed - self.currentVelocity * delta_time
            if self.speed == self.GRAVITY:
                self.up = False
        
        
        #Active Controlls
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RIGHT]:
            self.x += self.speed * delta_time
        elif keys[pygame.K_LEFT]:
            self.x -= self.speed * delta_time
        if keys[pygame.K_UP]:
            self.up = True
            self.speedUp = True
            self.currentVelocity = self.velocity
            