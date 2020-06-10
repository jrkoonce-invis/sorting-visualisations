class Menu():
    def __init__(self):
        self.elements = []

    def update(self, display, event, numbers):
        display.fill((169,169,169))
        for elem in self.elements:
            elem.update(display, event)
