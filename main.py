import pygame
import random
from UI.button import Button
from Methods.insertion import insertionPlay
from State.manager import getState

display_width, display_height = 500, 500

pygame.init()
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Sorting Visualisation")
clock = pygame.time.Clock()

rowColor = (0, 0, 0)
done = False

numRows = 100
numbers = [x for x in range(numRows)]
random.shuffle(numbers)

elements = []

# Adding buttons to menu (state: "menu")
insertionButton = Button(100, 100, (26, 83, 92), "insertion")
elements.append(insertionButton)

while not done:
    clock.tick(30)
    event = pygame.event.get()

    state = getState()

    if state == "menu":
        display.fill((169,169,169))
        for elem in elements:
            elem.update(display, event)
    elif state == "insertion":
        insertionPlay(display)

    for e in event:
        if e.type == pygame.QUIT:
            done = True

    pygame.display.update()
