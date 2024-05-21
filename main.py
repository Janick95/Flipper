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
        window1 = window.Window()                                                                                                                                   # Initialize the game window
        klicks = 0                                                                                                                                                  # Number of mouse clicks
        drawUI = False                                                                                                                                              # Draw the UI or not
        simparam1 = simparam.SimParam()
                
        #GameObjects
        #############


        ball1 = ball.Ball(window1.window)                   # Create a ball object
        

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
                    ball1.gravityAcceleration = int(event.text)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI: 
                    drawUI = False 
                ############

                simparam1.Manager.process_events(event)     # Update the UIManager object
                
        #Draw graphics
            simparam1.Manager.update(delta_time)            # Update the UIManager object
            window1.window.fill((255, 255, 255))            # Fill the window with white
            if drawUI: 
                simparam1.Manager.draw_ui(window1.window)             # Draw the UI elements

            if klicks > 0:
                ball1.update(delta_time, klicks)   # Update the ball object
            pygame.display.update()                         # Update the display
    
        pygame.quit()                                       # Quit the game

    game()                                                  # Call the game loop function

   
   