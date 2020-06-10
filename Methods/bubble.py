import pygame
import random
from UI.button import Button
from UI.menu import Menu
from State.manager import getWidth, getHeight, changeState

class Bubble:
    def __init__(self, resetState):
        self.cursor = 0
        self.cycles = 0
        self.switches = 0
        self.currRowColor = (0, 0, 0)
        self.rowColor = (220,20,60)
        self.doneRowColor = (124,252,0)
        self.resetState = resetState

    def createButton(self, x, y, rect):
        return Button(x, y, rect, self)

    def bubbleStep(self, numbers, cursor):
        if numbers[cursor] > numbers[cursor + 1]:
            temp = numbers[cursor + 1]
            numbers[cursor + 1] = numbers[cursor]
            numbers[cursor] = temp
            self.switches += 1

        return numbers

    def update(self, display, event, numbers):
        display.fill((169,169,169))
        numRows = len(numbers)

        if self.switches == 0 and self.cursor == numRows - 1 - self.cycles:
            self.__init__(self.resetState)
            changeState(self.resetState)
            random.shuffle(numbers)

        if self.cursor == numRows - 1 - self.cycles:
            self.cycles += 1
            self.cursor = 0
            self.switches = 0
        else:
            numbers = self.bubbleStep(numbers, self.cursor)
            self.cursor += 1

        for i in range(numRows):
            if i == self.cursor:
                color = self.currRowColor
            elif i >= numRows - self.cycles:
                color = self.doneRowColor
            else:
                color = self.rowColor

            rect = (0, i * getHeight() / numRows, numbers[i] * getHeight() / numRows, getHeight() / numRows)
            pygame.draw.rect(display, color, rect)

        for e in event:
            if e.type == pygame.KEYDOWN and e.key == pygame.K_ESCAPE:
                self.__init__(self.resetState)
                changeState(self.resetState)
                random.shuffle(numbers)
