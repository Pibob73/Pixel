from Line import Line


class Pixel:
    def __init__(self, symbol, begin, size, area, color='\033[37m'):
        self.symbol = symbol
        self.color = color
        self.begin = begin
        self.size = size
        self.window = area

    def create_pixel(self):
        for line in range(self.size):
            position = [0, 0]
            position[0] = self.begin[0] + line
            position[1] = self.begin[1]
            Line(self.symbol, position, self.size + 5, 'right', self.window).create_line()
