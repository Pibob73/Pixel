from UnitABC import UnitABC
from Letter import Letter
from Circle import Circle
class Drone:
    def __init__(self, position, symbol, area, danger=False, let=False
                 , direction='', color='\033[33m', head=False, dynamic=False):
        self.symbol = color + symbol
        self.color = color
        self.static = False
        self.head = head
        self.dynamic = dynamic
        self.position = position
        self.window = area
        self.direction = direction
        self.let = let
        self.danger = danger

    def create_drone(self):
        #car(self.position[0], self.position[1], self.window)
        self.window.create_position(Letter(self.symbol, color=self.color, head=True), self.position[0], self.position[1])

    def can_move(self, direction):
        move_on_row = self.position[0]
        move_on_column = self.position[1]
        if direction == 'up':
            move_on_row += -1
        if direction == 'down':
            move_on_row += 1
        if direction == 'left':
            move_on_column += -1
        if direction == 'right':
            move_on_column += 1
        return self.window.let[move_on_row][move_on_column]
    def danger_zone(self):
        return self.window.danger[self.position[0]][self.position[1]]
    def move(self, direction=''):
        if self.can_move(direction):
            self.window.create_position(Letter(self.symbol, color=self.color, head=True), self.position[0],
                                        self.position[1])
            return
        if direction == 'up':
            self.position[0] += -1
        if direction == 'down':
            self.position[0] += 1
        if direction == 'left':
            self.position[1] += -1
        if direction == 'right':
            self.position[1] += 1
        #car(self.position[0], self.position[1], self.window)
        self.window.create_position(Letter(self.symbol, color=self.color, head=True), self.position[0], self.position[1])