# Import necessary libraries and modules
import pygame
import ball
import window
import pygame_gui
import simparam

class Game:

    pygame.init()

    # Define the main game loop function
    def game():
                
        clock = pygame.time.Clock()                                                                                                                              # Create a clock object to keep track of time
        screen1 = window.Window().screen                                                                                                                                # Initialize the game window
        klicks = 0                                                                                                                                                  # Number of mouse clicks
        drawUI = False                                                                                                                                              # Draw the UI or not
        simparam1 = simparam.SimParam()
                
        #GameObjects
        #############


        ball1 = ball.Ball(screen1)                   # Create a ball object
        

        #############
      
        #Compute data
        running = True 
        while running:                                      # Game loop
            
            delta_time = clock.tick(60)/1000                # Compute the delta time
            for event in pygame.event.get():                # Check for events
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
                    simparam.SimParam.show_text(screen1, ball1.position, ball1.impulseAcceleration, ball1.gravityAcceleration)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI: 
                    drawUI = False 
                ############

                simparam1.Manager.process_events(event)     # Update the UIManager object
                
        #Draw graphics
            #simparam1.Manager.update(delta_time)
            screen1.fill((255, 255, 255))
            
            if drawUI: 
                simparam1.Manager.draw_ui(screen1)
                simparam.SimParam.show_text(screen1, ball.Ball.position, ball.Ball.impulseAcceleration, ball.Ball.gravityAcceleration)           # Draw the UI elements

            if klicks > 0:
                ball1.update(delta_time, klicks)   # Update the ball object
            pygame.display.update()                         # Update the display
    
        pygame.quit()                                       # Quit the game

    game()                                                  # Call the game loop function

   
   