from UnitABC import UnitABC
from Letter import Letter
from Circle import Circle


class Drone:
    def __init__(self, position, symbol, area, color='\033[33m', head=False, dynamic=False):
        self.symbol = color + symbol
        self.color = color
        self.static = False
        self.head = head
        self.dynamic = dynamic
        self.position = position
        self.window = area

    def create_drone(self):
        Circle(self.position, 2, '#', self.window, color='\033[31m').create_circle()
        self.window.create_position(Letter(self.symbol, color=self.color, head=True), self.position[0], self.position[1] - 1)
    def move(self, direction):
        if direction == 'up':
            self.position[0] += -1
        if direction == 'down':
            self.position[0] += 1
        if direction == 'left':
            self.position[1] += -1
        if direction == 'right':
            self.position[1] += 1
        Circle(self.position, 2, '#', self.window, color='\033[31m').create_circle()
        self.window.create_position(Letter(self.symbol, color=self.color, head=True), self.position[0], self.position[1] - 1)