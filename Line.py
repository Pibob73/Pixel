from .Letter import Letter


class Line:
    def __init__(self, symbol, begin, length, direction, area, danger=False, let=False,
                 head=False, color='\033[37m', floor=False):
        self.symbol = symbol
        self.color = color
        self.begin = begin
        self.length = length
        self.direction = direction
        self.window = area
        self.head = head
        self.floor = floor
        self.danger = danger
        self.let = let

    def create_line(self):
        for border in range(self.length):
            up = 0
            right = 0
            if self.direction == 'up':
                up = -border
            if self.direction == 'down':
                up = border
            if self.direction == 'left':
                right = -border
            if self.direction == 'right':
                right = border
            have_border = self.window.create_position(Letter(self.color + self.symbol, head=self.head),
                                                      self.begin[0] + up, self.begin[1] + right,
                                                      let=self.let, danger=self.danger)
            if not self.floor:
                if have_border == False and self.head == False:
                    return


