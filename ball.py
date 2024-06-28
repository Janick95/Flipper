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
    colorCounter = 0
    # steel
    density = 7.85 #g/cm

    #Player Score
    scoreCounter=0

    
    def __init__(self, screen):                             
        self.screen = screen
       
    def update(self, delta_time, klicks, obstacles):    
        if klicks > 1:                                      
            self.move(delta_time, klicks)                  
            collision, currentObstacle, collisionRim = self.detectCollision(obstacles)     
            if  collision:                                  
                self.handleCollision(currentObstacle, collisionRim)                      
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
        #self.velocity = self.velocity / (delta_time * 1000) + self.acceleration * delta_time
        self.position = self.position + (self.velocity * delta_time) + (0.5 * self.acceleration * delta_time**2)      
        
    def detectLine(self, obstacle, collision, direction_to_collide):
        self.lineStart = pygame.math.Vector2(obstacle.start_pos)
        self.lineEnd = pygame.math.Vector2(obstacle.end_pos)
        a = self.position - self.lineStart
        self.directionVec = self.lineEnd - self.lineStart
        #self.directionVec = self.directionVec.normalize()
        numerator = a * self.directionVec                                                                                       
        denominator = (math.sqrt(((self.directionVec.x)**2)+((self.directionVec.y)**2)))**2                                     
        self.scalar = numerator / denominator

        self.lineCollisionPoint = self.lineStart + (self.scalar * self.directionVec)                                            
        distanceVec = self.position - self.lineCollisionPoint                                                                   
        i = pygame.math.Vector2(0, 0)                                                                                           
        i.x = math.sqrt(((distanceVec.x)**2)+((distanceVec.x)**2))
        i.y = math.sqrt(((distanceVec.y)**2)+((distanceVec.y)**2))
        collisionDistance = i.length() - self.radius                 
        #print(collisionDistance)
        #if self.lineCollisionPoint.x >= self.lineStart.x and self.lineCollisionPoint.y <= self.lineStart.y:                       
        #    if self.lineCollisionPoint.x <= self.lineEnd.x and self.lineCollisionPoint.y >= self.lineEnd.y:
        #        self.onLine = True
        #else:
        #    self.onLine = False

        if self.lineStart.x <= self.lineCollisionPoint.x <= self.lineEnd.x or self.lineStart.x >= self.lineCollisionPoint.x >= self.lineEnd.x:
            #print("x works")
            if self.lineStart.y <= self.lineCollisionPoint.y <= self.lineEnd.y or self.lineStart.y >= self.lineCollisionPoint.y >= self.lineEnd.y:
                self.onLine = True  
        else:
            self.onLine = False
        #print(self.onLine)
        if self.lineCollisionPoint.x == self.lineStart.x and self.lineCollisionPoint.y == self.lineStart.y:
            collision = self.detectPoint(obstacle, collision, direction_to_collide)
        elif self.lineCollisionPoint.y == self.lineEnd.x and self.lineCollisionPoint.y == self.lineEnd.y:
            collision = self.detectPoint(obstacle, collision, direction_to_collide)
              
        elif collisionDistance < 1 and self.onLine and direction_to_collide:
            collision = True
            self.collisionCounter += 1
            #print("lineCollision")

        return collision
    
    def addScore(self, points):
        self.scoreCounter += points

    def detectPoint(self, currentObstacle, collision, direction_to_collide):
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
            collisionDistance = i.length() - self.radius

        print(collisionDistance)
        if collisionDistance < 1 and direction_to_collide:
            collision = True
            self.collisionCounter += 1
            # Change the obstacle's color based on the collision count
            currentObstacle.change_color_on_collision()
            self.addScore(10)  # Add score by 10 points for each point collision
            print("pointCollision")

        return collision


    def detectCollision(self, obstacles):

        collision = False
        currentObstacle = None
        collisionRim = 0
        ball_direction = self.velocity
        direction_to_collide = False

        for temporaryObstacle in obstacles:
            if isinstance(temporaryObstacle, obstacle.LineObstacle):
                normal_vec = temporaryObstacle.normal_vec
                angle = normal_vec.angle_to(ball_direction)
                
                if 0 <= angle <= 90 or 0 >= angle >= -90:
                    direction_to_collide = True
                else:
                    direction_to_collide = False
                collision = self.detectLine(temporaryObstacle, collision, direction_to_collide)
                currentObstacle = temporaryObstacle
                if not collision:
                    normal_vec = pygame.math.Vector2(normal_vec.x, -normal_vec.y)
                    angle = normal_vec.angle_to(ball_direction)
                    if 0 <= angle <= 90 or 0 >= angle >= -90:
                        direction_to_collide = True
                        collision = self.detectLine(currentObstacle, collision, direction_to_collide)
                        currentObstacle = temporaryObstacle

            if isinstance(temporaryObstacle, obstacle.CircleObstacle):
                normal_vec = (self.position - temporaryObstacle.position)
                angle = normal_vec.angle_to(ball_direction)
                if 0 <= angle <= 90 or 0 >= angle >= -90:
                    direction_to_collide = True
                else:
                    direction_to_collide = False

                collision = self.detectPoint(temporaryObstacle, collision, direction_to_collide)
                currentObstacle = temporaryObstacle

            #braucht noch ein ständiges update um die kollisionslinien auf dem rechteck zu platzieren
            #if isinstance(temporaryObstacle, obstacle.RectObstacle) or isinstance(temporaryObstacle, obstacle.FlipperObstacle):
                
            #    rectWidth = temporaryObstacle.rect[2]
            #    rectHeight = temporaryObstacle.rect[3]

            #    corner_top_left = pygame.math.Vector2(temporaryObstacle.rect[0], temporaryObstacle.rect[1])
            #    corner_bottom_left = pygame.math.Vector2(corner_top_left.x, corner_top_left.y + rectHeight)
            #    corner_top_right = pygame.math.Vector2(corner_top_left.x + rectWidth, corner_top_left.y)
            #    corner_bottom_right = pygame.math.Vector2(corner_top_left.x + rectWidth, corner_top_left.y + rectHeight)

            #    edge_left = obstacle.LineObstacle("alpha = 0", corner_bottom_left, corner_top_left, 0)
                #edge_left.draw(self.screen)
            #    edge_top = obstacle.LineObstacle("alpha = 0", corner_top_left, corner_top_right, 0)
                #edge_top.draw(self.screen)
            #    edge_right = obstacle.LineObstacle("alpha = 0", corner_top_right, corner_bottom_right, 0)
                #edge_right.draw(self.screen)
            #    edge_bottom = obstacle.LineObstacle("alpha = 0", corner_bottom_right, corner_bottom_left, 0)
                #edge_bottom.draw(self.screen)

            #    if 0 <= angle <= 90 or 0 >= angle >= -90:
            #        direction_to_collide = True
            #    else:
            #        direction_to_collide = False

            #    collision = self.detectLine(edge_left, collision, direction_to_collide)
            #    collision = self.detectLine(edge_top, collision, direction_to_collide)
            #    collision = self.detectLine(edge_right, collision, direction_to_collide)
            #    collision = self.detectLine(edge_bottom, collision, direction_to_collide)
            #    currentObstacle = temporaryObstacle

            #if isinstance(temporaryObstacle, obstacle.Ball):
            #    normal_vec = (self.position - temporaryObstacle.position)
            #    angle = normal_vec.angle_to(ball_direction)
            #    if 0 <= angle <= 90 or 0 >= angle >= -90:
            #        direction_to_collide = True
            #    else:
            #       direction_to_collide = False

            #    collision = self.detectPoint(temporaryObstacle, collision, direction_to_collide)
            #    currentObstacle = temporaryObstacle
                
        #left      
        if self.position.x - self.radius < 0:
            startVec = pygame.math.Vector2(0, 0)
            endVec = pygame.math.Vector2(0, self.screen.get_height())
            direction_vec = endVec - startVec
            normal_vec = pygame.math.Vector2(-direction_vec.y, direction_vec.x)
            angle = normal_vec.angle_to(ball_direction)
            if 0 <= angle <= 90 or 0 >= angle >= -90:
                direction_to_collide = True
            else:
                direction_to_collide = False

            if direction_to_collide:
                collision = True
            self.collisionCounter += 1
            currentObstacle = None
            collisionRim = 1
        #right
        if self.position.x + self.radius > self.screen.get_width():
            startVec = pygame.math.Vector2(self.screen.get_width(),self.screen.get_height())
            endVec = pygame.math.Vector2(self.screen.get_width(), 0)
            direction_vec = endVec - startVec
            normal_vec = pygame.math.Vector2(-direction_vec.y, direction_vec.x)
            angle = normal_vec.angle_to(ball_direction)
            if 0 <= angle <= 90 or 0 >= angle >= -90:
                direction_to_collide = True
            else:
                direction_to_collide = False

            if direction_to_collide:
                collision = True
            self.collisionCounter += 1
            currentObstacle = None
            collisionRim = 2
        #top
        if self.position.y - self.radius < 0:
            startVec = pygame.math.Vector2(self.screen.get_width(), 0)
            endVec = pygame.math.Vector2(0, 0)
            direction_vec = endVec - startVec
            normal_vec = pygame.math.Vector2(-direction_vec.y, direction_vec.x)
            angle = normal_vec.angle_to(ball_direction)
            if 0 <= angle <= 90 or 0 >= angle >= -90:
                direction_to_collide = True
            else:
                direction_to_collide = False

            if direction_to_collide:
                collision = True
            self.collisionCounter += 1
            currentObstacle = None
            collisionRim = 3
        #bottom
        if self.position.y + self.radius > self.screen.get_height():
            startVec = pygame.math.Vector2(0, self.screen.get_height())
            endVec = pygame.math.Vector2(self.screen.get_width(), self.screen.get_height())
            direction_vec = endVec - startVec
            normal_vec = pygame.math.Vector2(-direction_vec.y, direction_vec.x)
            angle = normal_vec.angle_to(ball_direction)
            if 0 <= angle <= 90 or 0 >= angle >= -90:
                direction_to_collide = True
            else:
                direction_to_collide = False

            if direction_to_collide:
                
                collision = True
            self.collisionCounter += 1
            currentObstacle = None
            collisionRim = 4

        return collision, currentObstacle, collisionRim                                                          
        

    def handleCollision(self, currentObstacle, collisionRim):

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
            
        if currentObstacle == None:
            startVec = pygame.math.Vector2(0, 0)
            endVec = pygame.math.Vector2(0, 0)
            normal = pygame.math.Vector2(0, 0)
        
            if collisionRim == 1:
                startVec = pygame.math.Vector2(0, 0)
                endVec = pygame.math.Vector2(0, self.screen.get_height())
            if collisionRim == 2:
                startVec = pygame.math.Vector2(self.screen.get_width(),self.screen.get_height())
                endVec = pygame.math.Vector2(self.screen.get_width(), 0)
            if collisionRim == 3:
                startVec = pygame.math.Vector2(self.screen.get_width(), 0)
                endVec = pygame.math.Vector2(0, 0)
            if collisionRim == 4:
                startVec = pygame.math.Vector2(0, self.screen.get_height())
                endVec = pygame.math.Vector2(self.screen.get_width(), self.screen.get_height())

            self.delta = endVec - startVec
            lineLength = self.delta.length()
            normal.x = self.delta.y / lineLength
            normal.y = -self.delta.x / lineLength
            dot_product = self.velocity.x * normal.x + self.velocity.y * normal.y
            self.velocity.x -= 2 * dot_product * normal.x
            self.velocity.y -= 2 * dot_product * normal.y 

        elif isinstance(currentObstacle, obstacle.LineObstacle):
            surface_vec = currentObstacle.end_pos - currentObstacle.start_pos
            surface_vec_amount.x = math.sqrt(((surface_vec.x)**2)+((surface_vec.y)**2))
            
            normal_vec = currentObstacle.normal_vec
            normal_vec_amount.x = math.sqrt(((normal_vec.x)**2)+((normal_vec.y)**2))
            
            velocity_surface_projection = ((surface_vec * self.velocity) / (surface_vec_amount**2)) * surface_vec
            velocity_normal_projection = ((normal_vec * self.velocity) / (normal_vec_amount**2)) * normal_vec

            self.velocity = velocity_surface_projection - velocity_normal_projection

            #self.delta = currentObstacle.end_pos - currentObstacle.start_pos
            #lineLength = self.delta.length()
            #direction = self.delta / lineLength
            #self.normal = pygame.math.Vector2(-direction.y, direction.x)
            #dot_product = self.velocity.dot(self.normal)
            #self.velocity -= 2 * dot_product * self.normal

            #self.delta = currentObstacle.end_pos - currentObstacle.start_pos
            #lineLength = self.delta.length()
            #self.normal.x = self.delta.y / lineLength
            #self.normal.y = -self.delta.x / lineLength
            #dot_product = self.velocity.x * self.normal.x + self.velocity.y * self.normal.y
            #self.velocity.x -= 2 * dot_product * self.normal.x
            #self.velocity.y -= 2 * dot_product * self.normal.y

        elif isinstance(currentObstacle, obstacle.CircleObstacle):
            normal_vec = (self.position - currentObstacle.position)
            normal_vec_amount = math.sqrt(((normal_vec.x)**2)+((normal_vec.y)**2))

            surface_vec = pygame.math.Vector2(normal_vec.y, -normal_vec.x)
            surface_vec_amount = math.sqrt(((surface_vec.x)**2)+((surface_vec.y)**2))

            velocity_surface_projection = ((surface_vec * self.velocity) / (surface_vec_amount**2)) * surface_vec
            velocity_normal_projection = ((normal_vec * self.velocity) / (normal_vec_amount**2)) * normal_vec

            self.velocity = velocity_surface_projection - velocity_normal_projection
            #direction = self.position - currentObstacle.position
            #self.normal = direction.normalize()
            #dot_product = self.velocity.dot(self.normal)
            #self.velocity -= 2 * dot_product * self.normal


        elif isinstance(currentObstacle, obstacle.Ball):

            ball_volume = 4/3 * math.pi * self.radius**3
            ball_mass = ball_volume * self.density

            obstacle_volume = 4/3 * math.pi * currentObstacle.radius**3
            obstacle_mass = obstacle_volume * currentObstacle.density

            #calculation for the own ball
            normal_vec = (self.position - currentObstacle.position)
            normal_vec_amount = math.sqrt(((normal_vec.x)**2)+((normal_vec.y)**2))
            surface_vec = pygame.math.Vector2(normal_vec.y, -normal_vec.x)
            surface_vec_amount = math.sqrt(((surface_vec.x)**2)+((surface_vec.y)**2))
            velocity_surface_projection = ((surface_vec * self.velocity) / (surface_vec_amount**2)) * surface_vec
            velocity_normal_projection = ((normal_vec * self.velocity) / (normal_vec_amount**2)) * normal_vec

            #calculation for the other ball
            obstacle_normal_vec = (currentObstacle.position - self.position)
            obstacle_normal_vec_amount = math.sqrt(((obstacle_normal_vec.x)**2)+((obstacle_normal_vec.y)**2))
            obstacle_surface_vec = pygame.math.Vector2(obstacle_normal_vec.y, -obstacle_normal_vec.x)
            obstacle_surface_vec_amount = math.sqrt(((obstacle_surface_vec.x)**2)+((obstacle_surface_vec.y)**2))
            #obstacle_velocity_surface_projection = ((obstacle_surface_vec * self.velocity) / (obstacle_surface_vec_amount**2)) * obstacle_surface_vec
            obstacle_velocity_normal_projection = ((obstacle_normal_vec * self.velocity) / (obstacle_normal_vec_amount**2)) * obstacle_normal_vec


            new_velocity_normal_projection = 2 * ((ball_mass * velocity_normal_projection + obstacle_mass * obstacle_velocity_normal_projection)/(ball_mass + obstacle_mass)) - velocity_surface_projection

            self.velocity = velocity_surface_projection + new_velocity_normal_projection

            #self.velocity = -self.velocity