# Import necessary libraries and modules
import pygame
import math
import obstacle

class Ball: 

    radius = 15                                         # RADIUS (int): The radius of the ball
    position = pygame.math.Vector2(0, 0)              # position (Vector2): The position of the ball
    target = pygame.math.Vector2(0, 0)                  # target (Vector2): The target position of the ball
    impulse = pygame.math.Vector2(0, 0)                # distance (Vector2): The distance between the ball and the target
    velocity = pygame.math.Vector2(0, 0)
    impulseNormal = pygame.math.Vector2(0, 0)          # impulseNormal
    impulseStrength = 0                                 # impulseStrength (int): The strength of the impulse
    direction = pygame.math.Vector2(0, 0)               # direction (Vector2): The direction of the ball
    acceleration = pygame.math.Vector2(0, 0)
    friction = pygame.math.Vector2(0, 0)
    GRAVITY = 981
    #metall ball on wood
    frictionCoefficient = 0.6
    impulseOnlyOnce = True
    lineCollisionPoint = pygame.math.Vector2(0, 0)
    lineStart = pygame.math.Vector2(0, 0)
    lineEnd = pygame.math.Vector2(0, 0)
    directionVec = pygame.math.Vector2(0, 0)
    scalar = 0
    collisionDistance = 0
    collisionCounter = 0
    collisionAngle = 0.0
    ballObjectDistance = collisionDistance
    distanceTreshold = 10.0
    velocityTreshold = 300.0

    
    def __init__(self, screen): 
        self.screen = screen                                # Set the window of the ball to the window of the game window
       
    def update(self, delta_time, klicks, obstacle1): 
        if klicks > 1: 
            self.move(delta_time, klicks)
            collision = self.detectCollision(obstacle1)
            if  collision:
                self.handleCollision()                     
        self.draw()                                             # Draw the ball to the window
       
    def draw(self):
        pygame.draw.circle(self.screen, "red", (self.position), self.radius)                                # Draw the ball to the window

    def move(self, delta_time, klicks):

        if klicks == 2 and self.impulseOnlyOnce:
            self.impulse = pygame.math.Vector2(self.target) - pygame.math.Vector2(self.position)
            self.impulseOnlyOnce = False

        vecGravity = pygame.math.Vector2(0.0, float(self.GRAVITY))
        normalForce = vecGravity
        self.friction = normalForce * self.frictionCoefficient
        self.frictionAmount = math.sqrt(((self.friction.x)**2)+((self.friction.y)**2))

        
        if self.collisionCounter < 1:
            self.acceleration = vecGravity + self.impulse
        else:
            self.acceleration = vecGravity
            

        self.velocity = self.velocity + self.acceleration * delta_time
        self.position = self.position + (self.velocity * delta_time) + (0.5 * self.acceleration * delta_time**2)  
        
    
    def detectCollision(self, obstacle1):

        collision = False
        collisionDirection = pygame.math.Vector2(0, 0)
        
       
        self.lineStart = pygame.math.Vector2(obstacle1.startX, obstacle1.startY)
        a = self.position - self.lineStart
        self.lineEnd = pygame.math.Vector2(obstacle1.endX, obstacle1.endY)
        self.directionVec = self.lineEnd - self.lineStart
        #directionVec = directionVec.normalize()
        numerator = a * self.directionVec
        denominator = (math.sqrt(((self.directionVec.x)**2)+((self.directionVec.y)**2)))**2
        self.scalar = numerator / denominator
        #calculates the Collisionpoint
        self.lineCollisionPoint = self.lineStart + (self.scalar * self.directionVec)
        distanceVec = self.position - self.lineCollisionPoint
        i = pygame.math.Vector2(0, 0)
        i.x = math.sqrt(((distanceVec.x)**2)+((distanceVec.x)**2))
        i.y = math.sqrt(((distanceVec.y)**2)+((distanceVec.y)**2))
        collisionDistance = i.length() - self.radius
        
        
        if self.position.x - self.radius < 0:
            collision = True
            self.collisionCounter += 1
        if self.position.x + self.radius > self.screen.get_width():
            collision = True
            self.collisionCounter += 1
        if self.position.y - self.radius < 0:
            collision = True
            self.collisionCounter += 1
        if self.position.y + self.radius > self.screen.get_height():
            collision = True
            self.collisionCounter += 1
        

        onLine = False
        if self.lineCollisionPoint.x > self.lineStart.x and self.lineCollisionPoint.y < self.lineStart.y:
            if self.lineCollisionPoint.x < self.lineEnd.x and self.lineCollisionPoint.y > self.lineEnd.y:
                onLine = True

        #if self.lineCollisionPoint.length() < self.lineEnd.length():
        #    onLine = True

        if collisionDistance < 1 and onLine:
            collision = True
            self.collisionCounter += 1

        
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

        if self.ballObjectDistance < self.distanceTreshold and self.velocity.length() < self.velocityTreshold:
            self.acceleration = 0
            velocityStrength = self.velocity.length()
            surfaceDirectionVec = pygame.math.Vector2(0, 0)
            surfaceDirectionVec = surfaceDirectionVec * velocityStrength
            self.velocity = surfaceDirectionVec
            self.position += (-5, -5)

        else:
            self.velocity = -self.velocity