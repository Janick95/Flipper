import pygame
import pygame_gui
import window


class SimParam:

    
    def __init__(self):

        self.Manager = pygame_gui.UIManager((window.Window.WINDOWWIDTH, window.Window.WINDOWHEIGHT))
        #self.TEXT_INPUT = pygame_gui.elements.UITextEntryLine(relative_rect=pygame.Rect((25, 950), (100, 50)), manager = self.Manager, object_id="#gravity_text_entry")

    def show_text(position, impulseAcceleration, gravityAcceleration):

        textPosition = pygame.font.SysFont("Arial", 10).render({position}, True, "black")
        textImpulseAcc = pygame.font.SysFont("Arial", 10).render({position}, True, "black")
        textgravityAcc = pygame.font.SysFont("Arial", 10).render({position}, True, "black")

        textPosition_pos = textPosition.get_rect(rect_pos = (20, 50))
        textImpulseAcc_pos = textImpulseAcc.get_rect(rect_pos = (20,80))
        textgravityAcc_pos = textgravityAcc.get_rect(rect_pos = (20,110))

        window.Window.blit(textPosition, textPosition_pos)
        window.Window.blit(textImpulseAcc, textImpulseAcc_pos)
        window.Window.blit(textgravityAcc, textgravityAcc_pos)