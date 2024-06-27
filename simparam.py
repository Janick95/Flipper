import pygame
import window
import pygame_gui
import ball
import math
import pygame_widgets
import button
from pygame_widgets.slider import Slider


class SimParam:

    pygame.init()
    
    text_font = pygame.font.SysFont("Arial", 20)                                                                                            # Set up a font for rendering text
    slider1 = Slider(window.Window().screen, 270, 40, 150, 20, min=0, max=981, step=1, handleColour=(255, 255, 0),curved= True, initial=981)                          # Create a slider for adjusting gravity

    restart_button = button.Button("Restart", (650, 50), (100, 40), "GREY", "ORANGE", text_font)
    pause_button = button.Button("| |", (650, 150), (100, 40), "GREEN", "RED", text_font)
    
    # Calculate the window resolution into real units
    def realUnits(pixel):# Calculate the window resolution into real units
        pixel /= 10# Convert pixels to real units by dividing by 10
        return pixel


    def drawVector(screen, ball1): # Draw the velocity vector of the ball on the screen                                                                         

        ball_x = ball1.position[0]# Get the ball's current position
        ball_y = ball1.position[1]
        ball_velocity_x = ball1.velocity.x# Get the ball's velocity components
        ball_velocity_y = ball1.velocity.y
        vector_length = ball1.velocity.length()# Calculate the length of the velocity vector

        vector_x = ball_x + math.cos(math.atan2(ball_velocity_y, ball_velocity_x)) * vector_length# Calculate the end point of the velocity vector
        vector_y = ball_y + math.sin(math.atan2(ball_velocity_y, ball_velocity_x)) * vector_length
        pygame.draw.line(screen, "WHITE", (ball_x, ball_y), (vector_x, vector_y), 2)# Draw the velocity vector as a black line

        arrowhead_length = 10# Define the arrowhead parameters
        arrowhead_angle = math.pi / 4
         # Calculate the points for the arrowhead
        arrowhead_x1 = vector_x - math.cos(math.atan2(ball_velocity_y, ball_velocity_x) + arrowhead_angle) * arrowhead_length
        arrowhead_y1 = vector_y - math.sin(math.atan2(ball_velocity_y, ball_velocity_x) + arrowhead_angle) * arrowhead_length
        arrowhead_x2 = vector_x - math.cos(math.atan2(ball_velocity_y, ball_velocity_x) - arrowhead_angle) * arrowhead_length
        arrowhead_y2 = vector_y - math.sin(math.atan2(ball_velocity_y, ball_velocity_x) - arrowhead_angle) * arrowhead_length
        # Draw the arrowhead as a black polygon
        pygame.draw.polygon(screen, "WHITE", [(vector_x, vector_y), (arrowhead_x1, arrowhead_y1), (arrowhead_x2, arrowhead_y2)])

    # Display the user interface elements on the screen
    def show_UI(screen, ball1):
        #General UI
        position = str(ball1.position)
        velocity = str(ball1.velocity)
        acceleration = str(ball1.acceleration)
        gravity = str(ball1.GRAVITY)
        impulse = str(ball1.impulse)
        score = str(ball1.scoreCounter)
        
        posImg = SimParam.text_font.render("Position: " + position, True, "WHITE")
        screen.blit(posImg, (20,20))

        accImg = SimParam.text_font.render("Velocity: " + velocity, True, "WHITE")
        screen.blit(accImg, (20,40))

        accImg = SimParam.text_font.render("Acceleration: " + acceleration, True, "WHITE")
        screen.blit(accImg, (20,60))

        gravImg = SimParam.text_font.render("Gravity: " + gravity, True, "WHITE")
        screen.blit(gravImg, (20,80))

        impulseImg = SimParam.text_font.render("Impulse: " + impulse, True, "WHITE")
        screen.blit(impulseImg, (20,100))

        scoreImg = SimParam.text_font.render("Score: " + score, True, "YELLOW")
        screen.blit(scoreImg, (20,120))
        
        gravImg = SimParam.text_font.render("Gravity: " + gravity, True, "WHITE")
        screen.blit(gravImg, (270,20))



        ball1.GRAVITY = SimParam.slider1.getValue()

        SimParam.drawVector(screen, ball1)

        #Collision UI
        pygame.draw.circle(screen, "yellow", (ball1.lineCollisionPoint), 5)
        pygame.draw.circle(screen, "green", (ball1.lineStart), 5)

    
    def draw_restart_button(screen):
        SimParam.restart_button.draw(screen)
        
    def is_restart_button_clicked(event):
        return SimParam.restart_button.is_clicked(event)    
    
    def draw_pause_button(screen):
        SimParam.pause_button.draw(screen)

    def is_pause_button_clicked(event):
        return SimParam.pause_button.is_clicked(event)