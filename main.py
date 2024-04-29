import pygame

pygame.init()


print ("Blub")

window_width = 800
window_height = 600

circlecolor = (200, 0, 0)
circleX = 100
circleY = 100
radius = 10


window = pygame.display.set_mode((window_width, window_height))


running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        window.fill((25,25,25))
        
        pygame.draw.circle(window, circlecolor,(circleX, circleY),radius)

        pygame.display.update()


pygame.quit()

