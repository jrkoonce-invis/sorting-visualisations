import pygame
import random
from State.manager import getWidth, getHeight, changeState

cursor = 0
cycles = 0
switches = 0
currRowColor = (0, 0, 0)
rowColor = (220,20,60)
doneRowColor = (124,252,0)

def initBubble():
    global cursor, cycles, switches
    cursor, cycles, switched = 0, 0, 0

def bubbleStep(numbers, cursor):
    global switches
    if numbers[cursor] > numbers[cursor + 1]:
        temp = numbers[cursor + 1]
        numbers[cursor + 1] = numbers[cursor]
        numbers[cursor] = temp
        switches += 1

    return numbers

def bubblePlay(display, numbers):
    global cursor, switches, cycles
    display.fill((169,169,169))

    numRows = len(numbers)
    if cursor == numRows - 1 - cycles:
        cycles += 1
        cursor = 0
        switches = 1
    else:
        numbers = bubbleStep(numbers, cursor)
        cursor += 1

    for i in range(numRows):
        if i == cursor:
            color = currRowColor
        elif i >= numRows - cycles:
            color = doneRowColor
        else:
            color = rowColor

        rect = (0, i * getHeight() / numRows, numbers[i] * getHeight() / numRows, getHeight() / numRows)
        pygame.draw.rect(display, color, rect)

    if cursor == numRows - 1 - cycles and switches == 0:
        cursor = 0
        changeState("menu")
        random.shuffle(numbers)
        return numbers

    return numbers
