import sys
import pygame

#Pygame Initialieren
pygame.init()


print ("Still works!")

# Constants
WIDTH, HEIGHT = 800, 600
GRAVITY = 0.1
FRICTION = 0.99

#Colors
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)


# Create the window
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("2D Flipper Automat")


#Circle
radius = 20
x, y = WIDTH // 2, HEIGHT // 2
velocity_x, velocity_y = 0, 0


#Main loop
while True:
    screen.fill(WHITE)

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
            running = False

   # keys = pygame.key.get_pressed()

    #if keys[pygame.K_RIGHT]:
       # ballX += 1
   # elif keys[pygame.K_LEFT]:
    #  ballX -= 1

    pygame.display.update()
pygame.quit()
sys.exit()

    #physics

    velocity_y += GRAVITY
    velocity_x *= FRICTION
    velocity_y *= FRICTION
    x += velocity_x
    y += velocity_y

    # Bounce off the walls
    if x + radius >= WIDTH or x - radius <= 0:
        velocity_x *= -1
    if y + radius >= HEIGHT or y - radius <= 0:
        velocity_y *= -1

    # Draw the circle
    pygame.draw.circle(screen, RED, (int(x), int(y)), radius)

    # Update the display
    pygame.display.flip()

    # Cap the frame rate
    pygame.time.Clock().tick(60)