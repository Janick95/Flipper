import pygame
import window
import pygame_gui
import ball
import pygame_widgets
from pygame_widgets.slider import Slider



class SimParam:

    pygame.init()
    text_font = pygame.font.SysFont("Arial", 10)
    slider1 = Slider(window.Window().screen, 270, 40, 150, 20, min=0, max=100, step=1, curved= True)
    slider2 = Slider(window.Window().screen, 500, 40, 150, 20, min=0, max=100, step=1, curved= True)

    def show_UI(screen, position, impulseAcceleration, gravityAcceleration, ball1):


        position = str(position)
        impulseAcceleration = str(impulseAcceleration)
        gravityAcceleration = str(gravityAcceleration)
        
        posImg = SimParam.text_font.render("Position: " + position, True, "black")
        screen.blit(posImg, (20,20))
        
        impAccImg = SimParam.text_font.render("Impulse Acceleration: " + impulseAcceleration, True, "black")
        screen.blit(impAccImg, (20,40))

        graAccImg = SimParam.text_font.render("Gravity Acceleration: " + gravityAcceleration, True, "black")
        screen.blit(graAccImg, (20,60))
        

        gravity = str(ball1.GRAVITY)
        friction = str(ball1.FRICTION)

        gravImg = SimParam.text_font.render("Gravity: " + gravity, True, "black")
        screen.blit(gravImg, (270,20))

        fricImg = SimParam.text_font.render("Friction: " + friction, True, "black")
        screen.blit(fricImg, (500,20))

        ball1.GRAVITY = SimParam.slider1.getValue()
        ball1.FRICTION = SimParam.slider2.getValue()
        