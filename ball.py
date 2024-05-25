# Import necessary libraries and modules
import pygame
import math

class Ball: 

    RADIUS = 15                                         # RADIUS (int): The radius of the ball
    position = pygame.math.Vector2(0, 0)              # position (Vector2): The position of the ball
    target = pygame.math.Vector2(0, 0)                  # target (Vector2): The target position of the ball
    impulse = pygame.math.Vector2(0, 0)                # distance (Vector2): The distance between the ball and the target
    velocity = pygame.math.Vector2(0, 0)                # velocity (Vector2): The velocity of the ball
    impulseStrength = 0                                 # impulseStrength (int): The strength of the impulse
    direction = pygame.math.Vector2(0, 0)               # direction (Vector2): The direction of the ball
    acceleration = pygame.math.Vector2(0, 0)
    friction = pygame.math.Vector2(0, 0)
    GRAVITY = 9810
    vecGravity = pygame.math.Vector2(0.0, float(GRAVITY))
    normalForce = vecGravity
    #metall ball on wood
    frictionCoefficient = 0.6
    
    def __init__(self, screen): 
        self.screen = screen                                # Set the window of the ball to the window of the game window
       
    def update(self, delta_time, klicks): 
        if klicks > 1: 
            self.movement(delta_time)                  # Update the movement of the ball
        self.draw()                                             # Draw the ball to the window
       
    def draw(self):
        pygame.draw.circle(self.screen, "red", (self.position), self.RADIUS)                                # Draw the ball to the window

    def movement(self, delta_time):
        
        self.impulse = pygame.math.Vector2(self.target) - pygame.math.Vector2(self.position)               # Update the distance of the ball
        self.impulseStrength = self.impulse.length()                                                       # Update the impulse strength of the ball
        self.direction = self.impulse.normalize()
        self.friction = self.normalForce * self.frictionCoefficient
        self.frictionAmount = math.sqrt(((self.friction.x)**2)+((self.friction.y)**2))

        self.impulseStrength = self.impulseStrength - self.frictionAmount                                  # Update the impulse strength of the ball
        

        if self.impulseStrength > 1: 
            self.acceleration = self.vecGravity + self.impulse
        else:
            self.acceleration = self.vecGravity

        self.velocity = self.velocity + self.acceleration * delta_time
        self.position = self.position + pygame.math.Vector2(self.direction + self.velocity * delta_time)    # Update the position of the ball
        