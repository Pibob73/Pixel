from Line import Line
from Window import Window


class Block:
    def __init__(self, left_corner, right_corner, symbol, area, head=False, floor=False, color='\033[37m'):
        self.leftCorner = left_corner
        self.rightCorner = right_corner
        self.symbol = symbol
        self.window = area
        self.color = color
        self.head = head
        self.floor = floor


    def create_block(self):
        len_width = (self.rightCorner[1] - self.leftCorner[1]) + 1
        len_height = (self.rightCorner[0] - self.leftCorner[0]) - 1
        begin_down = [0, 0]
        begin_down[0] = self.rightCorner[0]
        begin_down[1] = self.leftCorner[1]
        begin_left = [0, self.leftCorner[1]]
        begin_left[0] = self.leftCorner[0] + 1
        begin_right = [0, self.rightCorner[1]]
        begin_right[0] = self.rightCorner[0] - 1

        up_border = Line(self.symbol, self.leftCorner, len_width, 'right', self.window,
                        self.head, floor=self.floor, color=self.color)
        bottom_border = Line(self.symbol, begin_down, len_width, 'right', self.window,
                             self.head, floor=self.floor, color=self.color)
        left_border = Line(self.symbol, begin_left, len_height, 'down', self.window,
                           self.head, floor=self.floor, color=self.color)
        right_border = Line(self.symbol, begin_right, len_height, 'up', self.window,
                            self.head, floor=self.floor, color=self.color)

        up_border.create_line()
        bottom_border.create_line()
        left_border.create_line()
        right_border.create_line()
