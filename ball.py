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
    # Metallic ball on wood
    frictionCoefficient = 0.6                               
    impulseOnlyOnce = True                                  
    lineCollisionPoint = pygame.math.Vector2(0, 0)
    collisionPoint = pygame.math.Vector2(0, 0)         
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
       
    def update(self, delta_time, klicks, obstacles):    
        if klicks > 1:                                      
            self.move(delta_time, klicks)                  
            collision, currentObstacle = self.detectCollision(obstacles)     
            if  collision:                                  
                self.handleCollision(currentObstacle)                      
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
        
    def detectLine(self, obstacle, collision):
        #collisionDirection = pygame.math.Vector2(0, 0)
        self.lineStart = pygame.math.Vector2(obstacle.start_pos)
        self.lineEnd = pygame.math.Vector2(obstacle.end_pos)
        a = self.position - self.lineStart                                                                                      
        self.directionVec = self.lineEnd - self.lineStart
        #directionVec = directionVec.normalize()
        numerator = a * self.directionVec                                                                                       
        denominator = (math.sqrt(((self.directionVec.x)**2)+((self.directionVec.y)**2)))**2                                     
        self.scalar = numerator / denominator

        self.lineCollisionPoint = self.lineStart + (self.scalar * self.directionVec)                                            
        distanceVec = self.position - self.lineCollisionPoint                                                                   
        i = pygame.math.Vector2(0, 0)                                                                                           
        i.x = math.sqrt(((distanceVec.x)**2)+((distanceVec.x)**2))
        i.y = math.sqrt(((distanceVec.y)**2)+((distanceVec.y)**2))
        collisionDistance = i.length() - self.radius                 

        #if self.lineCollisionPoint.x >= self.lineStart.x and self.lineCollisionPoint.y <= self.lineStart.y:                       
        #    if self.lineCollisionPoint.x <= self.lineEnd.x and self.lineCollisionPoint.y >= self.lineEnd.y:
        #        self.onLine = True
        #else:
        #    self.onLine = False

        if self.lineStart.x <= self.lineCollisionPoint.x <= self.lineEnd.x or self.lineStart.x >= self.lineCollisionPoint.x >= self.lineEnd.x:
            if self.lineStart.y <= self.lineCollisionPoint.y <= self.lineEnd.y or self.lineStart.y >= self.lineCollisionPoint.y >= self.lineEnd.y:
                self.onLine = True
        else:
            self.onLine = False

        
        if self.lineCollisionPoint.x == self.lineStart.x and self.lineCollisionPoint.y == self.lineStart.y:
            collision = self.detectPoint(obstacle, collision)
        elif self.lineCollisionPoint.y == self.lineEnd.x and self.lineCollisionPoint.y == self.lineEnd.y:
            collision = self.detectPoint(obstacle, collision)
                        
        elif collisionDistance < 1 and self.onLine:
            collision = True
            self.collisionCounter += 1
            print("line collision")

        return collision
    

    def detectPoint(self, currentObstacle, collision):
        if isinstance(currentObstacle, obstacle.CircleObstacle):
            distanceVec = self.position - currentObstacle.position
        elif isinstance(currentObstacle, obstacle.LineObstacle):
            distanceVec = self.position - currentObstacle.start_pos
        i = pygame.math.Vector2(0, 0)
        i.x = math.sqrt(((distanceVec.x)**2)+((distanceVec.x)**2))
        i.y = math.sqrt(((distanceVec.y)**2)+((distanceVec.y)**2))
        if isinstance(currentObstacle, obstacle.CircleObstacle):
            collisionDistance = i.length() - self.radius - currentObstacle.radius
        elif isinstance(currentObstacle, obstacle.LineObstacle):
            print("point line")
            collisionDistance = i.length() - self.radius

        if collisionDistance < 1:                                                                               
            collision = True
            self.collisionCounter += 1
            print("pointCollision")

        return collision


    def detectCollision(self, obstacles):

        collision = False
        currentObstacle = None

        for temporaryObstacle in obstacles:
            if isinstance(temporaryObstacle, obstacle.LineObstacle):
                collision = self.detectLine(temporaryObstacle, collision)
                currentObstacle = temporaryObstacle
                
            if isinstance(temporaryObstacle, obstacle.CircleObstacle):
                collision = self.detectPoint(temporaryObstacle, collision)
                currentObstacle = temporaryObstacle


            #Auskommentieren um zu Testen. Code funktioniert noch nicht
            #if isinstance(obstacles[index], obstacle.RectObstacle):
            #    if self.onLine:
            #        collision = self.detectLine(obstacle[index])
            #    elif self.lineCollisionPoint.x == self.lineStart.x and self.lineCollisionPoint.y == self.lineStart.y:
            #        if self.lineCollisionPoint.y == self.lineEnd.x and self.lineCollisionPoint.y == self.lineEnd.y:
            #            collision = self.detectPoint(obstacle[index])
                
        if self.position.x - self.radius < 0:
            print("rim collision")
            collision = True
            self.collisionCounter += 1
        if self.position.x + self.radius > self.screen.get_width():
            print("rim collision")
            collision = True
            self.collisionCounter += 1
        if self.position.y - self.radius < 0:
            print("rim collision")
            collision = True
            self.collisionCounter += 1
        if self.position.y + self.radius > self.screen.get_height():
            print("rim collision")
            collision = True
            self.collisionCounter += 1

        return collision, currentObstacle                                                           
        

    def handleCollision(self, currentObstacle):

        #if self.ballObjectDistance < self.distanceTreshold and self.velocity.length() < self.velocityTreshold or self.rolling:
        #    self.rolling = True                                                                                                 
        #    point1 = pygame.math.Vector2(0,1000)                                                                                
        #    point2 = pygame.math.Vector2(800,1000)
        #    vec1 = point2 - point1
        #    alpha = vec1.angle_to(self.directionVec)                                                                            
        #    height = self.directionVec.length() * math.sin(alpha)                                                               
        #    self.acceleration = 0                                                                                               
        #    rollVelocity = math.sqrt(self.GRAVITY * height * 2)                                                                 
        #    rollDirection = -self.directionVec.normalize()                                                                      
        #    self.velocity = rollDirection * rollVelocity                                                                        
        #    normalForce = self.GRAVITY                                                                                          
        #    frictionStrength = normalForce * self.frictionCoefficient                                                           
        #    self.friction = -rollDirection * frictionStrength                                                                   
        #    self.velocity -= self.friction
        #    self.position += (-5, -5)

        #    if self.onLine == False:                                                                                            
        #        self.rolling = False
    
        #else:
            
        
        dx = currentObstacle.end_pos.x - currentObstacle.start_pos.x
        dy = currentObstacle.end_pos.y - currentObstacle.start_pos.y
        lineLength = math.sqrt(dx**2 + dy**2)
        normal_x = dy / lineLength
        normal_y = -dx / lineLength
        dot_product = self.velocity.x * normal_x + self.velocity.y * normal_y
        self.velocity.x -= 2 * dot_product * normal_x
        self.velocity.y -= 2 * dot_product * normal_y 

            #self.velocity = -self.velocity