STATE = "menu" # defaults to "menu" state

def changeState(newState):
    global STATE
    STATE = newState

def getState():
    return STATE
