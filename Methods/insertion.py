import pygame
import random
from UI.button import Button
from UI.menu import Menu
from State.manager import getWidth, getHeight, changeState

class Insertion:
    def __init__(self, resetState):
        self.cursor = 0
        self.currRowColor = (0, 0, 0)
        self.pastRowColor = (124,252,0)
        self.futureRowColor = (220,20,60)
        self.resetState = resetState

    def createButton(self, x, y, rect):
        return Button(x, y, rect, self)

    def insertionStep(self, numbers, cursor):
        val = numbers[cursor]

        while cursor != 0 and numbers[cursor - 1] > val:
            numbers[cursor] = numbers[cursor - 1]
            numbers[cursor - 1] = val
            cursor -= 1

        return numbers

    def update(self, display, event, numbers):
        display.fill((169,169,169))

        numRows = len(numbers)
        numbers = self.insertionStep(numbers, self.cursor)

        for i in range(numRows):
            if i > self.cursor:
                color = self.futureRowColor
            elif i < self.cursor or self.cursor == numRows - 1:
                color = self.pastRowColor
            else:
                color = self.currRowColor

            rect = (0, i * getHeight() / numRows, numbers[i] * getHeight() / numRows, getHeight() / numRows)
            pygame.draw.rect(display, color, rect)

        if self.cursor < numRows - 1:
            self.cursor += 1
        else:
            self.cursor = 0
            changeState(self.resetState)
            random.shuffle(numbers)

        for e in event:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.__init__(self.resetState)
                changeState(self.resetState)
                random.shuffle(numbers)
