import pygame
import ball
import window
import pygame_gui

class Game:

    #Pygame Initialieren
    pygame.init()

    #Parameters
    
    

    def game():
                
        clock = pygame.time.Clock()
        window1 = window.Window()
        klicks = 0
        drawUI = False
        Manager = pygame_gui.UIManager((window.Window.WINDOWWIDTH, window.Window.WINDOWHEIGHT))
        GravityInput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((25, 950), (100, 50)), manager = Manager, object_id="#gravity_text_entry")
        gravity = 50
        

        #GameObjects
        #############


        ball1 = ball.Ball(window1.window)
        

        #############
      
        #Compute data
        running = True
        while running:
            
            delta_time = clock.tick(60)/1000
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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI != True: 
                    drawUI = True
                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#gravity_text_entry" and drawUI:    
                    gravity = int(event.text)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI:
                    drawUI = False

                Manager.process_events(event)
                
        #Draw graphics
            
            Manager.update(delta_time)
            window1.window.fill((255, 255, 255))
            if drawUI:
                Manager.draw_ui(window1.window)

            if klicks > 0:
                ball1.update(delta_time, klicks, gravity)
            pygame.display.update()
    
        pygame.quit()

    game()

   
   