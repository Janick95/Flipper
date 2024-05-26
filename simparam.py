import pygame
import window
import pygame_gui
import ball
import math
import pygame_widgets
from pygame_widgets.slider import Slider



class SimParam:

    pygame.init()
    text_font = pygame.font.SysFont("Arial", 10)
    slider1 = Slider(window.Window().screen, 270, 40, 150, 20, min=0, max=9810, step=1, curved= True)
    slider2 = Slider(window.Window().screen, 500, 40, 150, 20, min=0, max=100, step=1, curved= True)

    def drawVector(screen, ball1):

        ball_x = ball1.position[0]
        ball_y = ball1.position[1]
        ball_velocity_x = ball1.velocity.x
        ball_velocity_y = ball1.velocity.y
        vector_length = math.sqrt(((ball_velocity_x)**2)+((ball_velocity_y)**2))

        vector_x = ball_x + math.cos(math.atan2(ball_velocity_y, ball_velocity_x)) * vector_length
        vector_y = ball_y + math.sin(math.atan2(ball_velocity_y, ball_velocity_x)) * vector_length
        pygame.draw.line(screen, "black", (ball_x, ball_y), (vector_x, vector_y), 2)


        arrowhead_length = 10
        arrowhead_angle = math.pi / 4
        arrowhead_x1 = vector_x - math.cos(math.atan2(ball_velocity_y, ball_velocity_x) + arrowhead_angle) * arrowhead_length
        arrowhead_y1 = vector_y - math.sin(math.atan2(ball_velocity_y, ball_velocity_x) + arrowhead_angle) * arrowhead_length
        arrowhead_x2 = vector_x - math.cos(math.atan2(ball_velocity_y, ball_velocity_x) - arrowhead_angle) * arrowhead_length
        arrowhead_y2 = vector_y - math.sin(math.atan2(ball_velocity_y, ball_velocity_x) - arrowhead_angle) * arrowhead_length
        pygame.draw.polygon(screen, "black", [(vector_x, vector_y), (arrowhead_x1, arrowhead_y1), (arrowhead_x2, arrowhead_y2)])

    def show_UI(screen, position, acceleration, GRAVITY, ball1):


        position = str(position)
        acceleration = str(acceleration)
        gravity = str(GRAVITY)
        
        posImg = SimParam.text_font.render("Position: " + position, True, "black")
        screen.blit(posImg, (20,20))
        
        accImg = SimParam.text_font.render("Acceleration: " + acceleration, True, "black")
        screen.blit(accImg, (20,40))

        gravImg = SimParam.text_font.render("Gravity: " + gravity, True, "black")
        screen.blit(gravImg, (20,60))
        

        friction1 = str(ball1.friction)

        gravImg = SimParam.text_font.render("Gravity: " + gravity, True, "black")
        screen.blit(gravImg, (270,20))

        fricImg = SimParam.text_font.render("Friction: " + friction1, True, "black")
        screen.blit(fricImg, (500,20))

        ball1.GRAVITY = SimParam.slider1.getValue()
        ball1.friction = SimParam.slider2.getValue()
        
        SimParam.drawVector(screen, ball1)