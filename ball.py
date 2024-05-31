# Import necessary libraries and modules
import pygame
import math
import obstacle

class Ball: 

    radius = 15                                         
    position = pygame.math.Vector2(0, 0)              
    target = pygame.math.Vector2(0, 0)                  
    impulse = pygame.math.Vector2(0, 0)                
    velocity = pygame.math.Vector2(0, 0)
    impulseNormal = pygame.math.Vector2(0, 0)          
    impulseStrength = 0                                 
    direction = pygame.math.Vector2(0, 0)               
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
    rolling = False
    onLine = False

    
    def __init__(self, screen): 
        self.screen = screen                                
       
    def update(self, delta_time, klicks, obstacle1): 
        if klicks > 1: 
            self.move(delta_time, klicks)
            collision = self.detectCollision(obstacle1)
            if  collision:
                self.handleCollision()                     
        self.draw()                                             
       
    def draw(self):
        pygame.draw.circle(self.screen, "red", (self.position), self.radius)                                

    def move(self, delta_time, klicks):

        if klicks == 2 and self.impulseOnlyOnce:
            self.impulse = pygame.math.Vector2(self.target) - pygame.math.Vector2(self.position)
            self.impulseOnlyOnce = False

        vecGravity = pygame.math.Vector2(0.0, float(self.GRAVITY))
        
        if self.collisionCounter < 1:
            self.acceleration = vecGravity + self.impulse

        else:
            self.acceleration = vecGravity
            
        self.velocity = self.velocity + self.acceleration * delta_time
        self.position = self.position + (self.velocity * delta_time) + (0.5 * self.acceleration * delta_time**2)  
        
    
    def detectCollision(self, obstacle1):

        collision = False
        #collisionDirection = pygame.math.Vector2(0, 0)
        
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
        
        if self.lineCollisionPoint.x > self.lineStart.x and self.lineCollisionPoint.y < self.lineStart.y:
            if self.lineCollisionPoint.x < self.lineEnd.x and self.lineCollisionPoint.y > self.lineEnd.y:
                self.onLine = True
        else:
            self.onLine = False

        if collisionDistance < 1 and self.onLine:
            collision = True
            self.collisionCounter += 1

        return collision


    def handleCollision(self):

        if self.ballObjectDistance < self.distanceTreshold and self.velocity.length() < self.velocityTreshold or self.rolling:
            self.rolling = True
            point1 = pygame.math.Vector2(0,1000)
            point2 = pygame.math.Vector2(800,1000)
            vec1 = point2 - point1
            alpha = vec1.angle_to(self.directionVec)
            hight = self.directionVec.length() * math.sin(alpha)
            self.acceleration = 0
            rollVelocity = math.sqrt(self.GRAVITY * hight * 2)
            rollDirection = -self.directionVec.normalize()
            self.velocity = rollDirection * rollVelocity
            normalForce = self.GRAVITY
            frictionStrength = normalForce * self.frictionCoefficient
            self.friction = -rollDirection * frictionStrength
            self.velocity -= self.friction
            self.position += (-5, -5)

            if self.onLine == False:
                self.rolling = False
                
        else:
            self.velocity = -self.velocity