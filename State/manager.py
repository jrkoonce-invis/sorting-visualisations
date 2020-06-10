STATE = "menu" # defaults to "menu" state
WIDTH = 500 # defaults to 500
HEIGHT = 500 # defaults to 500

def changeState(newState):
    global STATE
    STATE = newState

def getState():
    return STATE

def getWidth():
    return WIDTH

def getHeight():
    return HEIGHT

def setSize(width, height):
    global WIDTH, HEIGHT
    WIDTH = width
    HEIGHT = height

def getSize():
    return (WIDTH, HEIGHT)
