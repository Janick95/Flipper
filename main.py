# Import necessary libraries and modules
import pygame
import ball
import window
import pygame_gui
import simparam
import pygame_widgets
import obstacle

from obstacle import ObstacleManager, CircleObstacle, RectObstacle, LineObstacle

class Game:

    pygame.init()

   
    def reset_game():
        clock = pygame.time.Clock()
        screen1 = window.Window().screen
        klicks = 0
        drawUI = False

        obstacle_manager = ObstacleManager()
        obstacle_manager.add_obstacle(CircleObstacle("RED", (100, 100), 50))
        obstacle_manager.add_obstacle(RectObstacle("GREEN", pygame.Rect(200, 150, 100, 50)))
        obstacle_manager.add_obstacle(LineObstacle("BLUE", (300, 300), (400, 400), 5))

        ball1 = ball.Ball(screen1)

        return clock, screen1, klicks, drawUI, obstacle_manager, ball1

   
    def game():
        clock, screen1, klicks, drawUI, obstacle_manager, ball1 = Game.reset_game()
        running = True

        while running:
            delta_time = clock.tick(60) / 1000
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
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and not drawUI:
                    drawUI = True
                elif event.type == pygame_gui.UI_TEXT_ENTRY_FINISHED and event.ui_object_id == "#gravity_text_entry" and drawUI:
                    simparam.SimParam.show_text(screen1, ball1.position, ball1.acceleration, ball1.GRAVITY)
                elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE and drawUI:
                    drawUI = False

                # Check if the restart button is clicked
                if simparam.SimParam.is_restart_button_clicked(event):
                    clock, screen1, klicks, drawUI, obstacle_manager, ball1 = Game.reset_game()

            screen1.fill((255, 255, 255))
            obstacle_manager.draw(screen1)
            simparam.SimParam.draw_restart_button(screen1)

            if drawUI:
                simparam.SimParam.show_UI(screen1, ball1)
                pygame_widgets.update(events)

            if klicks > 0:
                ball1.update(delta_time, klicks, obstacle)

            pygame.display.update()

        pygame.quit()

   
    def run():
        Game.game()

if __name__ == "__main__":
    Game.run()
