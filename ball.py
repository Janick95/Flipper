# Import necessary libraries and modules
import pygame

class Ball: 

    RADIUS = 15                                         # RADIUS (int): The radius of the ball
    position = pygame.math.Vector2(0, 0)                # position (Vector2): The position of the ball
    target = pygame.math.Vector2(0, 0)                  # target (Vector2): The target position of the ball
    distance = pygame.math.Vector2(0, 0)                # distance (Vector2): The distance between the ball and the target
    velocity = pygame.math.Vector2(0, 0)                # velocity (Vector2): The velocity of the ball
    impulseStrength = 0                                 # impulseStrength (int): The strength of the impulse
    direction = pygame.math.Vector2(0, 0)               # direction (Vector2): The direction of the ball
    vecGravity = pygame.math.Vector2(0, 0)              # vecGravity (Vector2): The gravity vector
    FRICTION = 50                                       # FRICTION (int): The friction of the ball
    currentVelocity = 0                                 # currentVelocity (int): The current velocity of the ball
    impulseAcceleration = pygame.math.Vector2(0, 0)     # impulseAcceleration (Vector2): The impulse acceleration of the ball
    gravityAcceleration = pygame.math.Vector2(0, 0)     # gravityAcceleration (Vector2): The gravity acceleration of the ball
    up = False                                          # up (bool): Is the ball moving upwards?
    speedUp = False                                     # speedUp (bool): Is the ball moving upwards?
    xPos = position.x                                   # xPos (int): The x position of the ball
    yPos = position.y                                   # yPos (int): The y position of the ball

    xTar = target.x                                     # xTar (int): The x target of the ball
    yTar = target.y                                     # yTar (int): The y target of the ball

    xMov = xPos                                         # xMov (int): The x movement of the ball
    yMov = yPos                                         # yMov (int): The y movement of the ball

    newPosition = pygame.math.Vector2(0, 0)             # newPosition (Vector2): The new position of the ball
    distanceLength = 100                                # distanceLength (int): The length of the distance between the ball and the target

    time = 0                                            # time (int): The time of the ball

    def __init__(self, window): 
        self.window = window                                # Set the window of the ball to the window of the game window
       
    def update(self, delta_time, klicks, gravity): 
        if klicks > 1: 
            self.movement(delta_time, gravity)                  # Update the movement of the ball
        self.draw()                                             # Draw the ball to the window
       

    def draw(self):
        pygame.draw.circle(self.window, "red", (self.position), self.RADIUS)                                # Draw the ball to the window

    def movement(self, delta_time, gravity):
        self.time += 1                                                                                      # Update the time of the ball
        self.time /= 1000000                                                                                # Divide the time by 1000000 to get the time in
        
        
        self.vecGravity = pygame.math.Vector2(0.0, float(gravity))                                          # Set the gravity vector of the ball
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
        