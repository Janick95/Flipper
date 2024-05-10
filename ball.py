import pygame

class Ball:

    RADIUS = 15
    position = pygame.math.Vector2(0, 0)
    target = pygame.math.Vector2(0, 0)
    distance = pygame.math.Vector2(0, 0)
    velocity = pygame.math.Vector2(0, 0)
    impulseStrength = 0
    direction = pygame.math.Vector2(0, 0)
    vecGravity = pygame.math.Vector2(0, 0)
    FRICTION = 50
    currentVelocity = 0
    impulseAcceleration = pygame.math.Vector2(0, 0)
    gravityAcceleration = pygame.math.Vector2(0, 0)
    up = False
    speedUp = False
    xPos = position.x
    yPos = position.y

    xTar = target.x
    yTar = target.y

    xMov = xPos
    yMov = yPos

    newPosition = pygame.math.Vector2(0, 0)
    distanceLength = 100

    time = 0

    def __init__(self, window):
        self.window = window
       
    def update(self, delta_time, klicks, gravity):
        if klicks > 1:
            self.movement(delta_time, gravity)
        self.draw()
       

    def draw(self):
        pygame.draw.circle(self.window, "red", (self.position), self.RADIUS)


    def movement(self, delta_time, gravity):
        self.time += 1
        self.time /= 1000000
        
        
        self.vecGravity = pygame.math.Vector2(0.0, float(gravity))
        self.gravityAcceleration += self.vecGravity
        self.distance = pygame.math.Vector2(self.target) - pygame.math.Vector2(self.position)
        self.impulseStrength = self.distance.length()
        self.direction = self.distance.normalize()
        self.impulseAcceleration = self.direction * self.impulseStrength
        self.impulseStrength -= self.FRICTION
        
        self.velocity += (self.gravityAcceleration * delta_time)
        if self.impulseStrength > 1:
            self.velocity += (self.impulseAcceleration * delta_time)
            
        
        self.position = self.position + pygame.math.Vector2(self.direction + self.velocity * delta_time)
        