from Letter import Letter
class Fill:
    def __init__(self, center, symbol, area, head=False, color='\033[33m'):
        self.center = center
        self.color = color
        self.symbol = symbol
        self.window = area
        self.head = head

    def fill(self):
        for x in range(self.window.height):
            for y in range(self.window.width):
                if y < self.window.width:
                    self.window.create_position(Letter(self.color + self.symbol, head=self.head), x, y)