# Import necessary libraries and modules
import pygame
import ball
import window
import pygame_gui
import simparam
import pygame_widgets
import obstacle

from obstacle import ObstacleManager, CircleObstacle, RectObstacle, LineObstacle, FlipperObstacle

class Game:

    pygame.init()

    def reset_game():
        clock = pygame.time.Clock()
        screen1 = window.Window().screen
        klicks = 0
        #drawUI = False

        obstacle_manager = ObstacleManager()
        #Passive Elements
        #obstacle_manager.add_obstacle(LineObstacle("WHITE", (0, 0), (800, 0), 5))
        #obstacle_manager.add_obstacle(LineObstacle("WHITE", (800, 800), (800, 0), 5))
        #obstacle_manager.add_obstacle(LineObstacle("WHITE", (0, 800), (0, 0), 5))

        obstacle_manager.add_obstacle(LineObstacle("BLUE", (0, 800), (250, 875), 5))
        obstacle_manager.add_obstacle(LineObstacle("BLUE", (550, 875), (800, 800), 5))

        #EckenElemente
        obstacle_manager.add_obstacle(LineObstacle("BLUE", (0, 75), (200, 0), 5))
        obstacle_manager.add_obstacle(LineObstacle("BLUE", (600, 0), (800, 75), 5))

        # Active Elements
        #flippers
        left_flipper = LineObstacle("ORANGE", (250, 875), (375, 900), 10)  # Base at (225, 900) extending downward
        right_flipper = LineObstacle("ORANGE", (550, 875), (425, 900), 10)  # Base at (600, 900) extending downward
        obstacle_manager.add_obstacle(left_flipper)
        obstacle_manager.add_obstacle(right_flipper)
        # Active Elements
        active_positions = [(250, 200), (300, 300), (350, 200), (400, 300), (450, 200), (500, 300), (550, 200), 
                            (350, 400), (450, 400), (450, 400), (400, 500)]
        for pos in active_positions:
            obstacle_manager.add_obstacle(CircleObstacle("YELLOW", pos, 20))






        ball1 = ball.Ball(screen1)
        ball2 = ball.Ball(screen1)


        return clock, screen1, klicks, obstacle_manager, ball1, ball2, left_flipper, right_flipper


    def update_flippers(left_flipper, right_flipper, left_pressed, right_pressed):
        if left_pressed:
            left_flipper.end_pos = (350, 850)  # Slightly rotated upwards
        else:
            left_flipper.end_pos = (350, 900)  # Original position

        if right_pressed:
            right_flipper.end_pos = (450, 850)  # Slightly rotated upwards
        else:
            right_flipper.end_pos = (450, 900)  # Original position
            
    def game():
        clock, screen1, klicks, obstacle_manager, ball1, ball2, left_flipper, right_flipper = Game.reset_game()
        running = True
        paused = False
        drawUI = False
        rotated = False
        left_pressed = False
        right_pressed = False

        while running:
            delta_time = clock.tick(60) / 1000 # seconds
            events = pygame.event.get()

            for event in events:
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
                elif klicks == 2 and event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == pygame.BUTTON_LEFT:
                        ball2.position = event.pos
                        klicks = 3
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not drawUI:
                    drawUI = True
                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#gravity_text_entry" and drawUI:
                    simparam.SimParam.show_text(screen1, ball1.position, ball1.acceleration, ball1.GRAVITY)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI:
                    drawUI = False

                # Check if the restart button is clicked
                elif simparam.SimParam.is_restart_button_clicked(event):
                    clock, screen1, klicks, obstacle_manager, ball1, ball2, left_flipper, right_flipper = Game.reset_game()
                # Pause the game
                elif simparam.SimParam.is_pause_button_clicked(event):
                    paused = not paused

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        left_pressed = True
                    if event.key == pygame.K_RIGHT:
                        right_pressed = True

                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_LEFT:
                        left_pressed = False
                    if event.key == pygame.K_RIGHT:
                        right_pressed = False
                 # Update flippers based on key press state
                Game.update_flippers(left_flipper, right_flipper, left_pressed, right_pressed)




            if not paused:
                screen1.fill((0, 0, 0))
                obstacle_manager.draw(screen1)
                simparam.SimParam.draw_restart_button(screen1)
                simparam.SimParam.draw_pause_button(screen1)

                if drawUI:
                    simparam.SimParam.show_UI(screen1, ball1)
                    pygame_widgets.update(events)

                if klicks > 0:
                    ball1.update(delta_time, klicks, obstacle_manager.obstacles)
                if klicks == 3:
                    ball2.update(delta_time, klicks, obstacle_manager.obstacles)

                pygame.display.update()

        pygame.quit()

    def run():
        Game.game()

if __name__ == "__main__":
    Game.run()
