import sys
import pygame
import ball
import window

class Game:

    #Pygame Initialieren
    pygame.init()

#Parameters
    #Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    # Constants
    
    
    
    


    def game():
        
        

        #Ball Parameter
        
        clock = pygame.time.Clock()
        window1 = window.Window()
        #GameObjects
        #############


        ball1 = ball.Ball(window1.window, window1.WINDOWWIDTH/ 2, window1.WINDOWHEIGHT/ 2)


        #############
    
        #Compute data
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False

        #Draw graphics
            delta_time = clock.tick(60)/1000
            window1.window.fill((255, 255, 255))
            ball1.update(delta_time)
            pygame.display.update()
    
        pygame.quit()

    game()





























#velocity_x, velocity_y = 0, 0
  
   
#sys.exit()

    #physics

    #velocity_y += GRAVITY
    #velocity_x *= FRICTION
   # velocity_y *= FRICTION
    #x += velocity_x
   # y += velocity_y

    # Bounce off the walls
   # if x + radius >= WIDTH or x - radius <= 0:
   #     velocity_x *= -1
   # if y + radius >= HEIGHT or y - radius <= 0:
   #     velocity_y *= -1



   
   