# Import necessary libraries and modules
import pygame
import math
import obstacle

class Ball: 

    radius = 15                                             # Radius of the ball
    position = pygame.math.Vector2(0, 0)                    # Initial position of the ball
    target = pygame.math.Vector2(0, 0)                      # Target position for the ball
    impulse = pygame.math.Vector2(0, 0)                     # Impulse applied to the ball
    velocity = pygame.math.Vector2(0, 0)                    # Velocity of the ball
    impulseNormal = pygame.math.Vector2(0, 0)               # Normal impulse applied to the ball
    impulseStrength = 0                                     # Strength of the impulse
    direction = pygame.math.Vector2(0, 0)                   # Direction of the ball's movement
    acceleration = pygame.math.Vector2(0, 0)                # Acceleration of the ball
    friction = pygame.math.Vector2(0, 0)                    # Friction applied to the ball
    GRAVITY = 981                                           # Gravitational force acting on the ball
    # Metallic ball on wood
    frictionCoefficient = 0.6                               # Coefficient of friction between the ball and the surface
    impulseOnlyOnce = True                                  # Flag to control whether the impulse is applied only once
    lineCollisionPoint = pygame.math.Vector2(0, 0)          # Point of collision with a line
    lineStart = pygame.math.Vector2(0, 0)                   # Start point of the line
    lineEnd = pygame.math.Vector2(0, 0)                     # End point of the line
    directionVec = pygame.math.Vector2(0, 0)                # Vector representing the direction of the line
    scalar = 0                                              # Scalar value for calculating the collision point
    collisionDistance = 0                                   # Distance between the ball and the collision point
    collisionCounter = 0                                    # Counter for tracking collisions
    collisionAngle = 0.0                                    # Angle of collision
    ballObjectDistance = collisionDistance                  # Distance between the ball and the object
    distanceTreshold = 10.0                                 # Distance threshold for detecting collisions
    velocityTreshold = 300.0                                # Velocity threshold for detecting collisions
    rolling = False                                         # Flag to indicate whether the ball is rolling
    onLine = False                                          # Flag to indicate whether the ball is on a line

    
    def __init__(self, screen):                             
        self.screen = screen                                
       
    def update(self, delta_time, klicks, obstacle1):    
        if klicks > 1:                                      # if the number of clicks is greater than 1
            self.move(delta_time, klicks)                   # move the ball based on the given delta time and klicks
            collision = self.detectCollision(obstacle1)     # detect a collision with the given obstacle1
            if  collision:                                  # if a collision is detected
                self.handleCollision(obstacle1)                      # handle the collision
        self.draw()                                         # draw the ball on the screen    
       
    def draw(self):
        # Draw a red circle on the screen at the position with the specified radius
        pygame.draw.circle(self.screen, "red", (self.position), self.radius)                                                                     

    def move(self, delta_time, klicks):
        
        # If double-click is detected and impulse is to be applied only once
        if klicks == 2 and self.impulseOnlyOnce:                 
            # Calculate the impulse vector from the position to the target                                                   
            self.impulse = pygame.math.Vector2(self.target) - pygame.math.Vector2(self.position)  
            # Ensure impulse is applied only once                  
            self.impulseOnlyOnce = False                                                                            
        # Define the gravity vector
        vecGravity = pygame.math.Vector2(0.0, float(self.GRAVITY))                                                  
        # If no collision has been detected
        if self.collisionCounter < 1:
            # Set acceleration as the sum of gravity and impulse                                                                               
            self.acceleration = vecGravity + self.impulse                                                           

        else:
            # Set acceleration as just gravity if collision has been detected
            self.acceleration = vecGravity                                                                          

        # Update velocity with acceleration over time    
        self.velocity = self.velocity + self.acceleration * delta_time
        # Update position with velocity and acceleration over time                                              
        self.position = self.position + (self.velocity * delta_time) + (0.5 * self.acceleration * delta_time**2)      
        
    
    def detectCollision(self, obstacle1):

        # Initialize collision detection as False
        collision = False                                                                                                       
        #collisionDirection = pygame.math.Vector2(0, 0)
        
        # Define the start and end points of the obstacle line
        self.lineStart = pygame.math.Vector2(obstacle1.startX, obstacle1.startY)                                                
        self.lineEnd = pygame.math.Vector2(obstacle1.endX, obstacle1.endY)
        # Vector from the line start to the current position
        a = self.position - self.lineStart                                                                                      
        # Direction vector of the line
        self.directionVec = self.lineEnd - self.lineStart                                                                       
        #directionVec = directionVec.normalize()
        # Calculate the scalar projection of vector 'a' onto the direction vector
        numerator = a * self.directionVec                                                                                       
        denominator = (math.sqrt(((self.directionVec.x)**2)+((self.directionVec.y)**2)))**2                                     
        self.scalar = numerator / denominator

        # Calculate the collision point on the line
        self.lineCollisionPoint = self.lineStart + (self.scalar * self.directionVec)                                            
        # Vector from the position to the collision point    
        distanceVec = self.position - self.lineCollisionPoint                                                                   
        # Create a temporary vector 'i' for distance calculation
        i = pygame.math.Vector2(0, 0)                                                                                           
        i.x = math.sqrt(((distanceVec.x)**2)+((distanceVec.x)**2))
        i.y = math.sqrt(((distanceVec.y)**2)+((distanceVec.y)**2))
        # Calculate the collision distance
        collisionDistance = i.length() - self.radius                                                                            
        
        # Check for collisions with the screen boundaries
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
        
        # Check if the collision point lies on the obstacle line segment
        if self.lineCollisionPoint.x > self.lineStart.x and self.lineCollisionPoint.y < self.lineStart.y:                       
            if self.lineCollisionPoint.x < self.lineEnd.x and self.lineCollisionPoint.y > self.lineEnd.y:
                self.onLine = True
        else:
            self.onLine = False

        # Detect collision with the obstacle if within a small distance and on the line
        if collisionDistance < 1 and self.onLine:                                                                               
            collision = True
            self.collisionCounter += 1

        return collision


    def handleCollision(self, obstacle1):

        # Check if the object is close to the obstacle and moving slowly, or if it's rolling
        if self.ballObjectDistance < self.distanceTreshold and self.velocity.length() < self.velocityTreshold or self.rolling:  
            # Set the rolling state
            self.rolling = True                                                                                                 
            # Define points for calculating the slope of the line
            point1 = pygame.math.Vector2(0,1000)                                                                                
            point2 = pygame.math.Vector2(800,1000)
            
            vec1 = point2 - point1                                                                                              
            
            alpha = vec1.angle_to(self.directionVec)                                                                            
            
            height = self.directionVec.length() * math.sin(alpha)                                                               
           
            self.acceleration = 0                                                                                               
           
            rollVelocity = math.sqrt(self.GRAVITY * height * 2)                                                                 
            
            rollDirection = -self.directionVec.normalize()                                                                      
            
            self.velocity = rollDirection * rollVelocity                                                                        
            
            normalForce = self.GRAVITY                                                                                          
            
            frictionStrength = normalForce * self.frictionCoefficient                                                           
            
            self.friction = -rollDirection * frictionStrength                                                                   
            
            self.velocity -= self.friction                                                                                      
            
            self.position += (-5, -5)                                                                                           

            # If not on the line anymore, stop rolling
            if self.onLine == False:                                                                                            
                self.rolling = False

        # If not rolling, simply invert the velocity upon collision        
        else:                                                                                                                   
            
            dx = obstacle1.endX - obstacle1.startX
            dy = obstacle1.endY - obstacle1.startY
            lineLength = math.sqrt(dx**2 + dy**2)
            normal_x = dy / lineLength
            normal_y = -dx / lineLength
            dot_product = self.velocity.x * normal_x + self.velocity.y * normal_y
            self.velocity.x -= 2 * dot_product * normal_x
            self.velocity.y -= 2 * dot_product * normal_y 

            #self.velocity = -self.velocity