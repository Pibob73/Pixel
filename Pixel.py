from Line import Line


class Pixel:
    def __init__(self, symbol, begin, size, area, danger=False, let=False,
                 color='\033[37m', head=False, floor=False):
        self.symbol = symbol
        self.color = color
        self.begin = begin
        self.size = size
        self.window = area
        self.head = head
        self.floor = floor
        self.let = let
        self.danger = danger

    def create_pixel(self):
        for line in range(self.size):
            position = [0, 0]
            position[0] = self.begin[0] + line
            position[1] = self.begin[1]
            Line(self.symbol, position, self.size + 5, 'right', self.window,
                 danger=self.danger, let=self.let,
                 floor=self.floor, color=self.color,head=self.head).create_line()
