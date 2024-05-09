import pygame
import ball
import window
import pygame_gui

class Game:

    #Pygame Initialieren
    pygame.init()

#Parameters
    #Colors
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    RED = (255, 0, 0)
    
    window1 = window.Window()

    def show_text(text_to_show, window1):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                
            
            window1.window.fill((255, 255, 255))
            

            pygame.display.update()




    def game(window1, show_text(text_to_show, window1)):
        
        
        clock = pygame.time.Clock()
        
        klicks = 0
        drawUI = False
        Manager = pygame_gui.UIManager((window.Window.WINDOWWIDTH, window.Window.WINDOWHEIGHT))
        GravityInput = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((25, 950), (100, 50)), manager = Manager, object_id="#gravity_text_entry")

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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE: 
                    drawUI = True
                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#gravity_text_entry" and drawUI:    
                    show_text(event.text)

                Manager.process_events(event) 
                
        #Draw graphics
            
            Manager.update(delta_time)
            window1.window.fill((255, 255, 255))
            if drawUI:
                Manager.draw_ui(window1.window)

            if klicks > 0:
                ball1.update(delta_time, klicks)
            pygame.display.update()
    
        pygame.quit()

    game(window1)





























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



   
   