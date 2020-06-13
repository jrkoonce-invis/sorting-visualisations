import pygame
import random
import time
from UI.button import Button
from UI.menu import Menu
from State.manager import getWidth, getHeight, changeState

class Insertion:
    def __init__(self, resetState):
        self.cursor = 0
        self.cycle = 0
        self.currRowColor = (0, 0, 0)
        self.pastRowColor = (124,252,0)
        self.futureRowColor = (220,20,60)
        self.resetState = resetState

    def createButton(self, x, y, rect):
        return Button(x, y, rect, self)

    def insertionStep(self, numbers, cursor):
        val = numbers[cursor]

        if not cursor == 0 and val < numbers[cursor - 1]:
            numbers[cursor] = numbers[cursor - 1]
            numbers[cursor - 1] = val
        else:
            self.cycle += 1
            self.cursor = self.cycle

        return numbers

    def update(self, display, event, numbers):
        display.fill((169,169,169))

        numRows = len(numbers)
        numbers = self.insertionStep(numbers, self.cursor)

        for i in range(numRows):
            if self.cursor > numRows:
                color = self.pastRowColor
            elif i == self.cursor:
                color = self.currRowColor
            else:
                color = self.futureRowColor

            rect = (0, i * getHeight() / numRows, numbers[i] * getHeight() / numRows, getHeight() / numRows)
            pygame.draw.rect(display, color, rect)

        if self.cursor > numRows:
            self.cycle = 0
            self.cursor = 0
            changeState(self.resetState)
            random.shuffle(numbers)
        else:
            self.cursor -= 1

        for e in event:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.__init__(self.resetState)
                changeState(self.resetState)
                random.shuffle(numbers)
