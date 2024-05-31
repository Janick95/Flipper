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
                
        clock = pygame.time.Clock()                                                                                                                              
        screen1 = window.Window().screen                                                                                                                                
        klicks = 0                                                                                                                                                  
        drawUI = False
                
        #GameObjects
        #############

        obstacle1 = obstacle.Obstacle(screen1, 300, 600, 600, 250)
        ball1 = ball.Ball(screen1)
        

        #############
      
        #Compute data
        running = True
        # Game loop
        while running:                                      
            # Timecalculation mm per second
            delta_time = clock.tick(60)/1000
            
            events = pygame.event.get()
            for event in events:               
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
                #Show SimParam
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI != True:   
                    drawUI = True 
                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#gravity_text_entry" and drawUI:     
                    simparam.SimParam.show_text(screen1, ball1.position, ball1.acceleration, ball1.GRAVITY)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI: 
                    drawUI = False                
                
            #Draw graphics
            screen1.fill((255, 255, 255))
            obstacle1.draw()
            
            if drawUI:
                simparam.SimParam.show_UI(screen1, ball1)
                pygame_widgets.update(events)

            if klicks > 0:
                ball1.update(delta_time, klicks, obstacle1)
            pygame.display.update()                         
    
        pygame.quit()                                       

    game()                                                  

   
   