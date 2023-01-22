from .Line import Line

class Block:
    def __init__(self, left_corner, right_corner, symbol, area, danger=False, let=False,
                 head=False, floor=False, color='\033[37m'):
        self.leftCorner = left_corner
        self.rightCorner = right_corner
        self.symbol = symbol
        self.window = area
        self.color = color
        self.head = head
        self.floor = floor
        self.danger = danger
        self.let = let

    def create_block(self):
        height = self.rightCorner[0] - self.leftCorner[0]
        width = self.rightCorner[1] - self.leftCorner[1]
        for line in range(height):
            position = [0, 0]
            position[0] = self.leftCorner[0] + line
            position[1] = self.leftCorner[1]
            Line(self.symbol, position, width, 'right', self.window,
                 let=self.let, danger=self.danger,
                 floor=self.floor, color=self.color,head=self.head).create_line()