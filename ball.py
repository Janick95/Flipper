# Import necessary libraries and modules
import pygame
import math
import obstacle

class Ball: 

    radius = 15                                         # RADIUS (int): The radius of the ball
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
       
    def update(self, delta_time, klicks, obstacle1): 
        if klicks > 1: 
            self.move(delta_time)
            collision = self.detectCollision(obstacle1)
            if  collision:
                self.handleCollision()                     
        self.draw()                                             # Draw the ball to the window
       
    def draw(self):
        pygame.draw.circle(self.screen, "red", (self.position), self.radius)                                # Draw the ball to the window

    def move(self, delta_time):
        
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
        self.position = self.position + pygame.math.Vector2(self.velocity * delta_time) + 0.5 * self.acceleration * delta_time   # Update the position of the ball
        
        #acceleration hinzufügen Streckenformel anwenden
    def detectCollision(self, obstacle1):

        collision = False
        collisionDirection = pygame.math.Vector2(0, 0)
        
       
        lineStart = pygame.math.Vector2(obstacle1.startX, obstacle1.startY)
        a = self.position - lineStart
        lineEnd = pygame.math.Vector2(obstacle1.endX, obstacle1.endY)
        b = lineEnd - lineStart.normalize()
        c = pygame.math.Vector2(0, 0)
        c.x = a.x * b.x
        c.y = a.y * b.y
        d = pygame.math.Vector2(0, 0)
        d.x = math.sqrt(((b.x)**2)+((b.x)**2))**2
        d.y = math.sqrt(((b.y)**2)+((b.y)**2))**2
        e = pygame.math.Vector2(0, 0)
        e.x = c.x / d.x
        e.y = c.y / d.y
        f = pygame.math.Vector2(0,0)
        f.x = e.x * b.x
        f.y = e.y * b.y
        lineCollisionPoint = f + lineStart
        g = self.position - lineCollisionPoint
        i = pygame.math.Vector2(0, 0)
        i.x = math.sqrt(((g.x)**2)+((g.x)**2))
        i.y = math.sqrt(((g.y)**2)+((g.y)**2))
        collisionDistance = i.length() - self.radius
        
        
        if self.position.x - self.radius < 0:
            collision = True
        if self.position.x + self.radius > self.screen.get_width():
            collision = True
        if self.position.y - self.radius < 0:
            collision = True
        if self.position.y + self.radius > self.screen.get_height():
            collision = True
        



        if collisionDistance < 1:
            collision = True

        
        #self.position.x = self.radius
        #    self.velocity.x = -self.velocity.x
        
        
        #self.position.x = 1-self.radius
        #    self.velocity.x = -self.velocity.x
        
        #self.position.y = self.radius
        #    self.velocity.y = -self.velocity.y
        
        #self.position.y = 1-self.radius
        #    self.velocity.y = -self.velocity.y
        
        
        # Check if the ball collides with the window
        #if self.position[0] < self.RADIUS or self.position[0] > self.screen.get_width() - self.RADIUS:
            #print("collision x")
            #collisionX = True
        #if self.position[1] < self.RADIUS or self.position[1] > self.screen.get_height() - self.RADIUS:
            #print("collision y")
            #collisionY = True


        # Check if the ball collides with an Object


        return collision
            
            #self.position[0] = self.position[0] - self.velocity[0] * 2
            #self.velocity[0] = -self.velocity[0]
            
            #self.position[1] = self.position[1] - self.velocity[1] * 2
            #self.velocity[1] = -self.velocity[1]


    def handleCollision(self):

        self.velocity = -self.velocity