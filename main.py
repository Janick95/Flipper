# Import necessary libraries and modules
import pygame
import ball
import window
import pygame_gui
import simparam
import pygame_widgets
import obstacle

from obstacle import ObstacleManager, CircleObstacle, RectObstacle, LineObstacle


class Game: 

    pygame.init()

    # Define the main game loop function
    def game(): 
                
        clock = pygame.time.Clock()                                             # Initialize the clock for controlling the frame rate                                                                                                                   
        screen1 = window.Window().screen                                        # Get the main game window screen                                                                                                                          
        klicks = 0                                                              # Initialize the number of clicks 
        drawUI = False                                                          # Initialize the flag for drawing UI elements
                
        #GameObjects
        #############
        obstacle_manager = ObstacleManager()

         # Add some obstacles
        obstacle_manager.add_obstacle(CircleObstacle("RED", (100, 100), 50))
        obstacle_manager.add_obstacle(RectObstacle("GREEN", pygame.Rect(200, 150, 100, 50)))
        obstacle_manager.add_obstacle(LineObstacle("BLUE", (300, 300), (400, 400), 5))

        #obstacle1 = obstacle.Obstacle(screen1, 300, 600, 600, 250)              # Create an obstacle object
        ball1 = ball.Ball(screen1)                                              # Create a ball object 
        

        #############
      
        running = True                                                          # Initialize the game loop running flag
        # Game loop
        while running:                                      
            # Timecalculation mm per second
            delta_time = clock.tick(60)/1000 
            
            events = pygame.event.get()                                                     # Get all the events that occurred
            for event in events:                                                            # Iterate through the events
                if event.type == pygame.QUIT:                                               # If the user wants to quit
                    running = False                                                         # Stop the game loop
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:         # If the user presses the escape key
                    running = False                                                         # Stop the game loop
                elif klicks == 0 and event.type == pygame.MOUSEBUTTONDOWN:                  # If the user clicks the left mouse button 
                    if event.button == pygame.BUTTON_LEFT:                                  # If it's the left button
                        ball1.position = event.pos                                          # Set the ball's position to the mouse position                                                              
                        klicks = 1                                                          # Set the number of clicks to 1
                elif klicks == 1 and event.type == pygame.MOUSEBUTTONDOWN:                  # If the user clicks the left mouse button again
                    if event.button == pygame.BUTTON_LEFT:                                  # If it's the left button
                        ball1.target = event.pos                                            # Set the ball's target position to the mouse position           
                        klicks = 2                                                          # Set the number of clicks to 2
                #Show SimParam
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI != True:                                   # If the user presses the space key   
                    drawUI = True                                                                                                       # Set the flag for drawing UI elements to True
                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#gravity_text_entry" and drawUI:        # If the user finishes editing the gravity text entry field     
                    simparam.SimParam.show_text(screen1, ball1.position, ball1.acceleration, ball1.GRAVITY)                             # Show the text with the gravity value
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI:                                           # If the user presses the space key again
                    drawUI = False                                                                                                      # Set the flag for drawing UI elements to False                
                
            #Draw graphics
            screen1.fill((255, 255, 255))                                                   # Clear the screen with white color
           # Draw obstacles
            #obstacle1.draw()
            obstacle_manager.draw(screen1)
            
            if drawUI:                                                                      # If the flag for drawing UI elements is True
                simparam.SimParam.show_UI(screen1, ball1)                                   # Show the UI elements
                pygame_widgets.update(events)                                               # Update the widgets

            if klicks > 0:                                                                  # If the number of clicks is greater than 0
                ball1.update(delta_time, klicks, obstacle)                                 # Update the ball's position and velocity
            pygame.display.update()                                                         # Update the display with the rendered graphics                       
    
        pygame.quit()                                                                       # Quit the Pygame library                                      

    game()                                                   

   
   