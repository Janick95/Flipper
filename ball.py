# Import necessary libraries and modules
import pygame

class Ball: 

    RADIUS = 15                                         # RADIUS (int): The radius of the ball
    position = pygame.math.Vector2(0, 0)              # position (Vector2): The position of the ball
    target = pygame.math.Vector2(0, 0)                  # target (Vector2): The target position of the ball
    distance = pygame.math.Vector2(0, 0)                # distance (Vector2): The distance between the ball and the target
    velocity = pygame.math.Vector2(0, 0)                # velocity (Vector2): The velocity of the ball
    impulseStrength = 0                                 # impulseStrength (int): The strength of the impulse
    direction = pygame.math.Vector2(0, 0)               # direction (Vector2): The direction of the ball
    vecGravity = pygame.math.Vector2(0, 0)              # vecGravity (Vector2): The gravity vector
    impulseAcceleration = pygame.math.Vector2(0, 0)     # impulseAcceleration (Vector2): The impulse acceleration of the ball
    gravityAcceleration = pygame.math.Vector2(0, 0)
    
    GRAVITY = 9810
    FRICTION = 50
    
    def __init__(self, screen): 
        self.screen = screen                                # Set the window of the ball to the window of the game window
       
    def update(self, delta_time, klicks): 
        if klicks > 1: 
            self.movement(delta_time)                  # Update the movement of the ball
        self.draw()                                             # Draw the ball to the window
       
    def draw(self):
        pygame.draw.circle(self.screen, "red", (self.position), self.RADIUS)                                # Draw the ball to the window

    def movement(self, delta_time):
                
        self.vecGravity = pygame.math.Vector2(0.0, float(self.GRAVITY))                                          # Set the gravity vector of the ball
        self.gravityAcceleration += self.vecGravity                                                         # Update the gravity acceleration of the ball
        self.distance = pygame.math.Vector2(self.target) - pygame.math.Vector2(self.position)               # Update the distance of the ball
        self.impulseStrength = self.distance.length()                                                       # Update the impulse strength of the ball
        self.direction = self.distance.normalize()                                                          # Update the direction of the ball
        self.impulseAcceleration = self.direction * self.impulseStrength                                    # Update the impulse acceleration of the ball
        self.impulseStrength -= self.FRICTION                                                               # Update the impulse strength of the ball
        
        self.velocity += (self.gravityAcceleration * delta_time)                                            # Update the gravity acceleration of the ball
        if self.impulseStrength > 1: 
            self.velocity += (self.impulseAcceleration * delta_time)                                        # Update the impulse acceleration of the ball
            
        self.position = self.position + pygame.math.Vector2(self.direction + self.velocity * delta_time)    # Update the position of the ball
        