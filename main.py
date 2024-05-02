import pygame

pygame.init()


print ("Funktioniert noch")


window_width = 800
window_height = 600

ballcolor = (200, 0, 0)
ballX = window_width/2
ballY = window_height/2
radius = 10


window = pygame.display.set_mode((window_width, window_height))


running = True
while running:
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


    window.fill((25,25,25))
        
    pygame.draw.circle(window, ballcolor,(ballX, ballY),radius)

    pygame.display.update()


pygame.quit()

