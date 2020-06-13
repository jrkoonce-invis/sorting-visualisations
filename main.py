import pygame
import random
import time
from UI.button import Button
from UI.menu import Menu
from State.manager import *
from Methods.bubble import Bubble
from Methods.insertion import Insertion

setSize(500, 500)
done = False

# Starting pygame
pygame.init()
display = pygame.display.set_mode(getSize())
pygame.display.set_caption("Sorting Visualisation")
clock = pygame.time.Clock()

numRows = 20
numbers = [x for x in range(numRows)]
random.shuffle(numbers)

# Defaults as Menu State
mainMenu = Menu()
pastState = mainMenu
changeState(mainMenu)

# Adding sorting methods
bubbleVisual = Bubble(mainMenu)
insertionVisual = Insertion(mainMenu)
mainMenu.elements.append(bubbleVisual.createButton(200, 100, (78, 205, 196)))
mainMenu.elements.append(insertionVisual.createButton(100, 100, (26, 83, 92)))

while not done:
    clock.tick(60)
    event = pygame.event.get()

    state = getState()
    if pastState != state and not pastState == mainMenu:
        time.sleep(2)
    pastState = state

    state.update(display, event, numbers)

    for e in event:
        if e.type == pygame.QUIT:
            done = True

    pygame.display.update()
