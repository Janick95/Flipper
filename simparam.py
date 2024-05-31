import pygame
import window
import pygame_gui
import ball
import math
import pygame_widgets
from pygame_widgets.slider import Slider

class SimParam:

    pygame.init()
    text_font = pygame.font.SysFont("Arial", 15)                                                                                            # Set up a font for rendering text
    slider1 = Slider(window.Window().screen, 270, 40, 150, 20, min=0, max=9810, step=1, curved= True, initial=100)                          # Create a slider for adjusting gravity
    
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
        pygame.draw.line(screen, "black", (ball_x, ball_y), (vector_x, vector_y), 2)# Draw the velocity vector as a black line

        arrowhead_length = 10# Define the arrowhead parameters
        arrowhead_angle = math.pi / 4
         # Calculate the points for the arrowhead
        arrowhead_x1 = vector_x - math.cos(math.atan2(ball_velocity_y, ball_velocity_x) + arrowhead_angle) * arrowhead_length
        arrowhead_y1 = vector_y - math.sin(math.atan2(ball_velocity_y, ball_velocity_x) + arrowhead_angle) * arrowhead_length
        arrowhead_x2 = vector_x - math.cos(math.atan2(ball_velocity_y, ball_velocity_x) - arrowhead_angle) * arrowhead_length
        arrowhead_y2 = vector_y - math.sin(math.atan2(ball_velocity_y, ball_velocity_x) - arrowhead_angle) * arrowhead_length
        # Draw the arrowhead as a black polygon
        pygame.draw.polygon(screen, "black", [(vector_x, vector_y), (arrowhead_x1, arrowhead_y1), (arrowhead_x2, arrowhead_y2)])

    # Display the user interface elements on the screen
    def show_UI(screen, ball1):

        #General UI
        # Convert ball attributes to strings
        position = str(ball1.position)
        velocity = str(ball1.velocity)
        acceleration = str(ball1.acceleration)
        gravity = str(ball1.GRAVITY)
        impulse = str(ball1.impulse)
        
        # Render and display the ball's position
        posImg = SimParam.text_font.render("Position: " + position, True, "black")
        screen.blit(posImg, (20,20))

        # Render and display the ball's velocity
        accImg = SimParam.text_font.render("Velocity: " + velocity, True, "black")
        screen.blit(accImg, (20,40))

        # Render and display the ball's acceleration
        accImg = SimParam.text_font.render("Acceleration: " + acceleration, True, "black")
        screen.blit(accImg, (20,60))

        # Render and display the current gravity value
        gravImg = SimParam.text_font.render("Gravity: " + gravity, True, "black")
        screen.blit(gravImg, (20,80))

        # Render and display the ball's impulse
        impulseImg = SimParam.text_font.render("Impulse: " + impulse, True, "black")
        screen.blit(impulseImg, (20,100))
        
        # Render and display the current gravity value again
        gravImg = SimParam.text_font.render("Gravity: " + gravity, True, "black")
        screen.blit(gravImg, (270,20))

        # Update the ball's gravity based on the slider value
        ball1.GRAVITY = SimParam.slider1.getValue()

        # Draw the velocity vector of the ball
        SimParam.drawVector(screen, ball1)

        #Collision UI
        # Draw a small yellow circle at the collision point
        pygame.draw.circle(screen, "yellow", (ball1.lineCollisionPoint), 5)
        # Draw a small green circle at the start of the line
        pygame.draw.circle(screen, "green", (ball1.lineStart), 5)