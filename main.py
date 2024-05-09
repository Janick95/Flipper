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
    

    def game():
        
        
        clock = pygame.time.Clock()
        window1 = window.Window()
        klicks = 0
        #GameObjects
        #############


        ball1 = ball.Ball(window1.window)
        

        #############
    
        #Compute data
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif klicks == 0 and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        ball1.position = event.pos
                        klicks = 1
                elif klicks == 1 and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        ball1.target = event.pos
                        klicks = 2

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



   
   