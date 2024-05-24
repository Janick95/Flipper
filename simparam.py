import pygame
import window
import pygame_gui



class SimParam:

    pygame.init()
    text_font = pygame.font.SysFont("Arial", 10)

    def __init__(self):

        self.Manager = pygame_gui.UIManager((window.Window.WINDOWWIDTH, window.Window.WINDOWHEIGHT))
        #self.TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((25, 950), (100, 50)), manager = self.Manager, object_id="#gravity_text_entry")

    def show_text(screen, position, impulseAcceleration, gravityAcceleration):


        position = str(position)
        #positionY = str(position.y)
        impulseAccelerationX = str(impulseAcceleration.x)
        impulseAccelerationY = str(impulseAcceleration.y)
        gravityAccelerationX = str(gravityAcceleration.x)
        gravityAccelerationY = str(gravityAcceleration.y)

        posImg = SimParam.text_font.render("Position: " + position, True, "black")
        screen.blit(posImg, (20,20))
        
        impAccImg = SimParam.text_font.render("Impulse Acceleration: " + impulseAccelerationX + impulseAccelerationY, True, "black")
        screen.blit(impAccImg, (20,40))

        graAccImg = SimParam.text_font.render("Gravity Acceleration: " + gravityAccelerationX + gravityAccelerationY, True, "black")
        screen.blit(graAccImg, (20,60))
        
        
        
        

        
        
        