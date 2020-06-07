import pygame
import random

display_width, display_height = 500, 500

pygame.init()
display = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption("Insertion Sort Visualisation")
clock = pygame.time.Clock()

currRowColor = (0, 0, 0)
pastRowColor = (124,252,0)
futureRowColor = (220,20,60)
done = False

numRows = 100
numbers = [x for x in range(numRows)]
random.shuffle(numbers)

cursor = 0

def insertionStep(numbers, cursor):
    val = numbers[cursor]

    while cursor != 0 and numbers[cursor - 1] > val:
        numbers[cursor] = numbers[cursor - 1]
        numbers[cursor - 1] = val
        cursor -= 1

    return numbers

while not done:
    clock.tick(10)
    event = pygame.event.get()

    display.fill((169,169,169))

    for i in range(len(numbers)):
        if i > cursor:
            color = futureRowColor
        elif i < cursor or cursor == numRows - 1:
            color = pastRowColor
        else:
            color = currRowColor

        rect = (0, i * display_height / numRows, numbers[i] * display_height / numRows, display_height / numRows)
        pygame.draw.rect(display, color, rect)

    numbers = insertionStep(numbers, cursor)
    if cursor < numRows - 1:
        cursor += 1

    for e in event:
        if e.type == pygame.QUIT:
            done = True

    pygame.display.update()
