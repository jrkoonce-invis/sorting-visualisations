import pygame
from State.manager import changeState

class Button:

    def __init__(self, x, y, color, state):
        self.x, self.y = x, y
        self.w, self.h = 100, 50
        self.color = color
        self.state = state
        self.rect = (self.x, self.y, self.w, self.h)

    def update(self, display, event):
        # Draw
        pygame.draw.rect(display, self.color, self.rect)

        # Click
        for e in event:
            if e.type == pygame.MOUSEBUTTONUP:
                pos = pygame.mouse.get_pos()
                if self.gotClicked(pos):
                    changeState(self.state)
    def gotClicked(self, pos):
        if pos[0] > self.x and pos[0] < self.x + self.w and pos[1] > self.y and pos[1] < self.y + self.h:
           return True
        else:
           return False
