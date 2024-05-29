# Import necessary libraries and modules
import pygame
import ball
import window
import pygame_gui
import simparam
import pygame_widgets
import obstacle

class Game:

    pygame.init()

    # Define the main game loop function
    def game():
                
        clock = pygame.time.Clock()                                                                                                                              # Create a clock object to keep track of time
        screen1 = window.Window().screen                                                                                                                                # Initialize the game window
        klicks = 0                                                                                                                                                  # Number of mouse clicks
        drawUI = False
                
        #GameObjects
        #############

        obstacle1 = obstacle.Obstacle(screen1, 300, 600, 600, 250)
        ball1 = ball.Ball(screen1)
        

        #############
      
        #Compute data
        running = True
        while running:                                      # Game loop
            # Timecalculation mm per second
            delta_time = clock.tick(60)/1000
            
            events = pygame.event.get()
            for event in events:               # Check for events
                if event.type == pygame.QUIT: 
                    running = False 
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                    running = False
                elif klicks == 0 and event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == pygame.BUTTON_LEFT: 
                        ball1.position = event.pos          # Set the position of the ball to the mouse position
                        klicks = 1 
                elif klicks == 1 and event.type == pygame.MOUSEBUTTONDOWN: 
                    if event.button == pygame.BUTTON_LEFT: 
                        ball1.target = event.pos            # Set the target position of the ball to the mouse position
                        klicks = 2
                #Show SimParam
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI != True:   
                    drawUI = True 
                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#gravity_text_entry" and drawUI:     
                    #ball1.gravityAcceleration = int(event.text)
                    simparam.SimParam.show_text(screen1, ball1.position, ball1.acceleration, ball1.GRAVITY)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI: 
                    drawUI = False 
                ############

                
                
        #Draw graphics
            #simparam1.Manager.update(delta_time)
            screen1.fill((255, 255, 255))
            obstacle1.draw()
            
            if drawUI:
                simparam.SimParam.show_UI(screen1, ball1.position, ball1.acceleration, ball1.GRAVITY, ball1)
                pygame_widgets.update(events)

            if klicks > 0:
                ball1.update(delta_time, klicks, obstacle1)
            pygame.display.update()                         # Update the display
    
        pygame.quit()                                       # Quit the game

    game()                                                  # Call the game loop function

   
   